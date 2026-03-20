#import the required modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.weather_api import get_weather_data
import matplotlib.pyplot as plt

# Function to visualize weather data
def generate_weather_charts():
    weather = get_weather_data()
    # Create a bar chart for temperature, humidity, wind speed, and pressure
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Pressure (hpa)']
    values = [
        weather["Temperature"],
        weather["Humidity"],
        weather["Wind_Speed"],
        weather["Pressure"]
    ]
    plt.figure(figsize=(10, 9))
    plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
    plt.title(f"Live Weather Data for {weather['City']}")
    plt.ylabel("Values")
    plt.savefig("reports/weather_chart.png")
    plt.show()
    print("Weather chart saved successfully")

if __name__ == "__main__":
    generate_weather_charts()

