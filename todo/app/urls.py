from django.urls import path
from .views import *

urlpatterns= [
    # path('add/', add, name = 'add'),
    path('', view_tasks, name = 'view_task'),
    path('delete/<int:taskid>', delete_task, name = 'delete'),
    path('update/<int:taskid>', update, name = 'update'),
    
]