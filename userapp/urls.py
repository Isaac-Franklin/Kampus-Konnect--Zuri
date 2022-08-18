from django.urls import path
from . import views

# importing views from views..py

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Signup/", views.SignUpView, name='Signup'),
    path("Login/", views.Login_page, name='Login'),
    path("WatchPage/", views.Watch, name='Watch-Page'),
    path("new_signup/", views.SignUpView, name='New-Signup-Page'),
    path("logout/", views.Logout_user, name='Logout'),
    path("validateid/", views.Validate_id, name='Validate'),
    path("validation2/", views.Validation2, name='Validation'),
    path("Video/", views.Video_Upload, name='Video'),
    path("Library/", views.Library, name='library'),
    path("Comment/", views.Comment, name='comment'),
    path("email/", views.emailPage, name='EmailPage'),

]
