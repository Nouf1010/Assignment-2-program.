class Ticket:
    '''Class to represent a ticket'''
    # Constructor
    def __init__(self, ticketID, ticketType, price):
        self.__ticketID = ticketID
        self.__ticketType = ticketType
        self.__price = price

    # Calculating ticket price based on visitor category
    def calculate_price(self, age):
        # Default ticket price for adults
        ticket_price = 63

        if self.__ticketType.lower() == "adult":
            if 18 <= age <= 60:
                # Applying VAT which is 5%
                ticket_price *= 1.05
                return ticket_price
            else:
                return 0  # Free ticket for children, teachers/students, and seniors
        elif self.__ticketType.lower() == "group":
            # 50% discount for group tickets
            ticket_price *= 0.5
            return ticket_price
        elif self.__ticketType.lower() in ["child", "teacher", "student", "senior"]:
            return 0  # Free ticket for children, teachers/students, and seniors
        else:
            raise ValueError("Invalid ticket type.") #a value error if the ticket types are correct

    # Setters and getters
    def set_ticketID(self, ticketID):
        self.__ticketID = ticketID

    def get_ticketID(self):
        return self.__ticketID

    def set_ticketType(self, ticketType):
        self.__ticketType = ticketType

    def get_ticketType(self):
        return self.__ticketType

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


class Person:
    '''Class to represent a person'''
    # Constructor
    def __init__(self, nameP, age, gender):
        self._nameP = nameP
        self._age = age
        self._gender = gender
        self._ticket = None  # Ticket attribute added to represent a person may possess a ticket

    # Setters and getters
    def set_nameP(self, nameP):
        self._nameP = nameP

    def get_nameP(self):
        return self._nameP

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_ticket(self, ticket):
        self._ticket = ticket

    def get_ticket(self):
        return self._ticket