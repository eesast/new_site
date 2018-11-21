from django.urls import path

from . import views

urlpatterns = [
    path('dir/', views.directory, name='dir'),
    path('subdir/<str:subdir>',views.subdirectory,name='subdir'),
]