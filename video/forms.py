from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', help_text='Введите название видео')
    # image = forms.ImageField(label='Изображение', help_text='Добавьте изображение для превью')
    video = forms.FileField(label='Видео', help_text='Добавьте видео')

class DeleteVideoForm(forms.Form):
    video_id = forms.CharField(widget=forms.HiddenInput())