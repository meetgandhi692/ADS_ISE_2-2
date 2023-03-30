from django.db import models

# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="user"