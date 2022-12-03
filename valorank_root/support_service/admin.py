from django.contrib import admin
from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'status', 'mailbox', 'creation_time')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email', 'status', 'mailbox')
    list_filter = ('status', 'mailbox')
    list_editable = ('status', 'mailbox')
    list_per_page = 10
    list_max_show_all = 100


admin.site.register(Request, RequestAdmin)
