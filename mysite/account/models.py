from django.db import models, connection

class Account(models.Model):
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 500)

    class Meta:
        db_table = "accounts"