from django.urls import path
from .views import *

urlpatterns = [
    path("", view_task, name="view_task"),
    path("create-task/", create_task, name="create_task"),
    path("edit-task/<int:id>", edit_task, name="edit_task"),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
]
