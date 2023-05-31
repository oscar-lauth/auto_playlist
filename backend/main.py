from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from api import songs, user_auth, playlist
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
    secret_key=settings.secret_key
)

app.include_router(songs.router)
app.include_router(user_auth.router)
app.include_router(playlist.router)

# @app.on_event("startup")
# async def startup_event():
#     session = aiohttp.ClientSession()

@app.get("/test")
async def test():
    return {"Test":"Good"}

@app.get("/")
async def root():
    return {"message": "Hello There"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        log_level="info",
        reload=True
    )