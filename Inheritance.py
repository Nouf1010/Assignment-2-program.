class Person:
    '''Class to represent a person'''
    # Constructor
    def __init__(self, nameP, age, gender): #private attributes because its an inheritance relationship
        self._nameP = nameP
        self._age = age
        self._gender = gender
        self._ticket = None  # Ticket attribute added to represent a person may have a ticket

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

class Employee(Person): #calling the parent class to inherit from it
    '''Class to represent an employee'''
    #Constructor
    def __init__(self, empID, nameP, age, gender):
        super().__init__(nameP, age, gender) #inherits attributes from the parent class
        self.__empID = empID

    # Setters and getters
    def set_empID(self, empID):
        self.__empID = empID

    def get_empID(self):
        return self.__empID