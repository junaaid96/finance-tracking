from django.db import models
from users.models import UserProfile

class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} - {self.type}'
