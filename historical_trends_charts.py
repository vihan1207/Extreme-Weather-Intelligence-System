# Import required libraries for data processing and visualization
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate a historical weather trends chart
def generate_historical_chart():
    """
    Reads historical weather data from an Excel file and creates a line chart
    showing temperature and humidity trends over time.
    """
    try:
        # Define the path to the historical weather data file (CORRECTED: data instead of dat)
        file_path = "data/weather_history.xlsx"
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
        
        # Create a new figure with dimensions 12x7 inches for better visibility
        plt.figure(figsize=(12, 7))
        
        # Plot temperature data with circular markers and label (Column names are case-sensitive)
        plt.plot(df["Timestamp"], df["Temperature"], marker='o', label="Temperature")
        
        # Plot humidity data with circular markers and label (Column names are case-sensitive)
        plt.plot(df["Timestamp"], df["Humidity"], marker='o', label="Humidity")
        
        # Set the chart title and axis labels for clarity
        plt.title("Historical Weather Trends")
        plt.xlabel("Timestamp")
        plt.ylabel("Values")
        
        # Display legend to identify the plotted lines
        plt.legend()
        
        # Rotate x-axis labels by 45 degrees for better readability
        plt.xticks(rotation=45)
        
        # Automatically adjust layout to prevent label cutoff
        plt.tight_layout()
        
        # Save the chart as a PNG image in the reports folder
        plt.savefig("reports/historical_trends.png")
        
        # Display the chart in a window
        plt.show()
        
        # Print confirmation message
        print("Historical trends chart saved successfully")
        
    except FileNotFoundError:
        # Handle case where the Excel file is not found
        print(f"Error: File '{file_path}' not found. Please ensure the file exists in the correct location.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred while generating the chart: {str(e)}")

if __name__ == "__main__":
    # Call the function to generate the historical weather trends chart
    generate_historical_chart()    