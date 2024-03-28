from googleapiclient.discovery import build
import google.auth
import googlemaps
from dotenv import load_dotenv
import os

def load_api_key():
    """Loads the API key from an environment variable."""
    load_dotenv()
    return os.environ.get("API_KEY")

def initialize_gmaps(api_key):
    """Initializes the Google Maps client with an API key."""
    return googlemaps.Client(api_key)

def search_places_nearby(gmaps, location, radius=1000, place_type='tourist_attraction'):
    """Searches for places nearby a given location.
    
    Args:
        gmaps: Initialized Google Maps client.
        location: A tuple of (latitude, longitude).
        radius: Search radius in meters.
        place_type: Type of place to search for.
        
    Returns:
        A list of places found near the location.
    """
    places_result = gmaps.places_nearby(location=location, radius=radius, type=place_type)
    return places_result['results']

def process_and_print_places(places):
    """Processes and prints out places."""
    for place in places:
        print(f"Name: {place['name']}, Location: {place['geometry']['location']}")

def main():
    api_key = load_api_key()
    if not api_key:
        print("API key is not set. Please check your .env file.")
        return

    gmaps = initialize_gmaps(api_key)

    # Example location: Paris, France
    location = (48.8566, 2.3522)
    
    places = search_places_nearby(gmaps, location)
    process_and_print_places(places)

if __name__ == "__main__":
    main()
