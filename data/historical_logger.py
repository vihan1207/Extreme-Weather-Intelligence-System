# import the required modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.weather_api import get_weather_data
from intelligence.weather_intelligence import analyze_weather
import pandas as pd 
from datetime import datetime
# Function to log historical weather data
def save_historical_data():
    weather, alerts= analyze_weather()
    timestamp= datetime.now() 
    record= {
        "Timestamp": timestamp,
        "City": weather["City"],
        "Temperature": weather["Temperature"],
        "Humidity": weather["Humidity"],
        "Wind_Speed": weather["Wind_Speed"],
        "Pressure": weather["Pressure"],
        "Weather_condition": weather["Weather_Condition"],
        "Alerts": ", ".join(alerts) if alerts else "No Alerts"
    }
    # Check if the file exists, if not create a new DataFrame
    file_path= os.path.join(os.path.dirname(__file__), "weather_history.xlsx")
    if os.path.exists(file_path):
        existing_df= pd.read_excel(file_path)
        new_df= pd.concat([existing_df, pd.DataFrame([record])], ignore_index=True) 
    else: 
        new_df= pd.DataFrame([record])
    # Save the DataFrame to an Excel file
    new_df.to_excel(file_path, index=False)
    print("\nHistorical weather record saved successfully.")
    print(new_df.tail())
if __name__=="__main__":
    save_historical_data()        
