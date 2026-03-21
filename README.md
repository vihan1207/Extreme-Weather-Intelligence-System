# Extreme-Weather-Intelligence-System
A modular Python-based weather intelligence system designed to detect live weather conditions, analyze extreme environmental patterns, generate smart alerts, store historical weather records, and produce visual reports automatically.

Project Overview:
This project integrates live weather APIs, location detection, analytical intelligence, alert generation, and historical logging into one structured system.
The system automatically detects  the User's live city, fetches real-time weather data, analyzes risk conditions, compares forecast trends, and generates reports for weather monitoring.

Core Features: 
1. Live location detection using IP-based location services.
2. Real-time weather data collection using weather API.
3. Extreme weather condition analysis.
4. Forecast comparison intelligence.
5. Historical weather trend analyis.
6. Smart weather alert generation with sound alerts.
7. Automatic Excel weather logging.
8. Weather chart generation.
9. Daily text-based weather reporting.

Project Architecture:
location/
Contains location detection logic.
 •detect_location.py -> Detects current city, region, country, timezones, and coordinates.

api/ 
Handels external weather API communication.
 •weather_api.py -> Fetches live weather data.

intelligence/
Contains analytical weather intelligence modules.
 •weather_intelligence.py -> Detects extreme weather situations.
 •Forecast_comparison.py -> Compares current and forecasted conditions.
 •trend_analysis.py -> Analyzes historical weather patterns.

alerts/
Smart alert engine.
 •smart_alerts.py -> Generates alert messages and "Beep" sound notifications.

data/
Stores generated weather records.
 •live_weather_data.xlsx -> Historical weather storage.

reports/
Stores generated weather reports.
 •daily_report.py -> Creates daily reports.
 •daily_weather_report.txt -> Generated report output.

visualization/
