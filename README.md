# ShareExpress

This project contains a Python backend and a Next.js frontend.

## Deployment on Railway

1. **Backend**
   - Ensure your `requirements.txt` and `Procfile` are up to date in the `backend/` folder.
   - Add any required environment variables in Railway's dashboard (e.g., Azure keys).
   - Set the Railway service to run the backend using the command in `Procfile`.

2. **Frontend**
   - The frontend is a Next.js app in the `frontend/` folder.
   - Railway will detect and build the Next.js app automatically.
   - Add any required environment variables in Railway's dashboard.

3. **General**
   - Push your code to GitHub and connect the repo to Railway.
   - Set up environment variables/secrets in Railway as needed.
   - Deploy!

## Useful Commands

- Backend: `pip install -r requirements.txt`
- Frontend: `npm install && npm run build`

---

For more details, see Railway docs: https://docs.railway.app/
