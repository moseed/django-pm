from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ProjecListViews.as_view(),name='Project_List'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_Create')

]