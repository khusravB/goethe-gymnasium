from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news-list', views.news_list, name='news-list'),
]
