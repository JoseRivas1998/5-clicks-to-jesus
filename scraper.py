import requests
from bs4 import BeautifulSoup
import re


excluded_links = ['wikipedia:community_portal', 'main_page']


def get_links(page):
    start_url = "https://en.wikipedia.org/wiki/" + page
    page = requests.get(start_url)
    if page.status_code != 200:
        return set()
    soup = BeautifulSoup(page.content, 'html.parser')
    a_tags = soup.find_all('a')
    links = set()
    for a_tag in a_tags:
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            file_m = re.match('/wiki/File:.*', href)
            if file_m is None:
                portal_m = re.match('/wiki/portal:.*', href)
                if portal_m is None:
                    wiki_pages_m = re.match('/wiki/(.*)', href)
                    if wiki_pages_m is None:
                        continue
                    url = wiki_pages_m.group(1).lower()
                    if url in excluded_links:
                        continue
                    if re.match('(wikipedia|category|special|help):.*', url) is None:
                        links.add(url)
    return links
