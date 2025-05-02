import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (study-bot; +https://github.com/GyeongMin2/pythonLearningHub)',
}

def fetch(url: str, timeout=10):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as err:
        print('요청 실패', err)
        return ''

if __name__ == '__main__':
    html = fetch('https://example.com')
    print('len', len(html))

def fetch_bytes(url: str):
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.content
