
from . import views,apis
from .apps import APP_NAME
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name=APP_NAME
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('settings/',views.SearchView.as_view(),name="settings"), 
    path('search/',views.SearchView.as_view(),name="search"), 
    path('page/<int:pk>/',views.PageView.as_view(),name="page"),
    path('pages/',views.PagesView.as_view(),name="pages"),
   
 

]
