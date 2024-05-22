from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'description', 'date')
    list_filter = ('type', 'date')
    search_fields = ('user__user__username', 'type', 'description')
    ordering = ('-date',)


admin.site.register(Transaction, TransactionAdmin)
