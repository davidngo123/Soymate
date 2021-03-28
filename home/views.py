from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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


class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    #ordering = ['-date_posted]
    
    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'cooktime', 'ingredients', 'instructions', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'cooktime', 'ingredients', 'instructions', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'home/about.html')
