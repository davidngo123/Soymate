from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category



def home(request):
    context = {
        'posts': Post.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')
