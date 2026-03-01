from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
     path('task_task/<int:pk>/',views.task_task,name='task_task'),
     path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
     
    # placeholder urls for todos app; add patterns here later
]
