from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='projects'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create_projects/', views.create_projects, name='create_projects'),
    path('edit_projects/<int:pk>', views.editOur_project.as_view(), name='edit_projects'),
    path('update_projects/<int:pk>', views.updateOur_project, name='update_projects'),
    path('delete_projects/<int:pk>', views.delete_projects, name='delete_projects'),
]
