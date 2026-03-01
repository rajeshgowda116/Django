from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
    # placeholder urls for todos app; add patterns here later
]
