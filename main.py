from fastapi import FastAPI
from app import __version__
from app.routers import version

app = FastAPI(title="HiveBox App", version=__version__)

app.include_router(version.router)
