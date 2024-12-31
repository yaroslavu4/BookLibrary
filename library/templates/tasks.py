from celery import shared_task
from datetime import datetime

from library.models import Loan, Reservation
from library.constants import LoanPeriod


@shared_task
def check_due_dates_and_assign_books():
    now = datetime.now()

    # Search for overdue loans
    overdue_loans = Loan.objects.filter(date_due__lte=now, date_returned__isnull=True)

    for loan in overdue_loans:

        # Mark the current loan as returned
        loan.date_returned = now
        loan.save()

        # Is there a reservation for this book?
        reservations = Reservation.objects.filter(book=loan.book).order_by('reserved_at')
        if reservations.exists():
            # Taking 1 record in reservations
            reservation = reservations.first()

            # Assign a book to 1 reader from waitlist
            Loan.objects.create(
                book=loan.book,
                reader=reservation.reader,
                date_due=now + LoanPeriod.STANDARD.duration,  # 2 weeks to return
            )

            # Delete reservation
            reservation.delete()

        else:
            # 3. If no reservations, mark book as available
            loan.book.is_active = True
            loan.book.save()
