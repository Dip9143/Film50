# Film50 - Personalized Movie Recommender and Watchlist Manager
#### Video Demo:  <https://www.youtube.com/watch?v=VLEs1zPheK4>
#### Description:

## Overview
Film50 is an interactive Python-based movie recommendation and watchlist management app designed to help you explore movies that align with your tastes, preferences, and mood. By harnessing the powerful TMDb (The Movie Database) API, Film50 brings a wealth of movie data and insights directly to your fingertips. Whether you're looking to discover highly-rated films, search for movies featuring your favorite actors, or simply manage your watchlist, Film50 is here to make your cinematic experience more enjoyable and organized.

In today's digital world, where the availability of content can be overwhelming, Film50 simplifies your movie-watching decisions. Gone are the days of aimlessly scrolling through lists of movies or relying on algorithms with little customization options. With Film50, you’re in control of your movie recommendations, creating a curated and enjoyable experience that matches your unique preferences.

## Key Features and Functionalities
Film50 offers a wide range of features that elevate it from a simple movie search app to a fully interactive movie recommendation platform. Below are the core features that make Film50 an ideal movie companion:

### 1. Personalized Movie Recommendations
Film50 provides several tailored recommendation options based on different criteria, including:
   - **Top-Rated Movies**: If you're looking for the best films of all time, Film50 pulls in a list of the highest-rated movies globally. This feature is perfect for those who want to explore acclaimed films and all-time classics.
   - **Genre-Based Recommendations**: Customize your recommendations based on your preferred genre, such as Action, Comedy, Drama, Thriller, and many more. This helps you find movies that align with your current mood or genre interest.

### 2. Search and Discover
The search and discovery options allow you to actively seek out movies based on different aspects, such as:
   - **Film Search by Title**: Have a specific movie in mind? Simply enter the name, and Film50 will retrieve all relevant details, including the movie’s rating, release date, overview, and more.
   - **Find Movies by Actor/Director**: Love watching movies starring a particular actor or films directed by a certain filmmaker? Film50 enables you to look up movies associated with specific actors, actresses, or directors, helping you discover more from the people you enjoy watching on screen.

### 3. Watchlist Management
Film50 enhances the movie-watching experience by allowing users to manage their watchlists effectively:
   - **Track Watched Movies**: Keep a record of the movies you’ve already watched, so you don’t accidentally rewatch or lose track of past films.
   - **Maintain a "Not Interested" List**: Add movies that you don’t want to see to a "Not Interested" list. Film50 will then exclude these movies from future recommendations, providing a more focused and refined selection.
   - **Clear Lists**: Easily reset your watch history or "Not Interested" list if you wish to start fresh or want to reintroduce movies back into your recommendations.

### 4. Detailed Information for Each Movie
For every recommended or searched movie, Film50 provides extensive details to help you make an informed viewing choice. The details include:
   - **Title**: The name of the movie.
   - **Original Language**: The primary language in which the movie was originally created.
   - **Rating**: The average rating by viewers on TMDb, which can give you a sense of the movie’s reception.
   - **Release Date**: The release date of the movie.
   - **Director**: The director(s) of the film, giving insight into its creative vision.
   - **Overview**: A concise synopsis of the movie, so you know what it’s about before committing to watch.

## How Film50 Works
Film50 was built using Python and interacts directly with the TMDb API to retrieve live movie data. Here’s how the app operates from setup to usage:

1. **API Setup**: To begin, you’ll need an API key from [TMDb](https://www.themoviedb.org/documentation/api). After obtaining the key, replace the placeholder in the `API_KEY` variable with your personal key.

2. **Dependencies and Libraries**: Film50 relies on the following Python libraries:
   - **requests**: For making HTTP requests to the TMDb API to retrieve movie data.
   - **pyfiglet**: To create a visually engaging ASCII art title and headers.
   - **tabulate**: To display movie data in an easy-to-read, tabular format.
   - **json**: To save and manage user preferences in JSON format for storing watch history and "Not Interested" lists.

3. **Running Film50**: Once the API key is set up and dependencies are installed (with `pip install requests pyfiglet tabulate`), you can launch Film50 by running `python film50.py`. The app will start, and you’ll be greeted with a welcoming interface with options to receive recommendations, search for movies, or manage your watchlists.

4. **Using the Interface**: The user-friendly menu interface provides several options, each guiding you toward your desired functionality, be it searching, managing lists, or getting recommendations.

## Technical Design and Implementation
Film50’s code structure follows a modular design, with separate functions for interacting with the API, handling data processing, and managing user preferences through JSON files.

Upon launch, Film50 checks for the existence of `watched_movies.json` and `Not_interested_movies.json` files, which store data on watched and "Not Interested" movies, respectively. This persistent storage feature allows the app to retain user preferences across sessions. Additionally, when users make selections, Film50 interacts with the TMDb API, retrieves real-time movie data, and formats it for display using `tabulate` for clear and concise tables.

### Future Enhancements
To further improve Film50, here are some features we plan to add in the future:
- **User Ratings and Reviews**: Allow users to rate movies within the app and store these ratings to personalize future recommendations.
- **Advanced Filters**: Add filters by language, year, and cast to refine recommendations.
- **Graphical User Interface (GUI)**: Develop a graphical version of the app to make navigation easier for users unfamiliar with command-line applications.

## Conclusion
Film50 provides a comprehensive solution for movie enthusiasts who want a more personalized and organized approach to discovering and managing movies. It transforms the movie-watching experience, making it more accessible and tailored to individual preferences. With Film50, users can seamlessly explore new recommendations, manage their watchlists, and access detailed information on any movie they wish to watch. Designed with usability and practicality in mind, Film50 stands as a reliable movie companion for anyone looking to make movie selection easier and more enjoyable.

---

### Credits and Acknowledgments
- **TMDb API**: Data is sourced from [The Movie Database](https://www.themoviedb.org), a community-built movie database.
- **Libraries**: Built using Python libraries like `requests`, `pyfiglet`, `tabulate`, and `json`.

Film50 simplifies the overwhelming world of movies, helping you discover the perfect film for any occasion. Enjoy a seamless movie journey with Film50!
