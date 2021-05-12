from .forms import VideoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Snapshot, Video


def index(request):
    videos = Video.objects.all()
    for v in videos:
        if v.snapshot:
            v.snapshot_url = v.snapshot.image.url
        else:
            v.snapshot_url = 'default.jpg'

    context = {'videos': videos}

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            image = form.cleaned_data.get('image')
            obj = Video.objects.create(
                name = name,
                snapshot = Snapshot.objects.create(image = image)
            )
            obj.save()
        context['form'] = form
    else:
        context['form'] = VideoForm()

    return render(request, 'catalog/index.html', context)
