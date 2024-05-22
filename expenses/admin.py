from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'category', 'date', 'description')
    list_filter = ('user', 'category', 'date')
    search_fields = ('user', 'category', 'date')


admin.site.register(Expense, ExpenseAdmin)
