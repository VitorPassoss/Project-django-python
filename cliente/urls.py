from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("lista",views.lista),
    path("lista/<int:id>/",views.detalhe)
]
