class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.double_bookings = []
        self.bookings = []

    def check_overlap(self, a1, a2, b1, b2):
        if max(a1, a2) < min(b1, b2):
            return True

    def find_overlap(self, a1, a2, b1, b2):
        return (max(a1, a2) , min(b1, b2))

    def book(self, startTime: int, endTime: int) -> bool:

        # check is overlap in double bookings ==> triple booking not allowed
        for booking in self.double_bookings:
            if self.check_overlap(startTime, booking[0], endTime, booking[1]):
                return False 

        # check bookings for double booking
        for booking in self.bookings:
            if self.check_overlap(startTime, booking[0], endTime, booking[1]):
                self.double_bookings.append(self.find_overlap(startTime, booking[0], endTime, booking[1]))
        
        # add it to bookings
        self.bookings.append((startTime, endTime))
                
        # print('double bookings: ', self.double_bookings)
        # print('bookings: ', self.bookings)
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)