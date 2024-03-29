class Artwork:
    '''Class to represent artwork'''
    #Constructor
    def __init__(self, title, artist, style):
        self.__title = title
        self.__artist = artist
        self.__style = style

    # Setters and getters
    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_artist(self, artist):
        self.__artist = artist

    def get_artist(self):
        return self.__artist

    def set_style(self, style):
        self.__style = style

    def get_style(self):
        return self.__style

    #Using the str function to represent the artwork object as a string
    def __str__(self):
        return "Artwork: " + self.__title + ", Artist: " + self.__artist + ", Style: " + self.__style

class ExhibitionHall:
    '''Class to represent an exhibition hall'''
    # Constructor
    def __init__(self, nameE, locationE, sizeE):
        self.__nameE = nameE
        self.__locationE = locationE
        self.__sizeE = sizeE
        self.__artworks = []  # List to hold Artwork objects

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

    def add_artwork(self, artwork):
        self.__artworks.append(artwork)

    #Using the str function to represent the Exhibition Hall object as a string
    def __str__(self):
        hall_info = "Exhibition Hall: " + self.__nameE + ", Location: " + self.__locationE + ", Size: " + self.__sizeE + "\n"
        artwork_info = ""
        # Using a for loop to iterate in the artworks and join their string representations
        for artwork in self.__artworks:
            artwork_info += str(artwork) + "\n" #using += to add then assign right away
        return hall_info + artwork_info