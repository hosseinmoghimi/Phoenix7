
from . import views,apis
from .apps import APP_NAME
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name=APP_NAME
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('login/',views.HomeView.as_view(),name="login"),
    path('logout/',views.HomeView.as_view(),name="logout"), 
    path('register/',views.HomeView.as_view(),name="register"), 
   
 

]
