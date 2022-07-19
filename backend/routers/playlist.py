from fastapi import APIRouter
from spotify.api import generate_playlist
from spotify.api import create_playlist

router = APIRouter()

@router.post("/playlist/generate",status_code=201,description="Add songs")
async def add_songs(size:int=20):
    response = generate_playlist(size)
    return response

@router.post("/playlist/{name}",status_code=201,description="Creates new playlist by name")
async def new_playlist(name:str):
    response = create_playlist(name)
    return response


    