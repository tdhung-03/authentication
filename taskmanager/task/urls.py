from django.urls import path
from .views import *

urlpatterns = [
    path("view_task", view_task, name="view_task"),
]
