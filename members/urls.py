from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, \
    CreateProfilePageView
from django.contrib.auth import  views as auth_views
from . import views


urlpatterns = [
    #path('',views.home,name="home"),
    path('registration/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_sucess',views.password_sucess,name="password_sucess"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view( ), name="showprofile"),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name="editprofile"),
    path('createprofile', CreateProfilePageView.as_view(), name="createprofile"),

]
