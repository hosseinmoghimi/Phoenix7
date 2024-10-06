from .apps import APP_NAME
from . import views,apis
from django.urls import path
app_name=APP_NAME
urlpatterns = [
    path("",(views.HomeView.as_view()),name="home"),
    path("charts/",(views.ChartsView.as_view()),name="charts"),
    path("excel/",(views.ExcelView.as_view()),name="excel"),
    path("date_converter/",(views.DateConverterView.as_view()),name="date_converter"),
    path("read_excel_file/",(apis.ReadExcelFileApi.as_view()),name="read_excel_file"),
    

]
