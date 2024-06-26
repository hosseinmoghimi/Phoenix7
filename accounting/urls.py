from .apps import APP_NAME
from . import views,apis
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name=APP_NAME
urlpatterns = [
    path("",login_required(views.IndexView.as_view()),name="home"),
    path("accounts/",login_required(views.AccountsView.as_view()),name="accounts"),
    path("accounts/<int:sv>/",login_required(views.AccountsView.as_view()),name="accounts_simple_view"),
    path("account/<int:pk>/",login_required(views.AccountView.as_view()),name="account"),
    path("search/",login_required(views.SearchView.as_view()),name="search"),
]
