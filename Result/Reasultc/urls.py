from django.urls import path
from . import views
urlpatterns = [
  path('add_marks/',views.add_marks,name='add_marks'),
  path('result_came/',views.result_came,name='result_came'),

]
