from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ProjecListViews.as_view(),name='Project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create'),
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='Project_delete'),
    path('task/create', views.TaskCreatView.as_view(), name='Task_create'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='Task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='Task_delete')

]