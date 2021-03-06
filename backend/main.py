from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import songs, user_auth, playlist
import uvicorn

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(songs.router)
app.include_router(user_auth.router)
app.include_router(playlist.router)

# @app.on_event("startup")
# async def startup_event():
#     session = aiohttp.ClientSession()

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