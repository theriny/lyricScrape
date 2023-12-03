import requests
from bs4 import BeautifulSoup

def get_lyrics(song_title, artist_name, access_token):
    # Define the API endpoint for searching lyrics
    api_url = "https://api.genius.com/search"
    
    # Construct the query parameters
    params = {'q': f'{song_title} {artist_name}'}
    
    # Include the access token in the request headers
    headers = {'Authorization': 'Bearer ' + access_token}
    
    # Make the API request
    response = requests.get(api_url, params=params, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the URL of the first search result (assuming it's the most relevant)
        if data['response']['hits']:
            first_hit = data['response']['hits'][0]
            song_url = first_hit['result']['url']
            
            # Now, make a second request to get the full lyrics from the song URL
            lyrics_response = requests.get(song_url)
            
            # Check if the request was successful (status code 200)
            if lyrics_response.status_code == 200:
                
                # Parse the HTML to extract the lyrics using BeautifulSoup
                soup = BeautifulSoup(lyrics_response.text, 'html.parser')
                
                # Find all 'a' tags with 'href' attribute
                br_tags = soup.find_all('br')

               # Extract text between <br> tags
                results = []
                for br_tag in br_tags:
                    # Use next_sibling to get the text following the <br> tag
                    text_between_br_tags = br_tag.find_next(text=True) 
                    if text_between_br_tags:
                        print(text_between_br_tags.strip())
                        results.append(text_between_br_tags)

                return results
            else:
                print(f"Failed to get lyrics. Status code: {lyrics_response.status_code}")
                
    else:
        print(f"Failed to search for the song. Status code: {response.status_code}")