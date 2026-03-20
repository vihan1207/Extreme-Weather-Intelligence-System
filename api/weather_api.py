#import the required modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from location.detect_location import get_current_location
import pandas as pd
from datetime import datetime
API_Key="1d442088a64ea30591851f1c1c62ab38"
def get_weather_data():
    city, region, country, loc, postal, timezone = get_current_location()
    lat, lon = loc.split(',')
    URL=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&units=metric"
    response=requests.get(URL)
    data=response.json()

    weather_info={"City":city,
                  "Region":region,
                  "Country":country,
                  "Location":loc,
                  "Postal Code":postal,
                  "Timezone":timezone,
                  "Temperature":data["main"]["temp"],
                  "Feels like":data["main"]["feels_like"],
                  "Humidity":data["main"]["humidity"],
                  "Pressure":data["main"]["pressure"],
                  "Wind_Speed":data["wind"]["speed"],
                  "Weather_Condition":data["weather"][0]["description"]
                  }
    return weather_info
if __name__=="__main__":
    weather=get_weather_data()
    print("\nWeather Information") 
    print("---------------------")
    for key, value in weather.items():
        print(f"{key}:{value}")

    timestamp= datetime.now()
    df=pd.DataFrame([{"Timestamp":timestamp, **weather}])
    df.to_excel("data/live_weather_data.xlsx", index=False)
    print("\nWeather data saved successfully")
