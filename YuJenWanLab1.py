""" This program asks for the user to add their favorite movies to a
movie list and the user enter a command to adding a movie, checking the
entire list of movies, and deleting their unwanted movies from the list.

"""


class Movie:
    """ Add a Movie class;      Attributes: name, year   """
    __movieList = []

    def __init__(self, name="", year=2021):
        """ Initializes a dataset object """
        self.name = name
        self.year = year

    @staticmethod
    def strOK(name):
        return isinstance(name, str) and len(name) <= 50

    @staticmethod
    def yearOK(year):
        try:
            year = int(year)
        except ValueError:
            return False
        return 1000 <= year < 2023

    def setName(self, name):
        if self.strOK(name):
            self.name = name
            return True
        print(f"Invalid movie name {name}")
        return False

    def setYear(self, year):
        if self.yearOK(year):
            self.year = year
            return True
        print(f"Invalid movie year {year}")
        return False

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def getStr(self):
        return f"{self.name} ({self.year})"

    @classmethod
    def list(cls):
        if cls.__movieList:
            for movie_number, item in enumerate(cls.__movieList, 1):
                print(f"{movie_number}. {item.getStr()}")
        else:
            print("No any movie in the list!!")

    @classmethod
    def add(cls, movie):
        """Add each movie into item list """
        cls.__movieList.append(movie)
        print(f"{movie.getName()} was added.")

    @classmethod
    def delete(cls, number):
        movie = cls.__movieList.pop(number-1)
        print(f"{movie.getName()} was deleted.")

    @classmethod
    def menu(cls):
        print("")
        print("COMMAND MENU")
        print("list - List all movie")
        print("add -  Add a movie")
        print("del -  Delete a movie")
        print("exit - Exit program")
        while True:
            print("")
            selected_command = input("Command: ")
            try:
                str(selected_command)  # check the input is a string
            except ValueError:
                print("Please only enter one of the commands on the menu, "
                      "thank you!")
                continue  # ask the user to one command again
            if selected_command == "exit":
                print("Bye!")
                break  # exit the loop
            elif selected_command == "list":
                cls.list()
            elif selected_command == "add":
                movie = Movie()
                name = input("Name: ")
                if not movie.setName(name):
                    continue
                year = input("year: ")
                if not movie.setYear(year):
                    continue
                cls.add(movie)
            elif selected_command == "del":
                if 0 <= len(cls.__movieList):
                    number = input("Number: ")
                    try:
                        number = int(number)
                        cls.delete(number)
                    except ValueError:
                        print(f"Invalid number {number}")
                        continue  # ask the user to type a number again
                else:
                    print("The movie list is empty now.")

            else:
                print("This command is not on the menu.")
