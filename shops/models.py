from django.db import models


class Shop(models.Model):
    teste = models.FileField(upload_to="")
