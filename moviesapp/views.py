from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from . forms import MovieForm
# Create your views here.
def index(request):

      movie=movies.objects.all()
      context={

            'movie_list':movie
      }

      return render(request,"index.html",context)

def detail(request,movie_id):
      movie=movies.objects.get(id=movie_id)

      return render(request,"detail.html",{'movie':movie})
def add(request):
      if request.method=='POST':
            name=request.POST.get('name',)
            descr = request.POST.get('descr',)
            year = request.POST.get('year',)
            img = request.FILES['img']
            movie=movies(name=name,descr=descr,year=year,img=img)
            movie.save();
      return render(request,"add.html")

def update(request,id):
      movie=movies.objects.get(id=id)

      form=MovieForm(request.POST or None, request.FILES,instance=movie)
      if form.is_valid():
            form.save()
            return redirect('/')
      return render(request,"update.html",{'movie':movie,'form':form})



