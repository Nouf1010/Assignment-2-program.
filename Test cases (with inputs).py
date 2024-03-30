#importing all the files needed
from Composition import *
from Aggregation import *
from Inheritance import *
from Unidirectional import *

#Composition
# Create the exhibition halls
hall1 = ExhibitionHall("Hall 1", "Ground Floor", "Medium")
hall2 = ExhibitionHall("Hall 2", "First Floor", "Small")

# Get user input for the new hall
new_hall_name = input("Enter the name of the new exhibition hall: ")

# Create the museum
louvre = Museum("Louvre Museum", "Paris", "Large")

try:
    while True: #using a while loop to make the user re-enter if it was invalid
        try:
            # Input information for the new exhibition hall
            new_hall_location = input(
                "Enter the location of the new exhibition hall (Ground floor, First floor, Second floor, Third floor): ")
            if new_hall_location.lower() not in ["ground floor", "first floor", "second floor", "third floor"]:
                raise ValueError("Invalid location. Please enter one of: Ground Floor, First Floor, Second Floor, Third Floor.")
            break  # Exit the loop if location input is valid
        except ValueError as e: #this will happen when the user enters an invalid value
            print("Error:", e) #printing what the error is

    while True: #using a while loop to make the user re-enter if it was invalid
        try:
            new_hall_size = input("Enter the size of the new exhibition hall (Large, Medium, Small): ")
            if new_hall_size.lower() not in ["large", "medium", "small"]:
                raise ValueError("Invalid size. Please enter one of: Large, Medium, Small.")
            break  # Exit the loop if size input is valid
        except ValueError as e: #this will happen when the user enters an invalid value
            print("Error:", e) #printing what the error is

    new_hall = ExhibitionHall(new_hall_name, new_hall_location, new_hall_size)

    # Add the new exhibition hall to the museum
    louvre.add_exhibition_hall(new_hall)
    print("New exhibition hall added successfully to the museum.")
except TypeError as e: #this will happen when the user inputs the wrong type
    print("Error in adding the new exhibition hall to the museum:", e)
finally:
    # Print museum details including the new exhibition hall
    print(louvre)