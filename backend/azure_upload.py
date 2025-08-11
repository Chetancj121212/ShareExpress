import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables from .env file

# Load environment variables from .env file
load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_FILEUPLOAD = os.getenv("AZURE_CONTAINER_FILEUPLOAD")
CONTAINER_QRUPLOAD = os.getenv("AZURE_CONTAINER_QRUPLOAD")
CONTAINER_TXTUPLOAD = os.getenv("AZURE_CONTAINER_TXTUPLOAD")

if not AZURE_STORAGE_CONNECTION_STRING:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set. Check your .env file.")
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_to_container(container_name, file_path, blob_name=None):
    """
    Uploads a file to the specified Azure Blob container.
    :param container_name: Name of the container
    :param file_path: Path to the local file
    :param blob_name: Name for the blob in Azure (optional)
    """
    if not blob_name:
        blob_name = os.path.basename(file_path)
    container_client = blob_service_client.get_container_client(container_name)
    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    return f"Uploaded {blob_name} to {container_name}"

# Convenience functions for each container
def upload_file(file_path, blob_name=None):
    return upload_to_container(CONTAINER_FILEUPLOAD, file_path, blob_name)

def upload_qr(file_path, blob_name=None):
    return upload_to_container(CONTAINER_QRUPLOAD, file_path, blob_name)

def upload_text(file_path, blob_name=None):
    return upload_to_container(CONTAINER_TXTUPLOAD, file_path, blob_name)
