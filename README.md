# Genius Lyrics Scraper

This Python script utilizes the Genius API to retrieve song lyrics based on the provided song title and artist name. It employs the `requests` library to make API requests and `BeautifulSoup` for parsing HTML to extract lyrics from the Genius website.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. **Get Genius API Access Token:**
   Obtain a Genius API access token by registering on the [Genius API website](https://genius.com/developers) and create a new API client.

2. **Replace Access Token:**
   Replace the placeholder `access_token` in the script with your actual Genius API access token.

3. **Run the Script:**
   Execute the script, providing the song title, artist name, and the access token as parameters to the `get_lyrics` function.

   ```python
   get_lyrics("Song Title", "Artist Name", "Your Access Token")
   ```

   Example:
   ```python
   get_lyrics("Shape of You", "Ed Sheeran", "your_actual_access_token_here")
   ```

4. **Output:**
   The script will print the lyrics to the console.

## Note
- This script assumes that the first search result from the Genius API is the most relevant and extracts lyrics from the corresponding song URL.
- Ensure compliance with Genius API usage policies.

Feel free to enhance and customize the script based on your specific requirements.