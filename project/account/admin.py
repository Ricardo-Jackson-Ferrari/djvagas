from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from rolepermissions.admin import RolePermissionsUserAdminMixin

from project.account.forms import UserSignupForm
from project.account.models import Contact, ProfileCandidate, User

admin.site.register(ProfileCandidate)
admin.site.register(Contact)


@admin.register(User)
class UserAdmin(RolePermissionsUserAdminMixin, DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'email', 'password', 'image')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'created_at')}),
    )

    readonly_fields = ('created_at',)

    add_form = UserSignupForm

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'first_name',
                    'email',
                ),
            },
        ),
    )
    list_display = (
        'email',
        'first_name',
        'created_at',
        'is_staff',
    )
    list_filter = (
        'groups',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    search_fields = ('first_name', 'email')
    ordering = ('created_at',)
