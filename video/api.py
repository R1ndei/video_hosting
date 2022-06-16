from typing import List

from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks, Depends
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from user.auth import get_user

from .schemas import GetListVideo, GetVideo
from .models import Video, User
from .services import save_video, open_file

video_router = APIRouter(prefix='/video', tags=["video"])
templates = Jinja2Templates(directory="templates")