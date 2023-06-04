from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from api import songs, auth, playlist
import uvicorn
import config

app = FastAPI()


settings:config.Settings=config.get_settings()

origins = [settings.frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
    max_age=3600,
)

app.include_router(songs.router)
app.include_router(auth.router)
app.include_router(playlist.router)

@app.get("/test")
async def test():
    return {"Test":"Good"}

@app.get("/")
async def root():
    return {"message": "Hello There"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.backend_host,
        port=settings.backend_port,
        log_level="info",
        reload=True
    )