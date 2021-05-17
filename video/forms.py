from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', help_text='Введите название видео')
    video = forms.FileField(label='Видео', help_text='Добавьте видео')

class DeleteVideoForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())