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


#Aggregation
while True: #using a while loop to make the user re-enter if it was invalid
    try:
        # Get user input for the artwork
        title = input("Enter the title of the artwork: ")
        artist = input("Enter the name of the artist: ")
        style = input("Enter the style of the artwork: ")

        # Create an Artwork object
        artwork = Artwork(title, artist, style)

        # Get user input for the exhibition hall
        while True: #using a while loop to make the user re-enter if it was invalid
            hall_choice = input("Choose the exhibition hall (hall1 or hall2): ")
            if hall_choice == "hall1":
                hall_name = "Hall 1"
                hall_location = "Ground Floor"
                hall_size = "Medium"
                break  # Exit the hall choice loop if the choice is valid
            elif hall_choice == "hall2":
                hall_name = "Hall 2"
                hall_location = "First Floor"
                hall_size = "Small"
                break  # Exit the hall choice loop if the choice is valid
            else:
                print("Invalid hall choice. Please try again.")

        # Create an ExhibitionHall object
        hall = ExhibitionHall(hall_name, hall_location, hall_size)

        # Add the artwork to the exhibition hall
        hall.add_artwork(artwork)

        # Print exhibition hall details including the artwork
        print(hall)

        break  # Exit the main loop if everything executed successfully

    except ValueError as e: #this will happen when the user enters an invalid value
        print("Error:", e) #printing what the error is
        print("Please try again.")
    except TypeError as e: #this will happen when the user inputs the wrong type
        print("Error:", e) #printing what the error is
        print("Please try again.")
    finally:
        print("Execution completed.")


#Inheritance
try:
    # Creating instances of Person and Employee classes with user inputs
    while True: #using a while loop to make the user re-enter if it was invalid
        person_name = input("Enter person's name: ")
        if not person_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True: #using a while loop to make the user re-enter if it was invalid
        person_age = input("Enter person's age: ")
        if not person_age.isdigit():
            print("Age should be a positive integer.")
        else:
            person_age = int(person_age)
            break

    while True: #using a while loop to make the user re-enter if it was invalid
        person_gender = input("Enter person's gender (Male/Female): ").capitalize()
        if person_gender not in ["Male", "Female"]:
            print("Gender should be Male or Female.")
        else:
            break

    person1 = Person(person_name, person_age, person_gender)

    while True: #using a while loop to make the user re-enter if it was invalid
        emp_ID = input("Enter employee ID: ")
        if not emp_ID:
            print("Employee ID cannot be empty.")
        else:
            break

    while True: #using a while loop to make the user re-enter if it was invalid
        emp_name = input("Enter employee's name: ")
        if not emp_name.isalpha():
            print("Name should only contain alphabetic characters.")
        else:
            break

    while True: #using a while loop to make the user re-enter if it was invalid
        emp_age = input("Enter employee's age: ")
        if not emp_age.isdigit():
            print("Age should be a positive integer.")
        else:
            emp_age = int(emp_age)
            break

    while True: #using a while loop to make the user re-enter if it was invalid
        emp_gender = input("Enter employee's gender (Male/Female): ").capitalize()
        if emp_gender not in ["Male", "Female"]:
            print("Gender should be Male or Female.")
        else:
            break

    employee1 = Employee(emp_ID, emp_name, emp_age, emp_gender)

    # Testing setters and getters for Person class
    print("\nPerson 1 Details:")
    print("Name:", person1.get_nameP()) #get from the person class
    print("Age:", person1.get_age()) #get from the person class
    print("Gender:", person1.get_gender()) #get from the person class

    # Testing setters and getters for Employee class
    print("\nEmployee 1 Details:")
    print("Employee ID:", employee1.get_empID()) #get from the employee class
    print("Name:", employee1.get_nameP()) #get from the person class
    print("Age:", employee1.get_age()) #get from the person class
    print("Gender:", employee1.get_gender()) #get from the person class

except ValueError as e: #this will happen when the user enters an invalid value
    print("Error:", e) #printing what the error is
finally:
    print("Execution completed.")