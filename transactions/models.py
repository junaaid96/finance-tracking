from django.db import models
from users.models import UserProfile


class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.description}'
