from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('entry/', views.entry, name='entry'),
    path('report/', views.report, name='report'),
]
