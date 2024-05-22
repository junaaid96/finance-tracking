from django.db import models
from users.models import UserProfile
from categories.models import Category


class Expense(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.amount} - {self.category}'
