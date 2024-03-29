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