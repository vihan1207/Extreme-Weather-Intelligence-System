# import the required modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from intelligence.weather_intelligence import analyze_weather
import winsound
# Function to generate smart alerts based on weather conditions
def generate_smart_alerts():
    weather, alerts = analyze_weather()
    city = weather["City"]
    print("\nSMART WEATHER ALERTS")
    print("----------------------")
    if alerts:
        for alert in alerts:
            print(f"ALERT: {alert} in {city}")
            if "Heat" in alert or "Temperature" in alert:
                print("Advice: Stay hydrated and avoid direct sunlight.")
            elif "Humidity" in alert:
                print("Advice: Use a dehumidifier or stay in air-conditioned areas.")
            elif "Rain" in alert or "Storm" in alert:
                print("Advice: Carry an umbrella and avoid outdoor activities.")
            elif "Pressure" in alert:
                print("Advice: Be cautious if you have respiratory issues.") 
            elif "Snow" in alert or "Cold" in alert:
                print("Advice: Dress warmly and avoid prolonged exposure to cold.")
            if "Storm" in alert:
                winsound.Beep(2000, 1500)  # Additional beep for very strong alert
            else:
                winsound.Beep(1500, 1000)  # Beep sound for normal alert
    else:
        print("No major weather alerts at this time. Thank you")

if __name__ == "__main__":
    generate_smart_alerts() 

