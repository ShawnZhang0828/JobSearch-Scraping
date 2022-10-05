import time
from myScrapeThread import Scraper
import multiprocessing
from tools.parser import linkedinParser, googleParser, indeedParser
from tools import displayer


results = []


def worker(url):
    if "linkedin" in url:
        scraper = Scraper("LinkedIn", url)
        return linkedinParser(scraper.scrape())
    elif "google" in url:
        scraper = Scraper("Google", url)
        return googleParser(scraper.scrape())
    elif "indeed" in url:
        scraper = Scraper("Indeed", url)
        return indeedParser(scraper.scrape())
    else:
        pass


def main():
    linkedin_url = 'https://ca.linkedin.com/jobs/software-engineer-intern-jobs?position=1&pageNum=0'
    google_url = 'https://www.google.com/search?q=2023+software+engineering+internships&rlz=1C1CHBF_enCA864CA864&oq=2023+software+en&aqs=chrome.0.0i512j0i457i512j0i512l2j69i57j0i512l2j69i61.4910j0j4&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwi7m_vam4b6AhWekYkEHRX6CskQutcGKAF6BAgEEAY&sxsrf=ALiCzsYPZdwAlhIP1hAEQfjTuBVDe-wQKQ:1662675178151#htivrt=jobs&htidocid=01hG917poF0AAAAAAAAAAA%3D%3D&fpstate=tldetail'
    urls = [f'https://ca.indeed.com/jobs?q=software+engineer+intern&l=On&start={i*10}' for i in range(7)]
    urls.append(linkedin_url)
    urls.append(google_url)

    # initialize a pool with size of 5
    pool = multiprocessing.Pool(processes=5)
    results = pool.map(worker, urls)

    pool.terminate()
    pool.join()

    displayer.display(results)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
