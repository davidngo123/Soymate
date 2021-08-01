from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    """
    List View for the main page where all posts are shown
    you can filter and sort the posts
    """
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        order = self.request.GET.get('orderby', '-date_posted')
        filter_val = self.request.GET.get('filter', '')
        if(filter_val == ''):
            new_context = Post.objects.all().order_by(order)
        else:
            new_context = Post.objects.filter(title__contains=filter_val,).order_by(order)

        return new_context

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'Dinner')
        context['orderby'] = self.request.GET.get('orderby', '-date_posted')
        return context

class UserPostListView(ListView):
    """
    Shows all the posts from a specifc user
    """
    model = Post
    template_name = 'home/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        order = self.request.GET.get('orderby', '-date_posted')
        filter_val = self.request.GET.get('filter', '')
        if(filter_val == ''):
            new_context = Post.objects.all().order_by(order)
        else:
            new_context = Post.objects.filter(title__contains=filter_val,).order_by(order)

        return new_context.filter(author=user)

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'Dinner')
        context['orderby'] = self.request.GET.get('orderby', '-date_posted')
        return context

class FeedPostListView(LoginRequiredMixin, ListView):
    """
    Shows the posts from the current users followers

    """
    model = Post
    template_name = 'home/feed.html' 
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        my_profile = Profile.objects.get(user=self.request.user)
        followers = my_profile.following.all()
        order = self.request.GET.get('orderby', '-date_posted')
        filter_val = self.request.GET.get('filter', '')
        if(filter_val == ''):
            new_context = Post.objects.all().order_by(order)
        else:
            new_context = Post.objects.filter(title__contains=filter_val,).order_by(order)

        return new_context.filter(author__in=followers)

    def get_context_data(self, **kwargs):
        context = super(FeedPostListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'Dinner')
        context['orderby'] = self.request.GET.get('orderby', '-date_posted')
        return context

class FollowingListView(LoginRequiredMixin, ListView):
    """
    View of all the users registered that you follow
    """
    model = Profile
    template_name = 'home/following.html'
    context_object_name = 'posts'
    paginate_by = 8



    def get_queryset(self):
        my_profile = Profile.objects.get(user=self.request.user)
        followers = my_profile.following.all()
        order = self.request.GET.get('orderby', '-user')
        new_context = Profile.objects.all().order_by(order).exclude(user=self.request.user)
        return new_context.filter(user__in=followers)

    def get_context_data(self, **kwargs):
        context = super(FollowingListView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', '-user')
        my_profile = Profile.objects.get(user=self.request.user)
        followers = my_profile.following.all()
        context['followers'] = followers
        return context


class All_User_ListView(LoginRequiredMixin, ListView):
    """
    View of all the users registered
    """
    model = Profile
    template_name = 'home/all_users.html'
    context_object_name = 'posts'
    paginate_by = 8



    def get_queryset(self):
        order = self.request.GET.get('orderby', '-user')
        new_context = Profile.objects.all().order_by(order).exclude(user=self.request.user)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(All_User_ListView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', '-user')
        my_profile = Profile.objects.get(user=self.request.user)
        followers = my_profile.following.all()
        context['followers'] = followers
        return context

class PostDetailView(DetailView):
    """
    shows the detailed view of a recipe 

    """
    model = Post
    template_name = 'home/post_detail.html' 





class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'cooktime', 'ingredients', 'instructions', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'cooktime', 'ingredients', 'instructions', 'image']

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

def follow_unfollow_profile(request):
    if request.method=="POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)
        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('soymate-home')