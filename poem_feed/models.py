from django.db import models
from django.utils.timezone import now


class feed(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    msg=models.TextField(max_length=600)
    date_created = models.DateTimeField(default=now, editable=False)


# Create your models here.
