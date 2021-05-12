from django import forms

class VideoForm(forms.Form):
    name = forms.CharField(label='Название', help_text='Введите название видео')
    snapshot = forms.ImageField(label='Изображение', help_text='Добавьте изображение для превью')