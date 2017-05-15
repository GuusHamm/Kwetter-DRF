from django.contrib import admin


# Register your models here.
from kweet.models import Kweet


class KweetAdmin(admin.ModelAdmin):
    list_display = ('message', 'account', 'timestamp')
    list_filter = ('account__username', 'timestamp')
    search_fields = ('account__username', 'message')


admin.site.register(Kweet, KweetAdmin)
