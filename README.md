# ReadMe.md

## Lyrics Retrieval Using Genius API

This Python script leverages the Genius API to search for and retrieve lyrics for a given song title and artist. The Genius API provides a vast database of song lyrics and associated information.

### Prerequisites

- **Requests**: Ensure you have the Requests library installed. If not, you can install it using:
  ```bash
  pip install requests
  ```

- **Beautiful Soup**: Make sure you have the Beautiful Soup library installed. If not, you can install it using:
  ```bash
  pip install beautifulsoup4
  ```

### Usage

1. **Genius API Access Token**: You need to obtain a Genius API access token. Visit the [Genius API documentation](https://docs.genius.com/) to get your access token.

2. **Set Access Token**: Replace `'your_access_token_here'` in the script with your actual Genius API access token.
   ```python
   access_token = 'your_access_token_here'
   ```

3. **Run the Script**: Execute the script using a Python interpreter:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your Python script file.

4. **Provide Song Title and Artist**: The script prompts you to enter the song title and artist name. It then searches for the lyrics using the Genius API.

### Code Explanation

- **Import Libraries**:
  ```python
  import requests
  from bs4 import BeautifulSoup
  ```

- **Genius API Endpoint**:
  ```python
  api_url = "https://api.genius.com/search"
  ```

- **Make API Request**:
  The script constructs a request to the Genius API to search for the lyrics based on the provided song title and artist name.

- **Extract Song URL**:
  The first search result's URL is extracted from the JSON response, assuming it is the most relevant. A second request is then made to get the full lyrics from the song URL.

- **Extract Lyrics using BeautifulSoup**:
  The HTML content of the song URL is parsed using BeautifulSoup, and the lyrics are extracted. The script specifically looks for text between `<br>` tags in the HTML, assuming they denote line breaks in the lyrics.

- **Error Handling**:
  The script includes error handling to manage cases where the API requests fail, providing information about the status code.

### Notes

- Ensure you have the necessary permissions to use the Genius API and comply with their terms of service.

- Adjust the script based on changes in the Genius API or your specific requirements.

- Note that web scraping lyrics from a website is subject to the website's terms of service. Ensure compliance with Genius's terms.
