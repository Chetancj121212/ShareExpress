# ShareExpress

 A full-stack application with a Python backend and a Next.js frontend for sharing files and short links.

 ## Project Structure

 - `backend/` — Python FastAPI backend
 - `frontend/` — Next.js frontend

# ShareExpress

ShareExpress is a full-stack web application for secure file sharing and short link management. It features a Python backend and a Next.js frontend, designed for easy deployment on Railway.

 ## Backend
- Upload files securely and generate shareable links
- Create and manage short links for files or URLs
- Modern, responsive UI built with Next.js and Tailwind CSS
- Azure Blob Storage integration for scalable file storage
- RESTful API for backend operations
- Environment variable support for secrets and configuration

 - Written in Python
- Python (FastAPI)
- Next.js (React, TypeScript)
- Azure Blob Storage
- Railway (deployment)
- Tailwind CSS

 - Handles file uploads and short link generation
- `backend/` — Python FastAPI backend
- `frontend/` — Next.js frontend

 - Requirements listed in `backend/requirements.txt`
- Handles file uploads, short link generation, and API endpoints
- Requirements listed in `backend/requirements.txt`
- Entry point: `backend/main.py`
- Deployment: `backend/Procfile`

 - Entry point: `backend/main.py`
 - Procfile for Railway/Heroku deployment

 ### Running Locally
 ```bash
 cd backend

 pip install -r requirements.txt
- User interface for uploading files and accessing short links
- Requirements listed in `frontend/package.json`

 python main.py
 ```

 ## Frontend
 - Built with Next.js (React + TypeScript)
 - UI for uploading files and accessing short links

 - Requirements listed in `frontend/package.json`
Set the following environment variables in Railway or locally:
- `AZURE_STORAGE_CONNECTION_STRING` — Azure Blob Storage connection string
- Any other secrets required by your backend


1. Push your code to GitHub.
2. Connect your repository to Railway.
3. Set up environment variables in Railway dashboard.
4. Railway will auto-detect and build both backend and frontend.
5. For backend, ensure `Procfile` is present.

 ### Running Locally
1. Open the frontend in your browser.
2. Upload a file or create a short link.
3. Share the generated link with others.

 ```bash
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

 cd frontend
MIT
 npm install
 npm run dev
 ```

 ## Deployment (Railway)
 1. Push your code to GitHub.
 2. Connect your repo to Railway.
 3. Set up environment variables (e.g., Azure keys) in Railway dashboard.
 4. Railway will auto-detect and build both backend and frontend.
 5. For backend, ensure `Procfile` is present.

 ## Environment Variables
 - Store secrets (e.g., Azure credentials) in Railway's environment settings.

 ## License
 MIT

