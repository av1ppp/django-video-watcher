from .models import VideoThumbnail, VideoUnit, VideoFile
import cv2
from random import randint
from django.conf import settings
from os import path

def create_videounit(title, video):
    vu = VideoUnit.objects.create(title=title)
    vu.save()

    vf = VideoFile.objects.create(videounit=vu, file=video)
    vf.save()

    vt = _get_thumbnail(vu, vf)
    vt.save()
    
def _get_thumbnail(videounit, videofile):
    vt = VideoThumbnail(videounit=videounit)
    image_path = path.splitext(videofile.file.path)[0] + '_thumbnail.png'
    
    cap = cv2.VideoCapture(videofile.file.path)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.set(cv2.CAP_PROP_POS_FRAMES, randint(0, frame_count) - 1)
    _, frame = cap.read()
    cv2.imwrite(image_path, frame)
    cap.release()
    
    vt.file = path.relpath(image_path, settings.MEDIA_ROOT)
    
    return vt

def get_errors_with_form(form):
    error_string = ''
    for field in form:
        if field.errors:
            for error in field.errors:
                error_string += error + '\n'
    return error_string