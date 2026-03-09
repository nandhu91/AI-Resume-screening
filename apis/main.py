from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from apis.routes import router

app = FastAPI(title="AI Resume Analysis & Ranking System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Router mappings
app.include_router(router, prefix="/api")

# Serve HR dashboard interface
dashboard_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dashboard")

if os.path.exists(dashboard_dir):
    app.mount("/static", StaticFiles(directory=dashboard_dir), name="static")

    @app.get("/")
    async def serve_dashboard():
        index_path = os.path.join(dashboard_dir, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        return {"msg": "Dashboard frontend index.html not found! Check directory paths."}
