"""
============================================================
                    WEB SCRAPER
============================================================

Developer : Harsh Bhanarkar
Internship: Synent Technologies

Description:
A CLI application that extracts website information
using Requests and BeautifulSoup.

============================================================
"""

from modules.menu import (
    display_header,
    display_main_menu,
    display_about,
    display_exit
)

from modules.utils import get_url
from modules.scraper import fetch_website
from modules.parser import parse_html


def scrape_website():
    """Perform website scraping."""

    url = get_url()

    html = fetch_website(url)

    if html:
        parse_html(html)

    input("\nPress Enter to continue...")


def main():
    """Main application."""

    while True:

        display_header()
        display_main_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            scrape_website()

        elif choice == "2":
            display_about()
            input("\nPress Enter to continue...")

        elif choice == "3":
            display_exit()
            break

        else:
            print("\nInvalid choice!")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()