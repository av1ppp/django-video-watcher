from .forms import UploadVideoForm, DeleteVideoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Snapshot, Video, VideoFile


def catalog(request):
    videos = Video.objects.all()
    for v in videos:
        v.delete_form = DeleteVideoForm(initial={'video_id': v.id})

    context = {
        'videos': videos,
        'add_form': UploadVideoForm(),
    }

    return render(request, 'catalog/index.html', context)

def create_video(request):
    if request.method == 'POST':
        add_form = UploadVideoForm(request.POST, request.FILES)
        if add_form.is_valid():
            name = add_form.cleaned_data.get('name')
            image = add_form.cleaned_data.get('image')
            videofile = add_form.cleaned_data.get('videofile')
            obj = Video.objects.create(
                name = name,
                snapshot = Snapshot.objects.create(file = image),
                videofile = VideoFile.objects.create(file = videofile),
            )
            obj.save()
            return HttpResponseRedirect('../')

        error_string = ''
        for field in add_form:
            if field.errors:
                for error in field.errors:
                    error_string += error + '\n'
        return HttpResponse(error_string)

def delete_video(request):
    if request.method == 'POST':
        delete_form = DeleteVideoForm(request.POST)
        if delete_form.is_valid():
            video_id = delete_form.cleaned_data.get('video_id')
            Video.objects.filter(id=video_id).delete()
            return HttpResponseRedirect('../')
        
        error_string = ''
        for field in delete_form:
            if field.errors:
                for error in field.errors:
                    error_string += error + '\n'
        return HttpResponse(error_string)

    return HttpResponseRedirect('../')
