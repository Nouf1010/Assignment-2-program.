class ExhibitionHall:
    '''Class to represent an exhibition hall'''
    # Constructor and making the attributes private
    def __init__(self, nameE, locationE, sizeE):
        self.__nameE = nameE
        self.__locationE = locationE
        self.__sizeE = sizeE

    # Setters and getters
    def set_name(self, nameE):
        self.__nameE = nameE

    def get_name(self):
        return self.__nameE

    def set_location(self, locationE):
        self.__locationE = locationE

    def get_location(self):
        return self.__locationE

    def set_size(self, sizeE):
        self.__sizeE = sizeE

    def get_size(self):
        return self.__sizeE

    #Using the str function to represent the ExhibitionHall object as a string
    def __str__(self):
        return "Exhibition Hall: " + self.__nameE + ", Location: " + self.__locationE + ", Size: " + self.__sizeE


class Museum:
    '''Class to represent a museum'''
    # Constructor and making the attributes private
    def __init__(self, nameM, locationM, sizeM):
        self.__nameM = nameM
        self.__locationM = locationM
        self.__sizeM = sizeM
        # Creating exhibition halls for the museum
        self.__exhibition_halls = self.create_exhibition_halls()

    # Setters and getters
    def set_name(self, nameM):
        self.__nameM = nameM

    def get_name(self):
        return self.__nameM

    def set_location(self, locationM):
        self.__locationM = locationM

    def get_location(self):
        return self.__locationM

    def set_size(self, sizeM):
        self.__sizeM = sizeM

    def get_size(self):
        return self.__sizeM