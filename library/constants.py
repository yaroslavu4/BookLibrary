from enum import Enum
from datetime import timedelta


class LoanPeriod(Enum):
    STANDARD = 14
    EXTENDED = 21
    SHORT = 7

    @property
    def duration(self):
        return timedelta(days=int(self.value))
