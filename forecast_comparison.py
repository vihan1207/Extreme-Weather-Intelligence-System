# Import required modules
import sys
import os
import requests

# Ensure the project root directory is on sys.path when run as a script.
# This allows sibling packages like `api` to be imported reliably.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.weather_api import get_weather_data

# OpenWeatherMap API key (should ideally be stored in an environment variable)
API_KEY = "1d442088a64ea30591851f1c1c62ab38"


def compare_forecast():
    """Compare current weather against the next forecast entry.

    This function fetches the current weather via `get_weather_data()` (which uses
    the Geolocation + Current Weather API endpoint), then calls the OpenWeatherMap
    5-day/3-hour forecast endpoint and compares the first predicted temperature
    to the current temperature.

    The intent is to determine whether the temperature is expected to rise, fall,
    or remain stable in the near future.
    """

    # Get current weather data (includes city name and temperature)
    weather = get_weather_data()
    city = weather.get("City")

    # Build the forecast URL using the same city name (using the correct API endpoint)
    forecast_url = (
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}"
        f"&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(forecast_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # The OpenWeatherMap forecast API returns a list of 3-hour interval forecasts.
        # We use the first element to represent the 'next' forecast.
        forecast_temp = data["list"][0]["main"]["temp"]

    except requests.RequestException as exc:
        print(f"Failed to fetch forecast data: {exc}")
        return
    except (KeyError, IndexError) as exc:
        print(f"Unexpected forecast response format: {exc}")
        return

    current_temp = weather.get("Temperature")

    # Output a simple comparison of current vs forecast temperature
    print("\nForecast Comparison")
    print("----------------------")
    print(f"Current Temperature in {city}: {current_temp}°C")
    print(f"Forecasted Temperature in {city}: {forecast_temp}°C")

    # Generate a simple alert based on the comparison
    if forecast_temp > current_temp:
        print("Temperature is expected to rise.")
    elif forecast_temp < current_temp:
        print("Temperature is expected to drop.")
    else:
        print("Temperature is expected to remain stable.")


if __name__ == "__main__":
    compare_forecast()                

