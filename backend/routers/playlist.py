from fastapi import APIRouter
from spotify.api import create_playlist

router = APIRouter()

@router.post("/playlist/{name}",status_code=201,description="Creates new playlist by name")
async def new_playlist(name:str):
    response = create_playlist(name)
    return response

@router.post("/playlist/generate",status_code=201,description="Add songs")
async def add_songs(playlist_id:str):
    pass