from django.contrib import admin
from .models import SavingsGoal


class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount', 'current_amount', 'deadline')
    list_filter = ('user', 'deadline')
    search_fields = ('user', 'deadline')


admin.site.register(SavingsGoal, SavingsGoalAdmin)
