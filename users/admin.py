from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import Users
from .forms import SignupForm, ChangeDetails


class UsersAdmin(UserAdmin):
    list_display = ['email', 'active']
    list_display_links = ['email']
    list_filter = ['active']
    list_editable = ['active']

    class Meta:
        add_form = SignupForm
        form = ChangeDetails

    fieldsets = (
        ('Create new user', {'fields': ['email', 'password'] }),
        ('Permissions', {'fields': ['active']})
    )

    add_fieldsets = (
        ('Edit details', {
            'classes': ['wide'],
            'fields': ['email', 'password', 'confirm password']
        })
    )

    filter_horizontal = []
    search_fields = ('email',)
    ordering = ('email',)

admin.site.unregister(Group)
admin.site.register(Users, UsersAdmin)