"""
============================================================
                    SCRAPER MODULE
============================================================

Description:
Fetches HTML content from a website.

Developer : Harsh Bhanarkar
Internship: Synent Technologies

============================================================
"""

import requests


def fetch_website(url):
    """
    Fetch website HTML content.
    """

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.text

    except requests.exceptions.ConnectionError:
        print("\nNo internet connection.")

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.HTTPError:
        print("\nWebsite returned an error.")

    except requests.exceptions.RequestException:
        print("\nInvalid URL or unable to access website.")

    return None