# import the required modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.weather_api import get_weather_data

def analyze_weather():
    weather = get_weather_data()
    alerts = []
    
    # Analyze temperature
    temp = weather["Temperature"]
    if temp > 35:
        alerts.append("Extreme Heat Alert")
    elif temp > 30:
        alerts.append("High Temperature Alert")
    elif temp < 0:
        alerts.append("Extreme Cold Alert")
    elif temp < 10:
        alerts.append("Cold Alert")
    
    # Analyze humidity
    humidity = weather["Humidity"]
    if humidity > 80:
        alerts.append("High Humidity Alert")
    elif humidity < 30:
        alerts.append("Low Humidity Alert")
    
    # Analyze wind speed
    wind_speed = weather["Wind_Speed"]
    if wind_speed > 10:
        alerts.append("Strong Wind Alert")
    
    # Analyze pressure (assuming normal is around 1013 hPa)
    pressure = weather["Pressure"]
    if pressure < 1000:
        alerts.append("Low Pressure Alert")
    elif pressure > 1020:
        alerts.append("High Pressure Alert")
    
    # Check weather condition for rain, storm, snow
    condition = weather.get("Weather_Condition", "").lower()
    if "rain" in condition:
        alerts.append("Rain Alert")
    if "storm" in condition or "thunder" in condition:
        alerts.append("Storm Alert")
    if "snow" in condition:
        alerts.append("Snow Alert")
    
    return weather, alerts

if __name__ == "__main__":
    weather, alerts = analyze_weather()
    print("Weather Data:", weather)
    print("Alerts:", alerts)