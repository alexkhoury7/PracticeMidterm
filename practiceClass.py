'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play:


    def __init__(self, idnum, name, seatnum, date, stat=True):

        self.__idnum = idnum
        self.__name = name
        self.__seatnum = seatnum
        self.__date = date
        self.__stat = stat

    def get_idnum(self):
        return self.__idnum

    def get_name(self):
        return self.__name

    def get_seatnum(self):
        return self.__seatnum

    def get_date(self):
        return self.__date

    def set_stat(self):
        return self.stat

    def seats_left(self):
        self.__seatnum -=1

    def set_status(self):
        self.__stat = False

class Booking:
    def __init__(self, cust_name, seat_number):
        self.cust_name = cust_name
        self.seat_number = seat_number

    def get_cust_name(self):
        return self.cust_name

    def get_seat_number(self):
        return self.seat_number
