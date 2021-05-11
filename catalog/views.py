from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Person


def index(request):
    people = Person.objects.all()
    print(people.count())
    return render(request, 'catalog/index.html', {'people': people})

def create(request):
    print('this')
    if request.method == 'POST':
        tom = Person()
        tom.name = request.POST.get('name')
        tom.age = request.POST.get('age')
        tom.save()
        print('thiiis')
        print(tom)
    return HttpResponseRedirect('/')
