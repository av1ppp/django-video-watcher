from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import VideoUnit

def watch(request):
    v = request.GET.get('v', '')
    if not v:
        return HttpResponseNotFound('Not Found')

    video = VideoUnit.objects.get(id = int(v))
    if not video:
        return HttpResponseNotFound('Not Found')

    context = {'video': video}
    return render(request, 'watch/index.html', context)
    