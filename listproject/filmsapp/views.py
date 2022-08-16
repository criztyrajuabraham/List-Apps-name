

from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import Form

# Create your views here.
from .models import Movie

def index(request):
    movie=Movie.objects.all()
    context={
        "list":movie
    }
    return render(request,'lists.html',context)
def detail(request,film_id):
    film=Movie.objects.get(id=film_id)
    return render(request,'details.html',{'films':film})

def addfilm(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()

    return render(request,'add.html')

def updates(request,id):
    movie=Movie.objects.get(id=id)
    forms=Form(request.POST or None, request.FILES,instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'updates.html',{'forms':forms ,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')











