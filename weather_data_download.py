from data_collector import collect_data, save_to_csv, append_to_csv
from owa_data_processing import process_owa_data
from datetime import datetime
import logging
import csv
import os
from pathlib import Path

lat, lon = 51.1, 17.0333 # Coordinates for Wrocław
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


weather_data_api = "https://api.openweathermap.org/data/3.0/onecall"


Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/collector.log",
                    level=logging.INFO,
                    format="[OWA] %(asctime)s [%(levelname)s] %(message)s")

def main():
    try:
        raw = collect_data(weather_data_api, {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"})
        processed = process_owa_data(raw)
        filename_raw = f"data/owa/owa_{datetime.now():%Y-%m-%d_%H-%M}_raw.csv"
        filename_processed = f"data/owa_processed_data.csv"
        save_to_csv(raw, filename_raw)
        append_to_csv(filename_processed, processed)
        logging.info("Dane zebrane pomyślnie.")
    except Exception as e:
        logging.error(f"Pobranie danych zakończone porażką: {e}")

if __name__ == "__main__":
    main()