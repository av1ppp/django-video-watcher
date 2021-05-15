from .forms import UploadVideoForm, DeleteVideoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import VideoFile, VideoUnit

def catalog(request):
    videos = VideoUnit.objects.all()
    for v in videos:
        v.delete_form = DeleteVideoForm(initial={'video_id': v.id})

    context = {
        'videos': videos,
        'add_form': UploadVideoForm(),
    }

    return render(request, 'catalog/index.html', context)

def make_error_string(form):
    error_string = ''
    for field in form:
        if field.errors:
            for error in field.errors:
                error_string += error + '\n'


def create_video(request):
    if request.method == 'POST':
        add_form = UploadVideoForm(request.POST, request.FILES)
        if add_form.is_valid():
            title = add_form.cleaned_data.get('title')
            video = add_form.cleaned_data.get('video')

            vu = VideoUnit.objects.create(title=title)
            vu.save()

            vf = VideoFile.objects.create(videounit=vu, file=video)
            vf.save()

            return HttpResponseRedirect('../')

        return HttpResponse(make_error_string(add_form))

def delete_video(request):
    if request.method == 'POST':
        delete_form = DeleteVideoForm(request.POST)
        if delete_form.is_valid():
            video_id = delete_form.cleaned_data.get('video_id')
            VideoUnit.objects.filter(id=video_id).delete()
            return HttpResponseRedirect('../')
        
        return HttpResponse(make_error_string(delete_form))

    return HttpResponseRedirect('../')
