from django.db import models
from users.models import UserProfile


class SavingsGoal(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return f'{self.amount} - {self.deadline}'
