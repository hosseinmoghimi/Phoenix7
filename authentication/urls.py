
from . import views,apis
from .apps import APP_NAME
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name=APP_NAME
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name="profile"),
    path('change-password/',views.ChangePasswordView.as_view(),name="change_password"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"), 
    path('register/',views.HomeView.as_view(),name="register"), 
   
 

]
