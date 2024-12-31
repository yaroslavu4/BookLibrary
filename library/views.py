from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.timezone import now
from django.views.generic import (
    ListView,
    DetailView,
)

from .forms import CustomUserCreationForm
from .models import (
    Book,
    Reservation,
    Reader,
    Loan,
)
from .constants import LoanPeriod


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def handle_no_permission(self):
        response = super().handle_no_permission()
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Please log in or register to view this book.')
        return response

    def dispatch(self, request, *args, **kwargs):
        # s there a reader for current user
        try:
            self.reader = Reader.objects.get(user=request.user)
        except Reader.DoesNotExist:
            messages.error(request, 'Please log in or register to view this book.')
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book = self.object
        user = self.request.user

        # Reservation for the book?
        already_requested = book.reservations.filter(reader=self.reader).exists()
        context['already_requested'] = already_requested

        # Loan for the book?
        active_loan = Loan.objects.filter(
            book=self.object,
            reader=self.reader,
            date_returned__isnull=True
        ).exists()

        # Book status
        if active_loan:
            context['book_status'] = 'In Use'
        elif book.is_active:
            context['book_status'] = 'Available'
        else:
            context['book_status'] = 'Not Available'

        context['active_loan'] = active_loan
        return context


def request_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    # get current reader
    user = request.user
    reader = get_object_or_404(Reader, user=user)

    # if book is occupied --> cretae a reservation
    if not book.is_active:
        loan = book.loans.first()
        date_available = loan.date_due if loan else timezone.now() + LoanPeriod.STANDARD.duration

        # Check for existing reservations for any reader
        existing_reservations = Reservation.objects.filter(book=book).order_by('date_available')
        if existing_reservations.exists():
            # Update the date_available to follow the last reservation in the queue
            last_reservation = existing_reservations.last()
            date_available = last_reservation.date_available + LoanPeriod.STANDARD.duration

        # check for existing reservation for current reader
        existing_reservation = Reservation.objects.filter(book=book, reader=reader).exists()
        if not existing_reservation:

            # create new reservation
            reservation = Reservation.objects.create(
                book=book,
                reader=reader,
                reserved_at=timezone.now(),
                date_available=date_available
            )
            messages.success(request, "This book is requested successfully!")
        else:
            messages.warning(request, "You have already requested this book.")
        return redirect('book-detail', pk=book.pk)

    # if book available
    return redirect('book-detail', pk=book.pk)


def add_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if book.is_active:

        # get current reader
        user = request.user
        reader = get_object_or_404(Reader, user=user)

        # check for existing loan
        active_loan = Loan.objects.filter(
            book=book,
            reader=user.reader,
            date_returned__isnull=True  # check that book is not returned yet
        ).exists()
        if not active_loan:

            # create Loan
            Loan.objects.create(
                book=book,
                reader=reader,
                date_taken=now(),
                date_due=now() + LoanPeriod.STANDARD.duration,  # default loan period set to 14 days
                date_returned=None
            )
            messages.success(request, "This book was successfully added! You now have 14 days to return it")

            # mark book as not available
            book.is_active = False
            book.save()
        else:
            messages.warning(request, "You have already added this book.")
        return redirect('book-detail', pk=book.pk)

    # if the book is not available, redirect to the detail page
    return redirect('book-detail', pk=book.pk)


class ReaderListView(ListView):
    model = Reader
    template_name = 'readers/reader_list.html'
    context_object_name = 'readers'


class ReaderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Reader
    template_name = 'readers/reader_detail.html'
    context_object_name = 'reader'

    def test_func(self):
        # Allow access only to superuser or current user
        reader = self.get_object()
        return self.request.user.is_superuser or reader.user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get all loans for current user
        reader = self.get_object()
        loans = Loan.objects.filter(reader=reader, date_returned__isnull=True)
        reservations = reader.reservations.all()
        context['loans'] = loans
        context['reservations'] = reservations
        return context


class MyProfileView(LoginRequiredMixin, DetailView):
    model = Reader
    template_name = 'readers/my_profile.html'
    context_object_name = 'reader'

    def get_object(self, queryset=None):
        # return current user
        return self.request.user.reader

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get all loans for current user
        reader = self.get_object()
        loans = Loan.objects.filter(reader=reader, date_returned__isnull=True)
        reservations = reader.reservations.all()

        context['loans'] = loans
        context['reservations'] = reservations
        return context


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been successfully created! You can now log in.')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
