from django.urls import path
from . import views


urlpatterns = [
    path('', views.EntriesList.as_view(), name='entries-list'),
]
