from .apps import APP_NAME
from . import views,apis
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("",login_required(views.IndexView.as_view()),name="home"),
    path("search/",login_required(views.SearchView.as_view()),name="search"),
]
