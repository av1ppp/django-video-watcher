from django.forms import widgets
# from .models import video
from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', help_text='Введите название видео')
    video = forms.FileField(label='Видео', help_text='Добавьте видео')
    tags = forms.CharField(label='Теги', help_text='Выберите теги')


class DeleteVideoForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())