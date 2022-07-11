from fastapi import APIRouter

router = APIRouter()

@router.get("/song/")
async def get_song():
    return {
        "title": "Good News",
        "artists":["Mac Miller"],
        "album": "Circles",
        "duration": 127,
    }
