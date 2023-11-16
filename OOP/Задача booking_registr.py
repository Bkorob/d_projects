from datetime import date


# BEGIN (write your solution here)
class Booking:
    def __init__(self):
        self.bookdate = []

    def book(self, date_inn, date_out):
        self.book_inn = date.fromisoformat(date_inn)
        self.book_out = date.fromisoformat(date_out)
        if self.book_inn >= self.book_out:
            return False
        else:
            for day_begin, day_end in self.bookdate:
                if (day_begin >= self.book_inn < day_end) or (day_begin < self.book_out <= day_end):
                    return False
                self.bookdate.append((self.book_inn, self.book_out))
                return True


booking = Booking()
print(booking.book('2008-11-11', '2008-11-13'))
print(booking.book('2008-11-13', '2008-11-14'))
booking.book('2008-11-10', '2008-11-12')  # False
booking.book('2008-11-12', '2008-11-14')  # False
booking.book('2008-11-10', '2008-11-11')  # True
booking.book('2008-11-13', '2008-11-14')  # True
