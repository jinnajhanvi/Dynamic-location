import requests
from geopy.geocoders import Nominatim

def get_location_by_ip():
    # Access IP-based geolocation
    ip_info = requests.get("https://ipinfo.io").json()
    lat, lon = ip_info['loc'].split(',')
    return float(lat), float(lon)

# Use function to get and print latitude and longitude
latitude, longitude = get_location_by_ip()
print(f"Latitude: {latitude}, Longitude: {longitude}")
