from .apps import APP_NAME
from . import views,apis
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name=APP_NAME
urlpatterns = [
    path("",login_required(views.IndexView.as_view()),name="home"),
    path("accounts/",login_required(views.AccountsView.as_view()),name="accounts"),
    path("accountgroups/",login_required(views.AccountGroupsView.as_view()),name="account_groups"),
    path("accounts/<int:sv>/",login_required(views.AccountsView.as_view()),name="accounts_simple_view"),
    path("basic_account/<int:pk>/",login_required(views.BasicAccountView.as_view()),name="basicaccount"),
    path("moein_account/<int:pk>/",login_required(views.MoeinAccountView.as_view()),name="moeinaccount"),
    path("account_group/<int:pk>/",login_required(views.AccountGroupView.as_view()),name="accountgroup"),
    path("account/<int:pk>/",login_required(views.AccountView.as_view()),name="account"),
    path("add_account/",login_required(apis.AddAccountApi.as_view()),name="add_account"),
    path("search/",login_required(views.SearchView.as_view()),name="search"),
]
