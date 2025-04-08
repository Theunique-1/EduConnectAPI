from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'tutor', 'date_time', 'duration', 'booking_status')
    list_filter = ('booking_status', 'is_online', 'date_time', 'tutor')
    search_fields = ('student__username', 'tutor__username', 'location')
    ordering = ('-date_time',)
    fieldsets = (
        (None, {'fields': ('student', 'tutor', 'date_time', 'duration')}),
        ('Details', {'fields': ('is_online', 'location', 'booking_status')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Booking, BookingAdmin)
