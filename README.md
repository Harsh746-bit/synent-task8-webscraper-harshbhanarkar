# Web Scraper (CLI)

A Python Command-Line Interface (CLI) application that extracts useful information from a website by scraping its HTML content. The application fetches webpage details such as the title, meta description, headings, links, and images, and saves the extracted information to a text file.

---

## Project Objective

The objective of this project is to understand the fundamentals of web scraping using Python. It demonstrates how to retrieve webpage content, parse HTML, extract useful information, and store the results in a structured format.

---

## Features

- Extract website title
- Extract meta description
- Display H1 headings
- Display H2 headings
- Count total links
- Count total images
- Save extracted information to a text file
- Handle invalid URLs
- Handle connection and timeout errors
- Menu-driven Command Line Interface

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4

---

## Project Structure

```
synent-task8-webscraper/
│
├── assets/
├── docs/
├── modules/
│   ├── __init__.py
│   ├── menu.py
│   ├── parser.py
│   ├── scraper.py
│   └── utils.py
│
├── output/
│   └── scraped_data.txt
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Harsh746-bit/synent-task8-webscraper-harshbhanarkar.git
```

Navigate to the project directory:

```bash
cd synent-task8-webscraper-harshbhanarkar
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Execute the following command:

```bash
python main.py
```

---

## Sample Workflow

1. Launch the application.
2. Select **Scrape Website**.
3. Enter a valid website URL.
4. The application downloads and parses the webpage.
5. Extracted information is displayed on the terminal.
6. The results are saved to `output/scraped_data.txt`.

---

## Sample Output

```
============================================================
             WEBSITE INFORMATION
============================================================

Title          : Example Domain
Description    : Example website used for testing.
Total Links    : 1
Total Images   : 0

H1 Headings
------------------------------
Example Domain

H2 Headings
------------------------------
None

Information saved to output/scraped_data.txt
```

---

## Screenshots

### Home Screen

```
assets/home.png
```

### Website Input

```
assets/website_input.png
```

### Extracted Output

```
assets/output.png
```

### Saved Output File

```
assets/saved_file.png
```

---

## Error Handling

The application handles the following scenarios:

- Invalid website URL
- Connection failure
- Request timeout
- HTTP errors
- Inaccessible websites

---

## Future Enhancements

- Export extracted information to CSV
- Export extracted information to JSON
- Extract tables from webpages
- Scrape multiple webpages
- Keyword-based content extraction

---

## Learning Outcomes

- Working with HTTP requests
- HTML parsing using BeautifulSoup
- File handling in Python
- Modular programming
- Exception handling
- Command-Line Interface development

---

## Internship

This project was developed as part of the **Synent Technologies Python Development Internship Program**.

---

## Developer

**Harsh Bhanarkar**

GitHub: https://github.com/Harsh746-bit
