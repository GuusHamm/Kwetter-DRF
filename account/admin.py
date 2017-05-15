from django.contrib import admin

# Register your models here.
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'firstname', 'lastname')
    list_filter = ('username',)

admin.site.register(Account, AccountAdmin)
