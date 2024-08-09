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
    path("accounting-documents/",login_required(views.AccountingDocumentsView.as_view()),name="accounting_documents"),
    path("basic-accounts/",login_required(views.BasicAccountsView.as_view()),name="basic_accounts"),
    path("balance/",login_required(views.BalanceView.as_view()),name="balance"),
    path("accounting-document/<int:pk>/",login_required(views.AccountingDocumentView.as_view()),name="accountingdocument"),
    path("accounting-document-line/<int:pk>/",login_required(views.AccountingDocumentLineView.as_view()),name="accountingdocumentline"),
    path("account/<int:pk>/",login_required(views.AccountView.as_view()),name="account"),
    path("add_account/",login_required(apis.AddAccountApi.as_view()),name="add_account"),
    path("tree-chart/",login_required(views.TreeChartView.as_view()),name="tree_chart"),
    path("add-document/",login_required(views.AddEventView.as_view()),name="add_event"),
    path("add-event/",login_required(views.AddDocumentView.as_view()),name="add_document"),
    path("search/",login_required(views.SearchView.as_view()),name="search"),
]
