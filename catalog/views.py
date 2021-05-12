from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Video


def index(request):
    videos = Video.objects.all()
    for v in videos:
        v.snapshot_uri = v.get_snapshot_uri()
    return render(request, 'catalog/index.html', {'videos': videos})


def create(request):
    if request.method == 'POST':
        v = Video()
        v.name = request.POST.get('name')
        v.save()
    return HttpResponseRedirect('/')