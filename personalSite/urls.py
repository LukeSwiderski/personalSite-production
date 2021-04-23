from django.urls import path
from personalSite import views

urlpatterns = [
   path("", views.index),
]