class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for x in self.calendar:
            if (start < x[0] and end > x[0]) or (start == x[0]) or (start > x[0] and start < x[1]):
                return False
        self.calendar.append([start, end])
        return True