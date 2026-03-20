# import the required modules
import pandas as pd
import os

# Function to analyze weather trends based on historical data
# This function reads the historical weather data from an Excel file,
# compares the latest record with the previous one, and prints trends
# for temperature, humidity, wind speed, and pressure.
def analyze_trends():
    # Path to the historical weather data file (relative to the intelligence folder)
    file_path = os.path.join(os.path.dirname(__file__), "../data/weather_history.xlsx")
    
    # Load the historical data into a pandas DataFrame
    df = pd.read_excel(file_path)
    
    # Check if there are at least 2 records to compare trends
    if len(df) < 2:
        print("Not enough historical data to analyze trends.") 
        return
    
    # Get the most recent (latest) and the one before it (previous) records
    latest = df.iloc[-1]  # Last row in the DataFrame
    previous = df.iloc[-2]  # Second-to-last row
    
    # Print header for the trends analysis
    print("\nWeather Trends Intelligence")
    print("------------------------------")
    
    # Analyze temperature trend by comparing latest and previous values
    if latest["Temperature"] > previous["Temperature"]:
        print("Temperature is rising")
    elif latest["Temperature"] < previous["Temperature"]:
        print("Temperature is falling")
    else:
        print("Temperature is stable")
    
    # Analyze humidity trend
    if latest["Humidity"] > previous["Humidity"]:
        print("Humidity is increasing")
    elif latest["Humidity"] < previous["Humidity"]:
        print("Humidity is decreasing")
    else:
        print("Humidity is stable")
    
    # Analyze wind speed trends
    if latest["Wind_Speed"] > previous["Wind_Speed"]:
        print("Wind speed is increasing")        
    elif latest["Wind_Speed"] < previous["Wind_Speed"]:
        print("Wind speed is decreasing")
    else:
        print("Wind speed is stable")
    
    # Analyze pressure trends
    if latest["Pressure"] > previous["Pressure"]:
        print("Pressure is rising")
    elif latest["Pressure"] < previous["Pressure"]:
        print("Pressure is falling")
    else:
        print("Pressure is stable")

# Run the function if the script is executed directly
if __name__ == "__main__":
    analyze_trends()                            
