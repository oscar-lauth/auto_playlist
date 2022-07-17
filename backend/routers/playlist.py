from fastapi import APIRouter
from spotify.api import create_playlist

router = APIRouter()

@router.post("/playlist")
async def new_playlist(name:str):
    return create_playlist(name)