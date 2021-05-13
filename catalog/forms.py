from django import forms

class AddVideoForm(forms.Form):
    name = forms.CharField(label='Название', help_text='Введите название видео')
    image = forms.ImageField(label='Изображение', help_text='Добавьте изображение для превью')

class DeleteVideoForm(forms.Form):
    video_id = forms.IntegerField(widget=forms.HiddenInput())