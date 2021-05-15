from django import forms

class UploadVideoForm(forms.Form):
    name = forms.CharField(label='Название', help_text='Введите название видео')
    image = forms.ImageField(label='Изображение', help_text='Добавьте изображение для превью')
    videofile = forms.FileField(label='Видео', help_text='Добавьте видео')

class DeleteVideoForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())