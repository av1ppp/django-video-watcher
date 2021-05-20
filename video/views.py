from .forms import UploadVideoForm, DeleteVideoForm
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import VideoUnit, VideoTag
from . import services
import json

def home(request):
    return render(request, 'video/home.html')

def catalog(request):
    videos = VideoUnit.objects.all()
    for v in videos:
        v.delete_form = DeleteVideoForm(initial={'video_id': v.id})
        v.tags = list(v.videotag_set.all().values('name'))

    context = {'videos': videos}
    return render(request, 'video/catalog.html', context)

def watch_video(request):
    video_id = request.GET.get('id', '')
    if not video_id:
        return HttpResponseNotFound('Not Found')
    video_id = int(video_id)

    video = VideoUnit.objects.get(id=video_id)
    if not video:
        return HttpResponseNotFound('Not Found')
    
    context = {'video': video}
    return render(request, 'video/watch.html', context)

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            services.create_videounit(
                title=form.cleaned_data.get('title'),
                video=form.cleaned_data.get('video'),
                tags=json.loads(form.cleaned_data.get('tags')),
            )
            
            return HttpResponseRedirect('/catalog')
        return HttpResponse(services.get_errors_with_form(form))

    elif request.method == 'GET':
        context = {
            'upload_form': UploadVideoForm(),
        }
        return render(request, 'video/upload.html', context)

def delete_video(request):
    if request.method == 'POST':
        delete_form = DeleteVideoForm(request.POST)
        if delete_form.is_valid():
            video_id = delete_form.cleaned_data.get('video_id')
            VideoUnit.objects.filter(id=video_id).delete()
            return HttpResponseRedirect('/catalog')
        
        return HttpResponse(services.get_errors_with_form(delete_form))

    return HttpResponseRedirect('/catalog')

def get_tags(request):
    tags = VideoTag.objects.all()

    tags_dict = {'tags': [], 'count': 0}
    for tag in tags:
        tags_dict['tags'].append({
            'name': tag.name,
            'id': tag.id,
        })
        tags_dict['count'] += 1
    tags_json = json.dumps(tags_dict, indent=4, ensure_ascii=False)
        
    return HttpResponse(tags_json, content_type='application/json; charset=utf-8')

