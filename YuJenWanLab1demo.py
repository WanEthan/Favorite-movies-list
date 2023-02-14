from YuJenWanLab1 import Movie


def main():
    """

    """
    movie1 = Movie("Avatar", 2009)
    movie2 = Movie("Top Gun: Maverick", 2022)
    movie3 = Movie("Minions: The Rise of Gru", 2022)
    Movie.add(movie1)
    Movie.add(movie2)
    Movie.add(movie3)
    Movie.menu()


if __name__ == "__main__":
    main()

"""

------Sample Run------

Avatar was added.
Top Gun: Maverick was added.
Minions: The Rise of Gru was added.

COMMAND MENU
list - List all movie
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command: list
1. Avatar (2009)
2. Top Gun: Maverick (2022)
3. Minions: The Rise of Gru (2022)

Command: add
Name: The Shawshank Redemption
year: 1994
The Shawshank Redemption was added.

Command: add
Name: The Godfather
year: 1972
The Godfather was added.

Command: list
1. Avatar (2009)
2. Top Gun: Maverick (2022)
3. Minions: The Rise of Gru (2022)
4. The Shawshank Redemption (1994)
5. The Godfather (1972)

Command: del
Number: 4
The Shawshank Redemption was deleted.

Command: list
1. Avatar (2009)
2. Top Gun: Maverick (2022)
3. Minions: The Rise of Gru (2022)
4. The Godfather (1972)

Command: exit
Bye!

Process finished with exit code 0

"""
