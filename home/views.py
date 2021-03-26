from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {'author': 'tester',
     'title': 'recipe 1',
    },
    {'author': 'yo',
     'title': 'recipe 2',
    },
    {'author': 'yo',
     'title': 'recipe 2',
    },
    {'author': 'yo',
     'title': 'recipe 2',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')
