"""Functions that interact with the Postcode API."""

import os
import json
import requests as req

CACHE_FILE = "./postcode_cache.json"


def load_cache() -> dict:
    """Loads the cache from a file and converts it from JSON to a dictionary."""
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r") as file:
        return json.load(file)


def save_cache(cache: dict):
    """Saves the cache to a file as JSON"""
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def validate_postcode(postcode: str) -> bool:
    """Validates provided postcode."""

    if not isinstance(postcode, str):
        raise TypeError("Function expects a string.")

    data = load_cache()
    if postcode in data:
        return data[postcode]["valid"]

    res = req.get(
        f"https://api.postcodes.io/postcodes/{postcode}/validate", timeout=10)

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")

    if res.status_code == 200:
        data[postcode] = {"valid": res.json()["result"]}
        save_cache(data)
        return res.json()["result"]

    return None


def get_postcode_for_location(lat: float, long: float) -> str:
    """Gets the nearest postcode for a provided latitude and longitude."""

    if not isinstance(lat, float) or not isinstance(long, float):
        raise TypeError("Function expects two floats.")

    res = req.get(
        f"https://api.postcodes.io/postcodes?lon={long}&lat={lat}", timeout=10)

    if res.status_code == 200:
        res_json = res.json()["result"]
        if res_json is None:
            raise ValueError("No relevant postcode found.")
        return res_json[0]["postcode"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")

    return None


def get_postcode_completions(postcode_start: str) -> list[str]:
    """Gets postcode completions."""

    if not isinstance(postcode_start, str):
        raise TypeError("Function expects a string.")

    data = load_cache()

    res = req.get(
        f"https://api.postcodes.io/postcodes/{postcode_start}/autocomplete", timeout=10)

    if res.status_code == 200:
        data[postcode_start] = {"completions": res.json()["result"]}
        save_cache(data)
        return res.json()["result"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")

    return None


def get_postcodes_details(postcodes: list[str]) -> dict:
    """Gets details for provided postcodes."""

    if not isinstance(postcodes, list):
        raise TypeError("Function expects a list of strings.")

    for postcode in postcodes:
        if not isinstance(postcode, str):
            raise TypeError("Function expects a list of strings.")

    res = req.post("https://api.postcodes.io/postcodes", timeout=10)
    if res.status_code == 200:
        return res.json()["result"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")
    return None


if __name__ == "__main__":
    print(get_postcode_for_location(51.507, -0.127))
