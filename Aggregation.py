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