from django.urls import path
from .views import TransactionListCreate

urlpatterns = [
    path(
        "upload/",
        TransactionListCreate,
    )
]
