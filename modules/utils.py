"""
============================================================
                UTILITY MODULE
============================================================

Description:
Contains helper functions.

============================================================
"""


def get_url():
    """Get website URL from user."""

    while True:

        url = input("\nEnter Website URL: ").strip()

        if url.startswith("http://") or url.startswith("https://"):
            return url

        print("\nInvalid URL!")
        print("Example: https://example.com")