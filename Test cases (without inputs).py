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


#---Unidirectional (The purchase of tickets)---
# Test case for an adult
name_adult = "John"
age_adult = 30
gender_adult = "Male"
ticket_type_adult = "Adult"
ticket_adult = Ticket(ticketID=1, ticketType=ticket_type_adult, price=63)  # Price for a ticket
person_adult = Person(nameP=name_adult, age=age_adult, gender=gender_adult)

# Test case for a student
name_student = "Emma"
age_student = 20
gender_student = "Female"
ticket_type_student = "Student"
ticket_student = Ticket(ticketID=2, ticketType=ticket_type_student, price=63)  # Price for a ticket
person_student = Person(nameP=name_student, age=age_student, gender=gender_student)

# Test case for a teacher
name_teacher = "Mr. Brown"
age_teacher = 45
gender_teacher = "Male"
ticket_type_teacher = "Teacher"
ticket_teacher = Ticket(ticketID=3, ticketType=ticket_type_teacher, price=63)  # Price for a ticket
person_teacher = Person(nameP=name_teacher, age=age_teacher, gender=gender_teacher)

# Test case for a child
name_child = "Ashly"
age_child = 10
gender_child = "Female"
ticket_type_child = "Child"
ticket_child = Ticket(ticketID=4, ticketType=ticket_type_child, price=63)  # Price for a ticket
person_child = Person(nameP=name_child, age=age_child, gender=gender_child)

# Test case for a senior
name_senior = "James"
age_senior = 70
gender_senior = "Male"
ticket_type_senior = "Senior"
ticket_senior = Ticket(ticketID=5, ticketType=ticket_type_senior, price=63)  # Price for a ticket
person_senior = Person(nameP=name_senior, age=age_senior, gender=gender_senior)

# Test case for a group
name_group = "Tom"
age_group = 40
gender_group = "Male"
ticket_type_group = "Group"
ticket_group = Ticket(ticketID=6, ticketType=ticket_type_group, price=63)  # Price for a ticket
person_group = Person(nameP=name_group, age=age_group, gender=gender_group)

# Printing ticket purchase details for each test case
print("\nTicket Purchase Details:")
print("Ticket ID:", ticket_adult.get_ticketID())
print("Name:", person_adult.get_nameP())
print("Age:", person_adult.get_age())
print("Gender:", person_adult.get_gender())
print("Ticket Type:", ticket_type_adult)
print("Ticket Price:", ticket_adult.calculate_price(person_adult.get_age()))  # Using the function calculate_price

print("\nTicket ID:", ticket_student.get_ticketID())
print("Name:", person_student.get_nameP())
print("Age:", person_student.get_age())
print("Gender:", person_student.get_gender())
print("Ticket Type:", ticket_type_student)
print("Ticket Price:", ticket_student.calculate_price(person_student.get_age()))

print("\nTicket ID:", ticket_teacher.get_ticketID())
print("Name:", person_teacher.get_nameP())
print("Age:", person_teacher.get_age())
print("Gender:", person_teacher.get_gender())
print("Ticket Type:", ticket_type_teacher)
print("Ticket Price:", ticket_teacher.calculate_price(person_teacher.get_age()))

print("\nTicket ID:", ticket_child.get_ticketID())
print("Name:", person_child.get_nameP())
print("Age:", person_child.get_age())
print("Gender:", person_child.get_gender())
print("Ticket Type:", ticket_type_child)
print("Ticket Price:", ticket_child.calculate_price(person_child.get_age()))

print("\nTicket ID:", ticket_senior.get_ticketID())
print("Name:", person_senior.get_nameP())
print("Age:", person_senior.get_age())
print("Gender:", person_senior.get_gender())
print("Ticket Type:", ticket_type_senior)
print("Ticket Price:", ticket_senior.calculate_price(person_senior.get_age()))

print("\nTicket ID:", ticket_group.get_ticketID())
print("Name:", person_group.get_nameP())
print("Age:", person_group.get_age())
print("Gender:", person_group.get_gender())
print("Ticket Type:", ticket_type_group)
print("Ticket Price:", ticket_group.calculate_price(person_group.get_age()))