from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Position, EmployeeMailbox


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'phone',
        'discord',
        'is_employee',
        'position',
        'mailbox',
        'get_avatar'
    )
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email', 'phone', 'mailbox')
    list_filter = ('is_employee', 'position', 'mailbox')
    list_per_page = 10
    list_max_show_all = 100

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50px"')
        else:
            return 'Нет аватара'

    get_avatar.short_description = 'Аватар'


admin.site.register(User, UserAdmin)
admin.site.register(Position)
admin.site.register(EmployeeMailbox)