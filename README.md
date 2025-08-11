# ShareExpress

ShareExpress is a full-stack web application for secure file sharing and short link management. It features a Python FastAPI backend and a Next.js frontend.

## Project Structure

- `backend/` — Python FastAPI backend
- `frontend/` — Next.js frontend

## Backend (FastAPI)

- Handles file uploads and short link generation
- RESTful API endpoints
- Azure Blob Storage integration
- Requirements listed in `backend/requirements.txt`
- Entry point: `backend/main.py`
- Deployment: `backend/Procfile` (Railway/Heroku) and `render.yaml` (Render)

## Frontend (Next.js)

- Modern, responsive UI built with Next.js and Tailwind CSS
- Connects to backend API
- Deployment: Vercel

---

## Deployment Instructions

### Backend on Render

1. Sign up at [Render](https://render.com) and create a new Web Service.
2. Connect your GitHub repo or upload your backend files.
3. Render auto-detects Python projects. Ensure your `requirements.txt` and `Procfile` are present.
4. (Optional) Add a `render.yaml` for advanced config.
5. Set environment variables (e.g., `AZURE_STORAGE_CONNECTION_STRING`).
6. Render will build and deploy your backend. You’ll get a public API URL.

### Backend on Railway

1. Sign up at [Railway](https://railway.app) and create a new project.
2. Connect your GitHub repo or upload your backend files.
3. Ensure your `requirements.txt` and `Procfile` are present.
4. Set environment variables (e.g., `AZURE_STORAGE_CONNECTION_STRING`).
5. Railway will build and deploy your backend. You’ll get a public API URL.

### Frontend on Vercel

1. Sign up at [Vercel](https://vercel.com) and create a new project.
2. Connect your GitHub repo and select the `frontend/` directory.
3. Vercel auto-detects Next.js projects. No config needed, but you can add a `vercel.json` for custom settings.
4. Set environment variables (e.g., `NEXT_PUBLIC_API_URL` to your backend URL).
5. Vercel will build and deploy your frontend. You’ll get a public URL.

---

## Environment Variables

### Backend
- `AZURE_STORAGE_CONNECTION_STRING`: Azure Blob Storage connection string
- `OTHER_SECRET`: Any other secrets required

### Frontend
- `NEXT_PUBLIC_API_URL`: URL of your deployed backend

---

## Example Files

- `backend/Procfile`:
	```
	web: uvicorn main:app --host 0.0.0.0 --port $PORT
	```
- `backend/render.yaml`:
	```yaml
	services:
		- type: web
			name: shareexpress-backend
			env: python
			buildCommand: "pip install -r requirements.txt"
			startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
			autoDeploy: true
			envVars:
				- key: AZURE_STORAGE_CONNECTION_STRING
					sync: false
				- key: OTHER_SECRET
					sync: false
	```
- `frontend/vercel.json`:
	```json
	{
		"version": 2,
		"builds": [
			{ "src": "next.config.ts", "use": "@vercel/next" }
		],
		"env": {
			"NEXT_PUBLIC_API_URL": "https://your-backend-url.onrender.com"
		}
	}
	```

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

