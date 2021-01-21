MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit:"
Movies = []


def add_movie():
    title = input("Enter the movie title:")
    year = input("Enter the movie release year:")

    Movies.append({
        'title': title,
        'year':year
    })


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")


def list_movies():
    for counter, movie in enumerate(Movies):
        print(f"No.: {counter}")
        print_movie(movie)


def find_movie():
    search_title_year = input("Enter title or year of release:")
    for movie in Movies:
        if search_title_year in movie['title'] or search_title_year == movie['year']:
            print_movie(movie)
        else:
            print("\n\nWe have not found any things\n\n")

user_option = {"a": add_movie,
               "f": find_movie,
               "l": list_movies}


def MENU():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_option:
            selected_function = user_option[selection]
            selected_function()
        else:
            print("Unknown command, please try again.")

        selection = input(MENU_PROMPT)


MENU()