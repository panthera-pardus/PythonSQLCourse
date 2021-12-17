from datetime import datetime
import database


menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add a new user
7) Search for a movie
8) Exit

Your selection: """
welcome = "Welcome to the watchlist app!"

def prompt_add_movies():
    
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY):")
    parsed_date = datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movies(title, timestamp)

def print_movie_list(heading, movies):

    print(f"-- {heading} movies --")
    for _id, title, release_date in movies:

        movie_date = datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id} : {title} (on {human_date})")
        print("-----\n")

def prompt_watch_movie():
    username = input("Username: ")
    movie_title = input("Movie ID: ")
    database.watch_movies(movie_title, username)

def print_watched_movie_list(username, movies):
    print(f"-- {username}'s watched movies --")
    for movie in movies:
        print(f"{movie[1]}")
    print("-----\n")

def prompt_watch_movie():
    username = input("USername: ")
    movie_id = input("Movie ID: ")
    database.watch_movies(username, movie_id)

def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)

def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("This user has no watched movie")

def prompt_search_movies():
    search_term = input("Enter the partial movie title")
    movies = database.search_movies(search_term)
    
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("No movies found")



print(welcome)
database.create_tables()

while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movies()
    elif user_input == "2":
        print_movie_list(heading = "Upcoming", movies = database.get_movies(upcoming = True))
    elif user_input == "3":
        print_movie_list(heading = "Released", movies = database.get_movies(upcoming = False))
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")