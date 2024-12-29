from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import (
    Book,
    Reader,
    Loan,
    Reservation,
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'author')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'created_at')
    search_fields = ('user__username',)


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'date_taken', 'date_due')
    list_filter = ('date_due',)
    search_fields = ('book__title', 'reader__user__username')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'reserved_at')
    list_filter = ('reserved_at',)
    search_fields = ('book__title', 'reader__user__username')

# @admin.register(PeriodicTask)
# class PeriodicTaskAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(IntervalSchedule)
# class PIntervalScheduleAdmin(admin.ModelAdmin):
#     pass
