from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import Post, Comment, User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('is_admin', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', )
    ordering = ('username', )
    filter_horizontal = ()


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)