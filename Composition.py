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

    #A function to create an exhibition hall
    def create_exhibition_halls(self):
        # ExhibitionHall objects are created INSIDE the museum and then stored in a list
        exhibition_halls = [
            ExhibitionHall("Hall 1", "Ground Floor", "Medium"),
            ExhibitionHall("Hall 2", "First Floor", "Small")
        ]
        return exhibition_halls

    #A function to add an exhibition hall to the museum
    def add_exhibition_hall(self, hall):
        self.__exhibition_halls.append(hall)

    # Using the str function to represent the museum object as a string
    def __str__(self):
        museum_info = "Museum: " + self.__nameM + ", Location: " + self.__locationM + ", Size: " + self.__sizeM + "\n"
        exhibition_halls_info = ""
        #Using a for loop to iterate in the exhibition halls and join their string representations
        for hall in self.__exhibition_halls:
            exhibition_halls_info += str(hall) + "\n" #using += to add then assign right away
        return museum_info + exhibition_halls_info