from . import views
from django.urls import path
from visualization.views import get_json_data
urlpatterns = [
    path('get-filter-options/', views.filters, name='filters'),
    path("jsondata/", get_json_data, name="get_json_data")
]