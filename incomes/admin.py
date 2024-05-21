from django.contrib import admin
from .models import Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'date', 'description')
    list_filter = ('user', 'category', 'date')
    search_fields = ('user', 'category', 'date')


admin.site.register(Income, IncomeAdmin)
