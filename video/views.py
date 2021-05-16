from .forms import UploadVideoForm, DeleteVideoForm
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import VideoUnit
from . import services

def catalog(request):
    videos = VideoUnit.objects.all()
    for v in videos:
        v.delete_form = DeleteVideoForm(initial={'video_id': v.id})
        v.formatted_id = str(v.id)[:8]

    context = {'videos': videos, 'add_form': UploadVideoForm()}

    return render(request, 'catalog/index.html', context)

def watch(request):
    v = request.GET.get('v', '')
    if not v:
        return HttpResponseNotFound('Not Found')

    video = VideoUnit.objects.get(id=v)
    if not video:
        return HttpResponseNotFound('Not Found')

    context = {'video': video}
    return render(request, 'watch/index.html', context)

def create_video(request):
    if request.method == 'POST':
        add_form = UploadVideoForm(request.POST, request.FILES)
        if add_form.is_valid():
            services.create_videounit(
                add_form.cleaned_data.get('title'),
                add_form.cleaned_data.get('video'))

            return HttpResponseRedirect('../')
        return HttpResponse(services.get_error_str_with_form(add_form))

def delete_video(request):
    if request.method == 'POST':
        delete_form = DeleteVideoForm(request.POST)
        if delete_form.is_valid():
            video_id = delete_form.cleaned_data.get('video_id')
            VideoUnit.objects.filter(id=video_id).delete()
            return HttpResponseRedirect('../')
        
        return HttpResponse(services.get_error_str_with_form(delete_form))

    return HttpResponseRedirect('../')
