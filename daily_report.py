# Import necessary modules for weather data retrieval, analysis, and date/time handling
import os  # For file path operations
import sys  # For system path manipulation

# Add the project root directory to sys.path to enable imports from sibling modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from intelligence.weather_intelligence import analyze_weather  # Function to analyze weather and get alerts
from datetime import datetime  # For timestamp generation

# Function to generate and save a daily weather report
def generate_daily_report():
    """
    Generates a daily weather report by analyzing current weather data and alerts,
    then saves the formatted report to a text file.

    This function demonstrates integration of weather intelligence modules,
    data formatting, and file I/O operations in Python.
    """
    try:
        # Retrieve analyzed weather data and alerts from the intelligence module
        weather, alerts = analyze_weather()

        # Generate a formatted timestamp for the report
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a formatted report string using f-string for readability
        report = f"""Daily Weather Report
----------------------------------
Timestamp: {timestamp}
City: {weather['City']}
Temperature: {weather['Temperature']}°C
Humidity: {weather['Humidity']}%
Wind Speed: {weather['Wind_Speed']} m/s
Pressure: {weather['Pressure']} hPa
Weather Condition: {weather['Weather_Condition']}
Alerts: {", ".join(alerts) if alerts else "No Alerts"}
"""

        # Construct the file path relative to the script's directory for robustness
        report_file_path = os.path.join(os.path.dirname(__file__), "daily_weather_report.txt")

        # Save the report to a file in write mode
        with open(report_file_path, "w") as file:
            file.write(report)

        # Confirm successful save to the user
        print("Daily report saved successfully.")

    except KeyError as e:
        # Handle missing keys in weather data dictionary
        print(f"Error: Missing expected weather data key - {e}")
    except Exception as e:
        # General error handling for robustness
        print(f"An error occurred while generating the report: {e}")

# Main execution block to run the function when script is executed directly
if __name__ == "__main__":
    generate_daily_report()


