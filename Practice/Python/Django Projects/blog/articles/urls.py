from django.urls import path
from . import views

app_name = articles

urlpatterns = [
    path('', views.home, name='home'),
    path('article_list/', views.article_list, name='article_list'),
    path('<str:title>/', views.article_page, name='article_page'),
]