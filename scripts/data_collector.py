import requests
import csv
from pathlib import Path

def collect_data(api_url, params=None):
    """
    Collect data from the specified API endpoint.

    Args:
        api_url (str): The URL of the API endpoint.
        params (dict, optional): Query parameters to include in the request.

    Returns:
        dict: The JSON response from the API if the request is successful.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Wystąpił błąd: {e}")
        return None


def save_to_csv(data, filepath):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    write_header = not Path(filepath).exists()

    with open(filepath, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerow(data)

def append_to_csv(filepath, data):
    """
    Appends one or more dictionaries as rows to a CSV file.
    Automatically writes the header if the file is new.
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    file_exists = Path(filepath).exists()

    # Normalize input: if it's a single dict, wrap it in a list
    if isinstance(data, dict):
        data = [data]

    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

