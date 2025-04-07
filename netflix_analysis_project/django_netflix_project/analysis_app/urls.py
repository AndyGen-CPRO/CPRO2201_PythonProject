from django.urls import path
from .views import media_list, media_create, media_update, media_delete

urlpatterns = [
    path("", media_list, name="home"),
    path("media/", media_list, name="media_list"),
    path("create/", media_create, name="media_create"),
    path("update/<int:media_id>/", media_update, name="media_update"),
    path("delete/<int:media_id>/", media_delete, name="media_delete")
]