# Guided Exploration No. 3
# Scott Daron

# This part of the code is used to implement the random library in order to make it possible to generate random numbers
import random

# It's here where we establish the possible names code as currently empty, creating a space to store all the
# rap names from the rap name text file
possible_names = []


# This part is to open a new file and store the names generated by the code.
outputFile = open('rap-names-output.txt', 'w')


# It's at this point where the file is opened to be read, and then prepares to do stuff to it. Stuff that is
# specified in the code below
with open('rap-names.txt', 'r') as dataFile:
    # This for loop will iterate through each line in the file one at a time
    for name in dataFile:
        # This part of the code strips the white space off of each line of the code and then appends them to
        # the empty list one at a time
        possible_names.append(name.rstrip())

# This part of the code will get the user input for how many names they'd like to create
count = int(input('How many rap names would you like to create? '))
# There's another input request that asks how many parts should the name have
parts = int(input('How many parts should the name contain? '))

# This loop will take the count value and use it to determine how many rap names will be generated
for i in range(count):
    # It's here where we generate a new list to hold all the rap name parts generated
    name_parts = []
    # This nested loop will be used to generate the amount of parts the user wants to be in the name
    for j in range(parts):
        # In this part, a multitude of things are established: It lays out the random generation process by
        # calling upon the random library and setting its parameters to between zero, the length of the list,
        # and minus one. The number it randomly generates will correlate with a name on the list, and then
        # append that name to the name parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # This point is where the name parts are glued together with a space between each one, and then written
        # into the files
    outputFile.write(f"{' '.join(name_parts)}\n")
    # This is where the previous equation used to glue the parts together is used to print the result out
    # for the user to see for themselves
    print(f"{' '.join(name_parts)}")

# This one is simple. It closes the file now that it's done with it and the task is complete.
outputFile.close()
