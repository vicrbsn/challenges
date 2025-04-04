from toy import Toy

toys = [
    {
        "name": "Ball",
        "colour": "red"
    },
    {
        "name": "Teddy",
        "colour": "brown"
    }
]

# Make a toys list with at least 2 dictionaries representing a toy with name and colour DONE

# create a function to print out the name of all toys

def toy_names(list):
    for dict in list:
        print(dict['name'])
toy_names(toys)

# create a function to print out all colours of toys. print(print_colours()) => ['red', 'green']

def toy_colours(list):
    colour_list = []
    for dict in list:
        colour_list = [*colour_list, dict['colour']]
    print(colour_list)

toy_colours(toys)

# Now do this with classes

subject = Toy(toys)
subject.print_name()
subject.print_colours()
