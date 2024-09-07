from .apps import APP_NAME
from . import views,apis
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name=APP_NAME
urlpatterns = [
    path("",login_required(views.IndexView.as_view()),name="home"),
    path("accounts/",login_required(views.AccountsView.as_view()),name="accounts"),
    path("account-group/<int:pk>/",login_required(views.AccountGroupView.as_view()),name="accountgroup"),
    path("account-groups/",login_required(views.AccountGroupsView.as_view()),name="account_groups"),
    path("accounts/<int:sv>/",login_required(views.AccountsView.as_view()),name="accounts_simple_view"),
    path("basic-account/<int:pk>/",login_required(views.BasicAccountView.as_view()),name="basicaccount"),
    path("event/<int:pk>/",login_required(views.EventView.as_view()),name="event"),
    path("events/",login_required(views.EventsView.as_view()),name="events"),
    path("moein-account/<int:pk>/",login_required(views.MoeinAccountView.as_view()),name="moeinaccount"),
    path("moein-accounts/",login_required(views.MoeinAccountsView.as_view()),name="moein_accounts"),
    path("accounting-documents/",login_required(views.AccountingDocumentsView.as_view()),name="accounting_documents"),
    path("basic-accounts/",login_required(views.BasicAccountsView.as_view()),name="basic_accounts"),
    path("balance/",login_required(views.BalanceView.as_view()),name="balance"),
    path("accounting-document/<int:pk>/",login_required(views.AccountingDocumentView.as_view()),name="accountingdocument"),
    path("accounting-document-line/<int:pk>/",login_required(views.AccountingDocumentLineView.as_view()),name="accountingdocumentline"),
    path("add=accounting-document-line/",login_required(apis.AddAccountingDocumentLineApi.as_view()),name="add_accounting_document_line"),
    path("tafsili-account/<int:pk>/",login_required(views.TafsiliAccountView.as_view()),name="tafsiliaccount"),
    path("account/<int:pk>/",login_required(views.AccountView.as_view()),name="account"),
    path("account/code/<code>/",login_required(views.AccountView.as_view()),name="account_by_code"),
    path("add-account/",login_required(apis.AddAccountApi.as_view()),name="add_account"),
    path("tree-chart/",login_required(views.TreeChartView.as_view()),name="tree_chart"),
    path("tree-list/",login_required(views.TreeListView.as_view()),name="tree_list"),
    path("account-group-tree-chart/<int:pk>/",login_required(views.TreeChartView.as_view()),name="account_group_tree_chart"),
    path("add-event/",login_required(views.AddEventView.as_view()),name="add_event"),
    path("add-accounting-document/",login_required(views.AddAccountingDocumentView.as_view()),name="add_accounting_document"),
    path("add-moein-account/",login_required(apis.AddMoeinAccountApi.as_view()),name="add_moein_account"),
    path("add-tafsili-account/",login_required(apis.AddTafsiliAccountApi.as_view()),name="add_tafsili_account"),
    path("add-basic-account/",login_required(apis.AddBasicAccountApi.as_view()),name="add_basic_account"),
    path("edit-document/",login_required(views.EditDocumentView.as_view()),name="edit_document"),
    path("search/",login_required(views.SearchView.as_view()),name="search"),
    path("init_all_accounts/",login_required(apis.InitALLAccountsApi.as_view()),name="init_all_accounts"),
    path("delete_all_accounts/",login_required(apis.DeleteALLAccountsApi.as_view()),name="delete_all_accounts"),
    path("select_account_group/",login_required(apis.SelectAccountGroupApi.as_view()),name="select_account_group"),
    path("selection/",login_required(views.SelectionView.as_view()),name="selection"),
    path("select-account/",login_required(apis.SelectAccountApi.as_view()),name="select_account"),
    path("settings/",login_required(views.SettingsView.as_view()),name="settings"),
]
