from django.urls import path
from .views import *

urlpatterns = [
    path("", view_task, name="view_task"),
    path("create-task/", create_task, name="create_task"),
]
