from django.urls import path
from . import views
from .views import file_upload

urlpatterns = [
    path('' , views.index,name = 'index'),
    path('upload', views.file_upload),
    path('download/<str:filename>', views.download, name='download'),
]
