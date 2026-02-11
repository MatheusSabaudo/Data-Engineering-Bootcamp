import requests

api_key = "2cfa7ad15ad224c023a84f5a980f6fda"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching data from the API...")
    try:

        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        print("Data fetched successfully!")
        return response.json()
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        raise

def mock_fetch_data():
    print("Mock fetching data...")
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-02-11 03:45', 'localtime_epoch': 1770781500, 'utc_offset': '-5.0'}, 'current': {'observation_time': '08:45 AM', 'temperature': 1, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:55 AM', 'sunset': '05:26 PM', 'moonrise': '02:57 AM', 'moonset': '11:39 AM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 36}, 'air_quality': {'co': '278.85', 'no2': '26.75', 'o3': '52', 'so2': '4.95', 'pm2_5': '27.25', 'pm10': '27.65', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 7, 'wind_degree': 248, 'wind_dir': 'WSW', 'pressure': 1006, 'precip': 0, 'humidity': 75, 'cloudcover': 75, 'feelslike': -2, 'uv_index': 0, 'visibility': 14, 'is_day': 'no'}}