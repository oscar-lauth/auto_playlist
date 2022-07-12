from venv import create
from fastapi import APIRouter
from spotify_api.playlist import new_playlist

router = APIRouter()

@router.post("/create_playlist")
async def create_playlist(name:str):
    return new_playlist(name)