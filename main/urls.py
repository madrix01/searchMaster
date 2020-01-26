from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('tags/', views.TagView),
    path('search/', views.SearchView),
    
] 