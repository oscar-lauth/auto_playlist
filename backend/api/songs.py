from fastapi import APIRouter, HTTPException, Request
from spotify.utils import get_user_from_session
from spotify.api import get_recommendations
from spotify.api import get_top_tracks_raw, get_top_artists_raw

router = APIRouter()

@router.get("/top_songs")
async def get_top_songs(request: Request):
    user = get_user_from_session(request)
    if user is None:
        raise HTTPException(status_code=401, detail="User session data not found")
    response = get_top_tracks_raw(user)
    return response

@router.get("/top_artists")
async def get_top_artists(request: Request):
    user = get_user_from_session(request)
    if user is None:
        raise HTTPException(status_code=401, detail="User session data not found")
    response = get_top_artists_raw(user)
    return response

@router.get("/recs")
async def get_recs(request: Request):
    user = get_user_from_session(request)
    if user is None:
        raise HTTPException(status_code=401, detail="User session data not found")
    response = get_recommendations(user)
    res=[]
    for track in response["tracks"]:
        a = []
        for artists in track["artists"]:
            a.append(artists["name"])
        res.append({track["name"]:a})
    return res