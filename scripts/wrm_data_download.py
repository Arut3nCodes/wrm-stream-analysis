from data_collector import collect_data, save_to_csv, append_to_csv
from wrm_data_processing import process_wrm_data
from datetime import datetime
import logging
import csv
from pathlib import Path

bike_data_api = "https://api.nextbike.net/maps/nextbike-live.json"


Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/collector.log",
                    level=logging.INFO,
                    format="[WRM] %(asctime)s[%(levelname)s] %(message)s")

def main():
    try:
        raw = collect_data(bike_data_api, {"city": 148})
        processed = process_wrm_data(raw)
        filename_raw = f"data/wrm/wrm_{datetime.now():%Y-%m-%d_%H-%M}_raw.csv"
        filename_processed = f"data/processed_wrm_data.csv"
        save_to_csv(raw, filename_raw)
        append_to_csv(filename_processed, processed)
        logging.info("Dane zebrane pomyślnie.")
    except Exception as e:
        logging.error(f"Pobranie danych zakończone porażką: {e}")

if __name__ == "__main__":
    main()