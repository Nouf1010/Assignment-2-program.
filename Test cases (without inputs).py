#importing all the files needed
from Composition import *
from Aggregation import *
from Inheritance import *
from Unidirectional import *

#---Composition (Adding a new exhibition hall)---
# Create a new exhibition hall
new_hall = ExhibitionHall("New Hall", "Second Floor", "Large")

# Create the museum
louvre = Museum("Louvre Museum", "Paris", "Large")

# Add the new exhibition hall to the museum
louvre.add_exhibition_hall(new_hall)

# Print museum details including the new exhibition hall
print(louvre)


#---Aggregation (Adding new art)---
# Create artworks
mona_lisa = Artwork("Mona Lisa", "Leonardo da Vinci", "Renaissance")
starry_night = Artwork("The Starry Night", "Vincent van Gogh", "Post-Impressionism")

# Create an exhibition hall
hall1 = ExhibitionHall("Hall 1", "Ground Floor", "Medium")

# Add artworks to the exhibition hall
hall1.add_artwork(mona_lisa)
hall1.add_artwork(starry_night)

# Print exhibition hall details including artworks
print(hall1)


#---Inheritance (Showing the inheritance relationship)---
# Creating instances of Person and Employee classes
person1 = Person("Amy", 30, "Female")
employee1 = Employee("EMP231", "Tim", 35, "Male")

# Testing setters and getters for Person class
print("Person 1 Details:")
print("Name:", person1.get_nameP())
print("Age:", person1.get_age())
print("Gender:", person1.get_gender())

# Testing setters and getters for Employee class
print("\nEmployee 1 Details:")
print("Employee ID:", employee1.get_empID())
print("Name:", employee1.get_nameP())
print("Age:", employee1.get_age())
print("Gender:", employee1.get_gender())