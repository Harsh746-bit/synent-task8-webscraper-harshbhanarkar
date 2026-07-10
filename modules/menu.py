"""
============================================================
                    WEB SCRAPER
============================================================

Developer : Harsh Bhanarkar
Internship: Synent Technologies

Description:
Displays the application menus.

============================================================
"""


def display_header():
    """Display application header."""

    print("\n" + "=" * 60)
    print("                 WEB SCRAPER")
    print("=" * 60)
    print("     Website Information Extractor")
    print("=" * 60)


def display_main_menu():
    """Display the main menu."""

    print("\nMain Menu")
    print("-" * 25)
    print("1. Scrape Website")
    print("2. About")
    print("3. Exit")


def display_about():
    """Display project information."""

    print("\nProject Information")
    print("-" * 25)
    print("Project    : Web Scraper")
    print("Developer  : Harsh Bhanarkar")
    print("Internship : Synent Technologies")
    print("Language   : Python")
    print("Version    : 1.0")


def display_exit():
    """Display exit message."""

    print("\nThank you for using Web Scraper.")
    print("Goodbye!")