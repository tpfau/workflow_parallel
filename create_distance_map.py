import pandas as pd
from geopy.geocoders import Nominatim


# Function to get latitude and longitude for a city using OpenStreetMap
def get_lat_long(city, country):
    geolocator = Nominatim(user_agent="city_locator")
    location = geolocator.geocode(f"{city}, {country}")

    if location:
        return location.latitude, location.longitude
    else:
        return None, None


# Read the CSV file into a pandas DataFrame
file_path = "Cities.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

# Add empty columns for latitude and longitude
df["Latitude"] = None
df["Longitude"] = None

# Iterate through each row and get latitude and longitude
for index, row in df.iterrows():
    city = row["Name"]
    country = row["Country"]
    latitude, longitude = get_lat_long(city, country)
    print(f"{city}/{country}/{latitude}/{longitude}")
    # Update the DataFrame with latitude and longitude
    df.at[index, "Latitude"] = latitude
    df.at[index, "Longitude"] = longitude

# Print the updated DataFrame
print(df)
