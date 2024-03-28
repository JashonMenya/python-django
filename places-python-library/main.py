from googleapiclient.discovery import build
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
    if not places_result['results']:
        print("No places found ")
    return places_result['results']

def process_and_print_places(places):
    """Processes and prints out places."""
    for place in places:
        print(f"Name: {place['name']}, Visinity: {place['vicinity']}")


def geocode_location(gmaps, location_name):
    """Geocodes a location name to latitude and longitude coordinates.
    
    Args:
        gmaps: Initialized Google Maps client.
        location_name: The name of the location to geocode.
        
    Returns:
        A tuple of (latitude, longitude) coordinates if successful, None otherwise.
    """
    geocode_result = gmaps.geocode(location_name)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    else:
        print(f"Could not geocode the location: {location_name}")
        return None



def main():
    api_key = load_api_key()
    if not api_key:
        print("API key is not set. Please check your .env file.")
        return

    gmaps = initialize_gmaps(api_key)

    # Simulating user input for a destination
    destination_name = "Rosemount"  # Replace with any destination you'd like to test
    
    # Geocoding the destination to get coordinates
    location = geocode_location(gmaps, destination_name)
    if not location:
        return  # Exit if geocoding was unsuccessful

    places = search_places_nearby(gmaps, location)
    process_and_print_places(places)

if __name__ == "__main__":
    main()
