import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

from crawling.requests_intro import HEADERS

OUT = Path('crawling/titles.csv')
URL = 'https://example.com/'

def fetch_html():
    try:
        r = requests.get(URL, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.RequestException as err:
        print('크롤링 실패', err)
        return ''

def extract_titles(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    titles = [h.get_text(strip=True) for h in soup.find_all('h1')]
    if not titles:
        titles = ['(샘플) Example Domain']
    return titles

def save_csv(titles):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['title'])
        for t in titles:
            w.writerow([t])

def run():
    html = fetch_html()
    titles = extract_titles(html)
    save_csv(titles)
    print('saved', len(titles))

if __name__ == '__main__':
    run()

def load_saved():
    if not OUT.exists():
        return []
    with OUT.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

# 셀렉터 수정 메모 — h1 말고 a 태그도 시도
def extract_links(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get('href') for a in soup.find_all('a')[:5]]
