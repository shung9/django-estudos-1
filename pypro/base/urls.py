from django.urls import path
#option 1
from .import views #1
#ou podes usar, da na mesma
from .o_nome_do_app.views import home #2

#no caso da option 1, olha urls.py app principal 
urlpatterns = [
  path('', views.home, name='home'),#1
  #path('', home, name='home'), #2
]
