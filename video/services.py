from .models import VideoThumbnail, VideoUnit, VideoFile
import cv2
from random import randint
import uuid
from django.conf import settings
from django import forms
from django.db import models
from os import path

def create_videounit(title, video) -> None:
    u = _generate_uuid4()

    vu = VideoUnit.objects.create(id=u, title=title)
    vu.save()

    vf = VideoFile.objects.create(videounit=vu, file=video)
    vf.save()

    thumbnail_path = path.join(vu.get_root_dir(), 'thumbnail.png')
    _save_random_frame_from_video(vf.file.path, thumbnail_path)
    vt = VideoThumbnail(videounit=vu, file = path.relpath(thumbnail_path, settings.MEDIA_ROOT))
    vt.save()

def _generate_uuid4():
    while True:
        u = uuid.uuid4()
        if not VideoUnit.objects.filter(id=u):
            return u

def _save_random_frame_from_video(video_path, frame_file_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    cap.set(cv2.CAP_PROP_POS_FRAMES, randint(0, frame_count) - 1)
    _, frame = cap.read()
    cv2.imwrite(frame_file_path, frame)
    cap.release()

def get_error_str_with_form(form) -> str:
    error_string = ''
    for field in form:
        if field.errors:
            for error in field.errors:
                error_string += error + '\n'
    return error_string