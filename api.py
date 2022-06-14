from fastapi import File, UploadFile, APIRouter, Form, HTTPException
import shutil
from typing import List
from uuid import uuid4

from starlette.responses import StreamingResponse

from services import save_video

from starlette.background import BackgroundTasks

from models import Video, User

from schemas import UploadVideo, GetVideo, Message

video_router = APIRouter()


@video_router.post("/")
async def create_video(back_tasks: BackgroundTasks, title: str = Form(...), description: str = Form(...),
                       file: UploadFile = File(...)):
    user = await User.objects.first()
    return await save_video(user, file, title, description, back_tasks)


@video_router.get("/video/{video_pk}", responses={404: {'model': Message}})
async def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.dict().get('file'), mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")
