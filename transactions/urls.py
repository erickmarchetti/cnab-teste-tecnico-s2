from django.urls import path
from .views import transactionListCreate

urlpatterns = [
    path(
        "upload/",
        transactionListCreate,
    )
]
