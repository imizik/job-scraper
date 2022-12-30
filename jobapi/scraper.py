from bs4 import BeautifulSoup
import requests

class Scraper: 
    def __init__(self) -> None:
        pass

    def get_jobs(self): 
        ids = set()
        for page in range (5):
            source = requests.get(f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=softwareengineer&location=&start={page}&f_TPR=r86400')
            soup = BeautifulSoup(source.text, 'html.parser') 
            job_list = soup.find_all('div', class_='base-card')
            for x in job_list:
                post_id = x['data-entity-urn']
                ids.add(post_id.split(':')[3])
        
        return ids

x = Scraper()
print(x.get_jobs())
