from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Book name")
    author = models.CharField(max_length=100, verbose_name="Author")  # Add a Author modl afterall
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Available")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date added")

    def __str__(self):
        return f"{self.title} ({self.author})"


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reader", verbose_name="User")
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")

    def __str__(self):
        return f"{self.user.username} ({self.phone_number or 'Without number'})"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans", verbose_name="Book")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name="loans", verbose_name="Reader")
    date_taken = models.DateTimeField(auto_now_add=True, verbose_name="Date taken")
    date_due = models.DateTimeField(verbose_name="Date to be returned")
    date_returned = models.DateTimeField(blank=True, null=True, verbose_name="Date Returned")

    def __str__(self):
        return f"{self.book.title} -> {self.reader.user.username}"


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reservations")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name="reservations")
    reserved_at = models.DateTimeField(auto_now_add=True)
    date_available = models.DateTimeField(null=True)
