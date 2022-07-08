
from django.urls import path
from . import views
from .views import (CreateThread,UploadfileMessage,Checkgroup,
ListThreadAPIView,ActionThread,CountThread,MediathreadAPI,FilethreadAPI)

urlpatterns = [
    path('conversations/<int:id>',ActionThread.as_view()),
    path('thread/list', ListThreadAPIView.as_view()),
    path('thread/new', CreateThread.as_view()),
    path('thread/check', Checkgroup.as_view()),
    path('file/<int:id>', UploadfileMessage.as_view()),
    path('thread/count', CountThread.as_view()),
    path('thread/media',  MediathreadAPI.as_view()),
    path('thread/file',  FilethreadAPI.as_view()),
]