from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category



def home(request):
    category = request.GET.get('category')
    if category == None:
        post = Post.objects.all()
    else:
        post = Post.objects.filter(category__name=category)
    
    
    context = {
        'posts': post,
        'categories': Category.objects.all()
    }

    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')
