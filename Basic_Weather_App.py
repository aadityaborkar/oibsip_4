import requests
import json

def get_weather_data(api_key, location):
  """Fetches current weather data for a specified location using an API.

  Args:
      api_key: Your OpenWeatherMap API key.
      location: The user-specified location (city or ZIP code, optionally with country code).

  Returns:
      A dictionary containing weather data or None if an error occurs.
  """

  url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric"  # Metric units

  # Check if a comma is present, indicating a possible ZIP code with country code
  if "," in location:
    zip_code, country_code = location.split(",")
    url += f"&zip={zip_code},{country_code}"  # Append ZIP code and country code parameters
  else:
    url += f"&q={location}"  # Append city name parameter

  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return None

def main():
  """Prompts user for location, fetches weather data, and displays result."""

  api_key = "4f120ddaa38a3d8c5fbc3da7f9ecada3"  
  location = input("Enter a city or ZIP code (optionally with country code): ")

  weather_data = get_weather_data(api_key, location)

  if weather_data:
    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    weather_description = weather_data["weather"][0]["description"]
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {weather_description}")
  else:
    print("Error: Could not retrieve weather data for that location.")

if __name__ == "__main__":
  main()
