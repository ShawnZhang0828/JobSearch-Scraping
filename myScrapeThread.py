import threading
from tools import scraper

class Scraper():
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def run(self, threadLock):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        page_html = self.scrape()
        threadLock.release()
        print("Exiting: " + self.name + "\n")
        
        return page_html

    def scrape(self):
        lower_url = self.url.lower()
        if self.name == "LinkedIn":
            print('Extracting LinkedIn HTML...')
            return scraper.linkedinExtractor(self.url)
        elif self.name == "Google":
            print('Extracting Google HTML...')
            return scraper.googleExtractor(self.url)
        elif self.name == "Indeed":
            print('Extracting Indeed HTML...')
            return scraper.indeedExtractor(self.url)
        else:
            raise Exception("Sorry, please provide a valid url.")        

    
