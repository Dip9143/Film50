import requests
from pyfiglet import Figlet
import requests
import os
import json
from tabulate import tabulate
import textwrap

# TMDB movie data base api key
API_KEY = "be3abc30c7d421c54761878ee9a0a6d8"

def main():
    # If Watched_movies.json not exists, it creates the file
    if not os.path.exists("watched_movies.json"):
        with open("watched_movies.json", 'w') as file:
            json.dump([], file)

    # If Not_interested_movies.json not exists, it creates the file
    if not os.path.exists("Not_interested_movies.json"):
        with open("Not_interested_movies.json", 'w') as file:
            json.dump([], file)

    print(ascii_art("Film50"), end = '')
    usin = input_option([
        "Recommend a movie for me",
        "search for a film",
        "Find by a person(Director/Actor/Actress...)",
        "clear my watch history",
        "clear not interested movie section"])

    match usin:
        case 1:
            # Going recommend films based on genre or toprated
            rec_film()
        case 2:
            # seaches a film name
            search_film()
        case 3:
            # Searches person's profession and related movies to him
            find_per()
        case 4:
            # Clean watch history
            clear_watch()
        case 5:
            # Clean not interested section history
            clear_not()



def input_option(input_list):
    ''' Main menu'''
    i = 1
    for item in input_list:
        print(f"[{i}] {item.title()}")
        i += 1
    while True:
        usin = input("\nSelect any option no: ")
        if usin.isdigit() and 1 <= int(usin) <= len(input_list):
            return int(usin)
        else:
            continue

# Recommend a movie for me section ------------
def rec_film():
        try:
            print(ascii_art("Recommand a film for me", "digital"), end = '')
            print("Press ctrl+D to return to main options")
            usin = input_option(["top rated", "by genre"])
            match usin:
                case 1:
                    toprated()
                case 2:
                    bygenre()

        except EOFError:
            main()

def toprated():
    print(ascii_art("Toprated", "digital"), end = '')
    i = 1
    while True:
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&page={i}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
        else:
            print("Failed to retrieve data:", response.status_code)
            break

        if data["total_results"] == 0 or data["total_pages"] < i:
            print("Nothing Founnd!!!")
            break

        r_list = watched_movies(data["results"])
        if r_list[0]:
            print_film_and_add_to_watchlist(r_list[1])
            break
        else:
            continue
        i += 1

def bygenre():
    print(ascii_art("By Genere", "digital"), end = '')
    base_url = "https://api.themoviedb.org/3"
    genre_url = f"{base_url}/genre/movie/list?api_key={API_KEY}"

    response = requests.get(genre_url)

    if response.status_code == 200:
        genres = response.json()["genres"]
        l_g = {genre["name"]: genre["id"] for genre in genres}

        for key in l_g:
            print(f"|{key}| ", end = "")
        print()
        usin = input("Select any genre from the above mentioned list.\n")
        if usin.title() in l_g:
            i = 1
            while True:
                url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={l_g[usin.title()]}&page={i}"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                else:
                    print("Failed to retrieve data:", response.status_code)
                    break

                if data["total_results"] == 0 or data["total_pages"] < i:
                    print("Nothing Founnd!!!")
                    break

                r_list = watched_movies(data["results"])
                if r_list[0]:
                    print_film_and_add_to_watchlist(r_list[1])
                    break

                else:
                    continue
                i += 1
        else:
            print("Unexpected input!!!")


    else:
        print("Failed to retrieve genres:", response.status_code)

# ------------

# Search for a film ------------

def search_film():
    print(ascii_art("Search for a film", "digital"), end = '')
    movie_name = input("Enter the name of the film: ")
    i = 1
    while True:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name.title()}&language=en-US&page={i}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
        else:
            print("Failed to retrieve data:", response.status_code)
            break

        if data["total_results"] == 0 or data["total_pages"] < i:
            print("Nothing Founnd!!!")
            break

        r_list = watched_movies(data["results"])
        if r_list[0]:
            print_film_and_add_to_watchlist(r_list[1])
            break
        else:
            continue
        i += 1

# ------------

# Find a person ------------

def find_per():
    print(ascii_art("Find by a person", "digital"), end = '')
    person_name = input("Enter the person's name: ")
    person_id, profession = search_person(person_name)

    if person_id:
        print("\n" + "="*60)
        print(f"  Profession: {profession}".center(60))
        print("="*60)

        if profession == "Directing":
            movies = get_director_movies(person_id)
            print("\nMovies directed by", person_name, ":")
            print("-" * 60)
            for i, movie in enumerate(movies, start=1):
                print(f"{i}. {movie}")
            print("...")
            print("=" * 60 + "\n")
        else:
            related_movies = get_related_movies(person_id)
            print(f"\nMovies related to {person_name} (Not Directed):")
            print("-" * 60)
            for i, movie in enumerate(related_movies, start=1):
                print(f"{i}. {movie}")
            print("...")
            print("=" * 60 + "\n")
    else:
        print("\nPerson not found.\n")

def search_person(person_name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={person_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            person = data["results"][0]
            person_id = person["id"]
            profession = person["known_for_department"]
            return person_id, profession
    return None, None

def get_director_movies(person_id):
    url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = [movie["title"] for movie in data["crew"] if movie["job"] == "Director"][:5]
        return movies
    return []

def get_related_movies(person_id):
    url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = [movie["title"] for movie in data["cast"]][:5]
        return movies
    return []

# -------------

# Clean watch history -------------
def clear_watch():
    with open("Not_interested_movies.json", 'w') as file:
        json.dump([], file)
    print("Your watch history has been succesfully cleaned!!!")

# -------------

# Clean not interested section -------------

def clear_not():
    with open("watched_movies.json", 'w') as file:
        json.dump([], file)
    print("The section has been succesfully cleaned!!!")

# -------------

# Checks what movie is right choice based on previous information -------------
def watched_movies(data_dic):
    with open("watched_movies.json", 'r') as file1, open("Not_interested_movies.json", 'r') as file2:
        list_watched_films = json.load(file1)
        list_not_interested = json.load(file2)
        for item in data_dic:
            if item["title"] not in list_watched_films and item["title"] not in list_not_interested:
                return [True, item]
    return [False, None]

# -------------

# Data organizing and priting purpose -------------
def print_film_and_add_to_watchlist(data_dic):
    data_dic_s = {
        "Title" : data_dic["title"],
        "Original Language" : data_dic["original_language"],
        "Rating" : data_dic["vote_average"],
        "Release Date" : data_dic["release_date"],
        "Id" : data_dic["id"],
        "Original Title" : data_dic["original_title"],
        "Overview" : data_dic["overview"],
        "Director" : get_director(data_dic["id"]),
    }

    tabulate_form(data_dic_s)

    x = input("Are you going to watch this film?[(y/n) or press any key to bypass this section] ")

    if x == 'y':
        file_path = "watched_movies.json"
        with open(file_path, 'r') as file:
            my_list_from_json = json.load(file)

        my_list_from_json.append(data_dic["title"])

        with open(file_path, 'w') as file:
            json.dump(my_list_from_json, file)

        print("\nWalah! This film has been saved succesfully into your watch history!!!")
    elif x == 'n':
        file_path = "Not_interested_movies.json"
        with open(file_path, 'r') as file:
            my_list_from_json = json.load(file)

        my_list_from_json.append(data_dic["title"])

        with open(file_path, 'w') as file:
            json.dump(my_list_from_json, file)

        print("\nThis film has been added to the 'Not Interested' section!")
        main()

def get_director(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        credits = response.json()
        for crew_member in credits["crew"]:
            if crew_member["job"] == "Director":
                return crew_member["name"]
    return None


def tabulate_form(data_dic):
    table = [[key,item] for key, item in data_dic.items() if key != "Overview"]
    print(tabulate(table, tablefmt="grid"))

    wrapped_text = textwrap.fill(data_dic["Overview"], width=70)
    print("\n" + "="*70)
    print("Overview:".center(70))
    print("-"*70)
    print(wrapped_text)
    print("="*70)



def ascii_art(s, f_s = 'standard'):
    ''' Convert a string into a ascii art string'''
    figlet = Figlet()
    figlet.setFont(font= f_s)
    return figlet.renderText(s)

# -------------

if __name__ == "__main__":
    main()
