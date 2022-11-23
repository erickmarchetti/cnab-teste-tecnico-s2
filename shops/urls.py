from django.urls import path
from .views import shopListCreate

urlpatterns = [
    path(
        "upload/",
        shopListCreate,
    )
]
