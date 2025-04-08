from django.contrib import admin
from .models import Tutors

# Register your models here.

class TutorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'expertise')
    search_fields = ('username', 'email', 'expertise', 'location')
    list_filter = ('is_active', 'expertise', 'location')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'location', 'profile_picture')}),
        ('Expertise', {'fields': ('expertise',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(Tutors, TutorsAdmin)

