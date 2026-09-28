from bs4 import BeautifulSoup

SAMPLE = '''
<html><body><h1>News</h1><a class='title'>Hello</a></body></html>
'''

def parse_titles(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get_text(strip=True) for a in soup.select('a.title')]

if __name__ == '__main__':
    print(parse_titles(SAMPLE))

def parse_headings(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return [h.get_text(strip=True) for h in soup.find_all('h1')]

def safe_parse(html: str):
    try:
        return parse_titles(html)
    except Exception as err:
        print('파싱 오류', err)
        return []

# json 저장 연습과 연계
def to_rows(titles):
    return [{'title': t} for t in titles]
