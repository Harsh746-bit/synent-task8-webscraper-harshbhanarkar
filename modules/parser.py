"""
============================================================
                    PARSER MODULE
============================================================

Description:
Extracts information from HTML content.

Developer : Harsh Bhanarkar
Internship: Synent Technologies

============================================================
"""

from bs4 import BeautifulSoup
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "output" / "scraped_data.txt"

def parse_html(html):

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title else "Not Available"

    description = "Not Available"

    meta = soup.find("meta", attrs={"name": "description"})

    if meta and meta.get("content"):
        description = meta["content"]

    h1 = [tag.get_text(strip=True) for tag in soup.find_all("h1")]

    h2 = [tag.get_text(strip=True) for tag in soup.find_all("h2")]

    links = len(soup.find_all("a"))

    images = len(soup.find_all("img"))

    print("\n" + "=" * 60)
    print("             WEBSITE INFORMATION")
    print("=" * 60)

    print(f"Title          : {title}")
    print(f"Description    : {description}")
    print(f"Total Links    : {links}")
    print(f"Total Images   : {images}")

    print("\nH1 Headings")
    print("-" * 30)

    if h1:
        for heading in h1:
            print(heading)
    else:
        print("None")

    print("\nH2 Headings")
    print("-" * 30)

    if h2:
        for heading in h2:
            print(heading)
    else:
        print("None")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write(f"Title : {title}\n")
        file.write(f"Description : {description}\n")
        file.write(f"Total Links : {links}\n")
        file.write(f"Total Images : {images}\n\n")

        file.write("H1 Headings\n")

        for heading in h1:
            file.write(f"- {heading}\n")

        file.write("\nH2 Headings\n")

        for heading in h2:
            file.write(f"- {heading}\n")

    print(f"\nInformation saved to:\n{OUTPUT_FILE}")