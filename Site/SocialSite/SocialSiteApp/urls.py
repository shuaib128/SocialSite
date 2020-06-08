from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.contrib.auth import views as auth_views
from .models import Profile

urlpatterns = [
    path('', views.regester, name="regester"),
    path('home', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<str:username>/', UserPostListView.as_view(), name='users'),
    path('home/post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('explore', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('settings', views.settings, name='settings'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]