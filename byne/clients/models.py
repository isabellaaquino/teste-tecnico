from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    loglist = models.JSONField(default=[])
    log = models.JSONField(default={})