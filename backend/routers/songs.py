from fastapi import APIRouter
from spotify.api import get_recommendations
from spotify.api import get_top_tracks_raw, get_top_artists_raw

router = APIRouter()

@router.get("/top_songs")
async def get_top_songs():
    response = get_top_tracks_raw()
    return response

@router.get("/top_artists")
async def get_top_artists():
    response = get_top_artists_raw()
    return response

@router.get("/recs")
async def get_recs():
    response = get_recommendations()
    res=[]
    for track in response["tracks"]:
        a = []
        for artists in track["artists"]:
            a.append(artists["name"])
        res.append({track["name"]:a})
    return res