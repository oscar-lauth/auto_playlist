from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import songs
from routers import user_auth

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

# @app.on_event("startup")
# async def startup_event():
#     session = aiohttp.ClientSession()

@app.get("/")
async def root():
    return {"message": "Hello There"}
