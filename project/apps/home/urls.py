from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views  # --_> Importamos views por una importacion relativa

urlpatterns = [path("", views.index, name="index")]

# views.index --> Funcion que manejara la vista
# name="index" --> nombre que se la dara para luego referenciarlka en las plantillas

urlpatterns += staticfiles_urlpatterns()
