# JobStreet Scraper

A web scraper built with Scrapy to extract job listings from JobStreet Philippines.

## Features

- Extracts job titles, companies, locations, and other details
- Saves data in CSV format
- Includes pagination handling
- Respects robots.txt and implements polite scraping

## Installation

```bash
# Clone the repository
git clone [your-repository-url]
cd svscraper

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Unix or MacOS
# or
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run the spider
scrapy crawl svspider

# The output will be saved in the output directory as a CSV file
```

## Project Structure

```
svscraper/
├── scrapy.cfg
└── svscraper/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        ├── __init__.py
        └── svspider.py
```

## Configuration

You can modify the scraping behavior in `settings.py`:
- Adjust crawl speed with `DOWNLOAD_DELAY`
- Configure output format in `FEEDS`
- Set custom User-Agent

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.