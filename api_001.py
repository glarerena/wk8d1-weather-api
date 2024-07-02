import requests

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = "6033329bb661428aad001802240207"
CITY = "New York"

# Function to fetch current weather data
def get_current_weather(api_key, city):
    endpoint = f"{BASE_URL}/current.json"
    params = {
        "key": api_key,
        "q": city
    }
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    weather_data = get_current_weather(API_KEY, CITY)
    if weather_data:
        current = weather_data['current']
        temp_c = current['temp_c']
        humidity = current['humidity']
        wind_speed = current['wind_kph']
        condition = current['condition']['text']
        
        print(f"Current temperature in {CITY}: {temp_c}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} kph")
        print(f"Weather Condition: {condition}")
    else:
        print("Weather data retrieval failed.")
