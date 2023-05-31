from fastapi import APIRouter, Request
from spotify.api import get_recommendations
from spotify.api import get_top_tracks_raw, get_top_artists_raw

router = APIRouter()

@router.get("/top_songs")
async def get_top_songs(request: Request):
    response = get_top_tracks_raw(request)
    return response

@router.get("/top_artists")
async def get_top_artists(request: Request):
    response = get_top_artists_raw(request)
    return response

@router.get("/recs")
async def get_recs(request: Request):
    response = get_recommendations(request)
    res=[]
    for track in response["tracks"]:
        a = []
        for artists in track["artists"]:
            a.append(artists["name"])
        res.append({track["name"]:a})
    return res