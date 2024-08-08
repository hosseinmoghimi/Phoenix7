from .apps import APP_NAME
from django.urls import path
from . import views,apis
from django.contrib.auth.decorators import login_required
app_name=APP_NAME
urlpatterns = [
    path("",login_required(views.IndexView.as_view()),name="home"),
    path("process/<int:pk>/",login_required(views.ProcessView.as_view()),name="process"),
    path("processes/",login_required(views.ProcessesView.as_view()),name="processes"),
]
