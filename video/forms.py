from django.forms import widgets
from video.models import VideoFile, VideoTag, VideoUnit
from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', help_text='Введите название видео')
    video = forms.FileField(label='Видео', help_text='Добавьте видео')

    tags = forms.CharField(label='Теги', help_text='Выберите теги')

    def __init__(self, *args, **kwargs):
        super(UploadVideoForm, self).__init__(*args, **kwargs)
        
        tags = []
        for tag in VideoTag.objects.all().values('name'):
            tags.append(tag['name'])
        
        self.fields['tags'].widget.attrs['tags'] = '; '.join(tags)

class DeleteVideoForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())