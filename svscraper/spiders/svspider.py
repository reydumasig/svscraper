# svscraper/spiders/svspider.py

import scrapy
from datetime import datetime

class SvspiderSpider(scrapy.Spider):
    name = 'svspider'
    allowed_domains = ['ph.jobstreet.com']
    start_urls = ['https://ph.jobstreet.com/online-jobs']
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'FEEDS': {
            'output/jobs_%(time)s.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
                'overwrite': True,
                'fields': [
                    'title',
                    'company',
                    'location',
                    'salary',
                    'employment_type',
                    'posted_date',
                    'job_url',
                    'description_preview',
                    'scraped_date'
                ]
            },
        },
        'DOWNLOAD_DELAY': 2,
        'COOKIES_ENABLED': False
    }

    def parse(self, response):
        # Extract job listings
        job_listings = response.css('article[data-job-id]')
        self.logger.info(f'Found {len(job_listings)} job listings')
        
        for job in job_listings:
            yield {
                'title': self.clean_text(job.css('h1 a::text, h3 a::text').get()),
                'company': self.clean_text(job.css('[data-automation="job-card-company-name"] span::text').get()),
                'location': self.clean_text(job.css('[data-automation="job-card-location"]::text').get()),
                'salary': self.clean_text(job.css('[data-automation="job-card-salary"]::text').get()),
                'employment_type': self.clean_text(job.css('[data-automation="job-card-employment-type"]::text').get()),
                'posted_date': self.clean_text(job.css('time::attr(datetime)').get()),
                'job_url': response.urljoin(job.css('h1 a::attr(href), h3 a::attr(href)').get()),
                'description_preview': self.clean_text(job.css('[data-automation="job-card-description"]::text').get()),
                'scraped_date': datetime.now().isoformat()
            }

        # Follow pagination
        next_page = response.css('[data-automation="pagination-next-button"]::attr(href)').get()
        if next_page:
            self.logger.info(f'Following next page: {next_page}')
            yield response.follow(next_page, self.parse)

    def clean_text(self, text):
        """Clean extracted text by removing extra whitespace and None values"""
        if text is None:
            return ''  # Return empty string instead of None for CSV compatibility
        return ' '.join(text.strip().split())