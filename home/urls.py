from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', PostListView.as_view(), name = 'soymate-home'),
    path('users/', All_User_ListView.as_view(), name = 'soymate-users'),
    path('feed/', FeedPostListView.as_view(), name = 'soymate-feed'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name = 'soymate-about'),
    path('following/', FollowingListView.as_view(), name = 'soymate-following'),
    path('switch_follow/', views.follow_unfollow_profile, name ='follow'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)