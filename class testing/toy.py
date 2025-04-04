class Toy:
    def __init__(self, list):
        self.toys = list
        self.colours = []

    def print_name(self):
        for item in self.toys:
            print(item['name'])

    def print_colours(self):
        for item in self.toys:
            self.colours.append(item['colour'])
        print(self.colours)

