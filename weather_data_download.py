from data_collector import collect_data, save_to_csv, append_to_csv
from owa_data_processing import process_owa_data
from datetime import datetime
import logging
import os
from pathlib import Path

# Coordinates for Wrocław
lat, lon = 51.1, 17.0333
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

weather_data_api = "https://api.openweathermap.org/data/3.0/onecall"

# Create directories if they don't exist
Path("logs").mkdir(exist_ok=True)
Path("data/owa").mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/collector.log",
    level=logging.INFO,
    format="[OWA] %(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("Starting data collection script.")

    # Check API key
    if not API_KEY:
        logging.error("OPENWEATHERMAP_API_KEY is not set!")
        return
    logging.info("API key found.")

    try:
        logging.info(f"Requesting data from {weather_data_api} for lat={lat}, lon={lon}")
        raw = collect_data(weather_data_api, {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"})
        
        if raw is None:
            logging.error("collect_data returned None. Aborting processing.")
            return
        logging.info("Data successfully collected from API.")
        logging.debug(f"Raw data: {raw}")

        logging.info("Processing raw data...")
        processed = process_owa_data(raw)
        if processed is None:
            logging.warning("process_owa_data returned None. Nothing to append.")
        else:
            logging.info("Data successfully processed.")
            logging.debug(f"Processed data: {processed}")

        # Prepare filenames
        filename_raw = f"data/owa/owa_{datetime.now():%Y-%m-%d_%H-%M}_raw.csv"
        filename_processed = f"data/owa_processed_data.csv"

        logging.info(f"Saving raw data to {filename_raw}")
        save_to_csv(raw, filename_raw)

        if processed:
            logging.info(f"Appending processed data to {filename_processed}")
            append_to_csv(filename_processed, processed)

        logging.info("Data collection and processing completed successfully.")

    except Exception as e:
        logging.exception(f"Data collection failed: {e}")

if __name__ == "__main__":
    main()
