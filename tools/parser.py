from bs4 import BeautifulSoup as soup


def googleParser(html_code):
    print('Parsing Google HTML...')
    page_soup = soup(html_code, 'html.parser')
    job_items = page_soup.find_all('li', {'class': 'iFjolb gws-plugins-horizon-jobs__li-ed'})

    jobs_desc = []
    for job in job_items:
        jobs_desc.append({
            'Title': job.findChildren('div', {'class': 'BjJfJf PUpOsf'})[0].text,
            'Location': job.findChildren('div', {'class': 'Qk80Jf'})[0].text,
            'Company': job.findChildren('div', {'class': 'vNEEBe'})[0].text
        })
    
    return jobs_desc


def linkedinParser(html_code):
    print('Parsing LinkedIn HTML...')
    page_soup = soup(html_code, 'html.parser')
    job_list = page_soup.find_all('ul', {'class': 'jobs-search__results-list'})
    job_items = job_list[0].findChildren('div', {'class': 'base-search-card__info'})

    jobs_desc = []
    for job in job_items:
        jobs_desc.append({
            'Title': job.findChildren('h3', {'class': 'base-search-card__title'})[0].text.strip().replace('\n', '').strip(),
            'Location': job.findChildren('span', {'class': 'job-search-card__location'})[0].text.strip().replace('\n', '').strip(),
            'Company': job.findChildren('h4', {'class': 'base-search-card__subtitle'})[0].text.strip().replace('\n', '').strip()
        })


    return jobs_desc


def indeedParser(html_code):
    print('Parsing Indeed HTML...')
    page_soup = soup(html_code, 'html.parser')
    job_items = page_soup.find_all('td', {'class': 'resultContent'})

    job_desc = []
    for job in job_items:
        job_desc.append({
            'Title': job.findChildren('h2', {'class': 'jobTitle'})[0].text,
            'Location': job.findChildren('div', {'class': 'companyLocation'})[0].text,
            'Company': job.findChildren('span', {'class': 'companyName'})[0].text
        })

    return job_desc