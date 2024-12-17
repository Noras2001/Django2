from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list, name='news_list'),  # Список новостей
    path('<int:pk>/', views.news_detail, name='news_detail'),  # Полная информация о новости
]