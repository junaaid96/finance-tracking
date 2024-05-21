from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    def current_balance(self, obj):
        return obj.user.available_balance

    list_display = ('user', 'amount', 'type', 'date', 'current_balance')
    list_filter = ('user', 'type', 'date')
    search_fields = ('user', 'type', 'date')


admin.site.register(Transaction, TransactionAdmin)
