from django.contrib import admin

# Register your models here.
from kwetter.models import Account, Kweet


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'firstname', 'lastname')
    list_filter = ('username',)


class KweetAdmin(admin.ModelAdmin):
    list_display = ('message', 'account', 'timestamp')
    list_filter = ('account__username', 'timestamp')
    search_fields = ('account__username', 'message')


admin.site.register(Account, AccountAdmin)
admin.site.register(Kweet, KweetAdmin)
