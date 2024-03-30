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
