from datetime import date

class Booking:
    def __init__(self) -> None:
        self.bookdate = []
        
    # def in_dates(date1, date2):
        

    def book(self, begin, end):
        self.begin = date.fromisoformat(begin)
        self.end = date.fromisoformat(end)
        if self.begin >= self.end:
            return False
        else:
            for day_begin, day_end in self.bookdate:
                    if (day_begin <= self.begin < day_end) or (day_end >= self.end > day_begin):
                        return False
            # self.bookdate.clear()
            self.bookdate.append((self.begin, self.end))
            return True
            

booking = Booking()
print(booking.book('2008-11-10', '2008-11-05')) #F
print(booking.book('2008-11-11', '2008-11-13')) #T
print(booking.book('2008-11-12', '2008-11-12')) #F
print(booking.book('2008-11-12', '2008-11-14')) #F
print(booking.book('2008-11-10', '2008-11-11')) #T
print(booking.book('2008-11-12', '2008-11-13')) #T
print(booking.book('2008-11-13', '2008-11-13')) #F
print(booking.book('2008-11-13', '2008-11-14')) #T
print(booking.book('2008-05-08', '2008-05-18')) #T
print(booking.book('2008-05-09', '2008-05-10')) #F