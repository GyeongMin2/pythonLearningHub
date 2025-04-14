from bs4 import BeautifulSoup

SAMPLE = '''
<html><body><h1>News</h1><a class='title'>Hello</a></body></html>
'''

def parse_titles(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get_text(strip=True) for a in soup.select('a.title')]

if __name__ == '__main__':
    print(parse_titles(SAMPLE))
