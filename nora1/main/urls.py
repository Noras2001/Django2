from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('new3', views.new3, name='page3'),
    path('new4', views.new4, name='page4'),
]

