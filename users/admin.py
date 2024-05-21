from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    # def email(self, obj):
    #     return obj.user.email

    list_display = ['full_name', 'phone_number',
                    'address', 'available_balance']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']


admin.site.register(UserProfile, UserProfileAdmin)
