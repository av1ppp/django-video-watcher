from .forms import VideoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Video


def index(request):
    if request.method == 'POST':
        v = Video()
        v.name = request.POST.get('name')
        v.save()
        return HttpResponseRedirect(request.path)
    else:
        videos = Video.objects.all()
        for v in videos:
            v.snapshot_uri = v.get_snapshot_uri()

        videoform = VideoForm()
        ctx = {
            'form': videoform,
            'videos': videos
        }
        return render(request, 'catalog/index.html', ctx)
