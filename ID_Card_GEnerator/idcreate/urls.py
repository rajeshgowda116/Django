from django.urls import path
from . import views

urlpatterns = [
   path('idhistory/', views.idhistory, name='idhistory'),
   path('idgenerate/', views.idgenerate, name='idgenerate'),
   

]
