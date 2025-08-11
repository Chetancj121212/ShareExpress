from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import json
import random
import string
from azure_upload import upload_file, upload_text
from azure.storage.blob import BlobServiceClient
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

SHORTLINKS_FILE = "shortlinks.json"
def generate_short_code(length=3):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def load_shortlinks():
    if not os.path.exists(SHORTLINKS_FILE):
        return {}
    with open(SHORTLINKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_shortlinks(shortlinks):
    with open(SHORTLINKS_FILE, "w", encoding="utf-8") as f:
        json.dump(shortlinks, f)
@app.post("/shorten")
async def shorten_link(file_id: str = Form(...)):
    shortlinks = load_shortlinks()
    # Ensure unique code
    for _ in range(100):
        code = generate_short_code()
        if code not in shortlinks:
            shortlinks[code] = file_id
            save_shortlinks(shortlinks)
            base_url = os.getenv("BASE_URL", "http://localhost:8000")
            short_url = f"{base_url}/s/{code}"
            return {"short_url": short_url, "code": code, "file_id": file_id}
    return {"error": "Could not generate unique code"}


@app.get("/s/{code}")
async def resolve_shortlink(code: str):
    shortlinks = load_shortlinks()
    file_id = shortlinks.get(code)
    if not file_id:
        return {"error": "Shortlink not found"}
    # Determine container by file type
    if file_id.endswith('.txt'):
        container = os.getenv("AZURE_CONTAINER_TXTUPLOAD", "txtupload")
    else:
        container = os.getenv("AZURE_CONTAINER_FILEUPLOAD", "fileupload")
    account = os.getenv("AZURE_STORAGE_ACCOUNT", "shareexpress")
    file_url = f"https://{account}.blob.core.windows.net/{container}/{file_id}"
    return {"file_url": file_url, "file_id": file_id}


# No need to create uploads folder or serve static files

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>📤 Share Files & Text via Link</h2>
    <form action="/upload_file" enctype="multipart/form-data" method="post">
        <input type="file" name="file"><br><br>
        <button type="submit">Upload File</button>
    </form>
    <hr>
    <form action="/upload_text" method="post">
        <textarea name="text" rows="4" cols="40" placeholder="Enter text here"></textarea><br><br>
        <button type="submit">Upload Text</button>
    </form>
    """

@app.post("/upload_file")
async def upload_file_endpoint(file: UploadFile = File(...)):
    try:
        if not file.filename:
            return {"error": "No file provided"}
        file_id = str(uuid.uuid4()) + "_" + file.filename
        # Read file content
        content = await file.read()
        # Save to Azure Blob Storage
        temp_path = f"/tmp/{file_id}" if os.name != "nt" else f"{file_id}"
        with open(temp_path, "wb") as f:
            f.write(content)
        upload_file(temp_path, file_id)
        os.remove(temp_path)
        # Generate Azure Blob URL
        # Direct Azure Blob Storage link
        account = os.getenv("AZURE_STORAGE_ACCOUNT", "shareexpress")
        container = os.getenv("AZURE_CONTAINER_FILEUPLOAD", "fileupload")
        link = f"https://{account}.blob.core.windows.net/{container}/{file_id}"
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
        return {
            "link": link,
            "shared_link": f"{frontend_url}/shared/{file_id}"
        }
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return {"error": f"Failed to upload file: {str(e)}"}

@app.post("/upload_text")
async def upload_text_endpoint(text: str = Form(...)):
    file_id = str(uuid.uuid4()) + ".txt"
    temp_path = f"/tmp/{file_id}" if os.name != "nt" else f"{file_id}"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(text)
    upload_text(temp_path, file_id)
    os.remove(temp_path)
    # Direct Azure Blob Storage link
    account = os.getenv("AZURE_STORAGE_ACCOUNT", "shareexpress")
    container = os.getenv("AZURE_CONTAINER_TXTUPLOAD", "txtupload")
    link = f"https://{account}.blob.core.windows.net/{container}/{file_id}"
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    return {
        "link": link,
        "shared_link": f"{frontend_url}/shared/{file_id}"
    }
# Add endpoint to stream files from Azure Blob Storage
@app.get("/download/{file_id}")
async def download_file(file_id: str, type: str = "file"):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if type == "text":
        container = os.getenv("AZURE_CONTAINER_TXTUPLOAD", "txtupload")
    else:
        container = os.getenv("AZURE_CONTAINER_FILEUPLOAD", "fileupload")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container, blob=file_id)
    stream = blob_client.download_blob()
    content_type = "text/plain" if type == "text" else "application/octet-stream"
    return StreamingResponse(stream.chunks(), media_type=content_type, headers={"Content-Disposition": f"attachment; filename={file_id}"})

@app.get("/file-info/{file_id}")
async def get_file_info(file_id: str):
    """Get file metadata from Azure Blob Storage (basic info)"""
    try:
        # Only returns file name and type, not size
        is_text = file_id.endswith('.txt')
        return {
            "filename": file_id,
            "is_text": is_text,
            "exists": True
        }
    except Exception as e:
        return {"error": str(e)}
