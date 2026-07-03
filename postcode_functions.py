"""Functions that interact with the Postcode API."""

import requests as req
import os
import json

CACHE_FILE = "./postcode_cache.json"


def load_cache() -> dict:
    """Loads the cache from a file and converts it from JSON to a dictionary."""
    # This function is used in Task 3, you can ignore it for now.
    ...


def save_cache(cache: dict):
    """Saves the cache to a file as JSON"""
    # This function is used in Task 3, you can ignore it for now.
    ...


def validate_postcode(postcode: str) -> bool:

    if not isinstance(postcode, str):
        raise TypeError("Function expects a string.")

    res = req.get(f"https://api.postcodes.io/postcodes/{postcode}/validate")

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")

    if res.status_code == 200:

    return False


def get_postcode_for_location(lat: float, long: float) -> str:
    if not isinstance(lat, float) or not isinstance(long, float):
        raise TypeError("Function expects two floats.")

    res = req.get(f"https://api.postcodes.io/postcodes?lon={long}&lat={lat}")

    if res.status_code == 200:
        res_json = res.json()["result"]
        if res_json == None:
            raise ValueError("No relevant postcode found.")
        return res_json[0]["postcode"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")


def get_postcode_completions(postcode_start: str) -> list[str]:
    if not isinstance(postcode_start, str):
        raise TypeError("Function expects a string.")
    res = req.get(
        f"https://api.postcodes.io/postcodes/{postcode_start}/autocomplete")

    if res.status_code == 200:
        return res.json()["result"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")


def get_postcodes_details(postcodes: list[str]) -> dict:

    if not isinstance(postcodes, list):
        raise TypeError("Function expects a list of strings.")

    for postcode in postcodes:
        if not isinstance(postcode, str):
            raise TypeError("Function expects a list of strings.")

    res = req.post(f"https://api.postcodes.io/postcodes")
    if res.status_code == 200:
        return res.json()["result"]

    if res.status_code == 500:
        raise req.RequestException("Unable to access API.")


if __name__ == "__main__":
    print(get_postcode_for_location(51.507, -0.127))
