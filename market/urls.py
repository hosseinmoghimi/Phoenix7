
from . import views,apis
from .apps import APP_NAME
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name=APP_NAME
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('customers/',views.CustomersView.as_view(),name="customers"), 
    path('search/',views.SearchView.as_view(),name="search"), 
    
   
 

]
