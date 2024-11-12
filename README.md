# 🎬 Film50 - Your Personalized Movie Journey Begins Here! 🎥

#### Video Demo: [https://youtu.be/VLEs1zPheK4?si=rdID0kdLaXTxNsNz]

---

## What’s Film50?
Film50 is your new movie buddy—an intelligent and interactive Python-powered movie app that gives you customized recommendations, detailed film info, and a personal watchlist manager all in one! From epic adventure classics to hidden indie gems, Film50 makes it easy to find, track, and manage your next watch. Built with **The Movie Database (TMDb) API**, Film50 offers live, up-to-the-minute data to keep your watchlist fresh and relevant!

When faced with a galaxy of movie options, Film50 helps you zoom in on what *you* want to watch, saving you time and guiding you toward those next big screen moments.

## 🚀 Key Features
### 🎥 Curated Recommendations
Film50's recommendations go beyond basic search, letting you:
   - **Discover Top-Rated Films**: Dive into the highest-rated titles across genres and eras, all just a click away.
   - **Get Genre-Specific Suggestions**: Whether you're feeling like an action-packed thriller, a heartfelt drama, or a lighthearted comedy, pick your genre and let Film50 do the rest!

### 🔍 Search for Your Favorites
Film50 is also your personal film detective! Search by:
   - **Title**: Got a specific movie in mind? Just type it in, and Film50 will bring it to you, complete with all the essential details.
   - **Actors & Directors**: If you're loyal to certain actors or directors, just enter their names to find more movies featuring their talents.

### 📋 Watchlist and Movie Management
Film50 lets you be the master of your own movie universe:
   - **Watched List**: Log the movies you've watched, so you can keep track of your viewing journey.
   - **"Not Interested" List**: Say goodbye to those unwanted movie options by adding them to a list of movies you’d rather skip.
   - **List Reset Options**: Ready for a fresh start? Easily clear your watchlist or "Not Interested" list anytime.

### 🎞️ Movie Details You Need to Know
Each movie Film50 recommends comes with:
   - **Title** and **Language**: Essential for choosing international titles.
   - **Rating**: See what the world thinks with up-to-date ratings.
   - **Release Date**: Perfect for sorting through the latest blockbusters and timeless classics.
   - **Director and Overview**: Get the scoop on who’s behind the magic and what each film is about before you dive in.

## 🛠️ Behind the Scenes
### Requirements
To get started, all you need is:
   - **API Key from TMDb**: Sign up at [TMDb](https://www.themoviedb.org/documentation/api) to get your key.
   - **Python Libraries**:
      - `requests`: Handles the API calls to fetch live data.
      - `pyfiglet`: Adds a splash of ASCII art for a fun interface.
      - `tabulate`: Displays movies in an easy-to-read table format.
      - `json`: Saves and organizes your watch history and preferences.

### Setup
1. **Install Dependencies**:  
   Run `pip install requests pyfiglet tabulate` in your terminal.
2. **Add Your API Key**:  
   Open `film50.py` and place your TMDb API key where specified.
3. **Launch Film50**:  
   Start the app with `python film50.py` and get ready for recommendations!

### How It Works
Film50 is structured to keep things simple yet powerful. From accessing TMDb to managing your preferences, Film50’s functions run the show:
- **API Integration**: Each user action (search, add to watchlist, etc.) triggers an API call, bringing live movie data straight to your screen.
- **Local Storage in JSON**: Your preferences, watch history, and “not interested” list are stored in JSON format, making them easy to load, edit, and reset.

## 🌟 Future Enhancements
Here’s what’s next on the roadmap for Film50:
   - **User Ratings**: Rate movies directly and see personalized recommendations based on your ratings.
   - **Enhanced Search Filters**: Filter movies by language, year, and more for a tailored experience.
   - **Graphical Interface**: Transitioning Film50 into a full-fledged GUI app for an even more intuitive experience.

## Why Film50?
In a world of endless streaming options and recommendation engines, Film50 brings a human touch back to finding movies. Designed to let *you* take the reins, it’s more than a recommendation engine—it’s a personalized movie guide that gets better the more you use it.

## 🎉 Ready to Join the Movie Adventure?
Start your journey with Film50 today, and unlock the world of cinema in a way that feels personal, organized, and endlessly entertaining. Enjoy exploring, tracking, and watching movies in a brand new way. This is the ultimate toolkit for movie lovers—built by movie lovers.

## Credits and Acknowledgments
- **TMDb API**: Movie data powered by [The Movie Database](https://www.themoviedb.org).
- **Python Libraries**: Big thanks to `requests`, `pyfiglet`, `tabulate`, and `json` for making Film50 smooth and feature-rich!

**Film50** - Because your movie choices should be as unique as your taste!
