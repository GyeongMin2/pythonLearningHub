"""날씨 수집기 — CSV 로그 + (선택) API/스크래핑 스텁"""
import csv
import logging
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

LOG = Path('projects/weather_log.csv')
REPORT = Path('projects/weather_report.txt')
API_URL = 'https://api.example.com/weather'  # placeholder

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
logger = logging.getLogger('weather')

HEADERS = {
    'User-Agent': 'pythonLearningHub-study/1.0',
}

def init_log():
    if LOG.exists():
        return
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open('w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['date', 'city', 'temp', 'rain', 'source'])

def append_row(city, temp, rain=0.0, source='manual'):
    init_log()
    day = datetime.now().strftime('%Y-%m-%d')
    with LOG.open('a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([day, city, temp, rain, source])
    logger.info('saved %s %s', city, temp)

def load_rows():
    if not LOG.exists():
        return []
    with LOG.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

def summary():
    rows = load_rows()
    if not rows:
        print('데이터 없음')
        return
    temps = [float(r['temp']) for r in rows]
    rainy = [r for r in rows if float(r.get('rain', 0)) > 0]
    print(f"{len(rows)}건, 평균기온 {sum(temps)/len(temps):.1f}")
    print(f'비 온 기록 {len(rainy)}건')

def fetch_api(city: str):
    if requests is None:
        logger.warning('requests 없음 — 더미 반환')
        return {'city': city, 'temp': 20.0, 'rain': 0.0}
    try:
        # 실제 키 없어서 placeholder
        resp = requests.get(API_URL, params={'city': city}, headers=HEADERS, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        return data
    except Exception as err:
        logger.error('API 실패 %s', err)
        return {'city': city, 'temp': 18.0, 'rain': 0.0, 'source': 'fallback'}

def collect_city(city: str):
    data = fetch_api(city)
    temp = float(data.get('temp', 0))
    rain = float(data.get('rain', 0))
    source = data.get('source', 'api')
    append_row(city, temp, rain, source)

def scrape_stub(city: str):
    # BeautifulSoup 으로 확장 예정
    logger.info('scrape stub for %s', city)
    append_row(city, 19.5, 0.0, 'scrape-stub')

def write_report():
    rows = load_rows()
    lines_out = ['=== weather report ===']
    for r in rows[-10:]:
        lines_out.append(f"{r['date']} {r['city']} {r['temp']}C rain={r['rain']}")
    REPORT.write_text('\n'.join(lines_out) + '\n', encoding='utf-8')

def filter_by_city(city: str):
    return [r for r in load_rows() if r['city'].lower() == city.lower()]

def cli():
    print('1 수동입력 2 API수집 3 요약 4 리포트 0 종료')
    while True:
        choice = input('> ').strip()
        if choice == '0':
            break
        if choice == '1':
            city = input('도시: ').strip() or 'Seoul'
            temp = float(input('기온: ').strip() or '20')
            rain = float(input('강수: ').strip() or '0')
            append_row(city, temp, rain, 'manual')
        elif choice == '2':
            city = input('도시: ').strip() or 'Seoul'
            collect_city(city)
        elif choice == '3':
            summary()
        elif choice == '4':
            write_report()
            print('saved', REPORT)
        else:
            print('다시')

def export_txt(path: str = 'projects/weather_export.txt'):
    rows = load_rows()
    Path(path).write_text('\n'.join(str(r) for r in rows), encoding='utf-8')

def validate_row(row: dict) -> bool:
    try:
        float(row['temp'])
        float(row.get('rain', 0))
        return bool(row.get('city'))
    except (KeyError, ValueError):
        return False

def clean_log():
    rows = [r for r in load_rows() if validate_row(r)]
    init_log()
    with LOG.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['date', 'city', 'temp', 'rain', 'source'])
        for r in rows:
            w.writerow([r['date'], r['city'], r['temp'], r['rain'], r.get('source', '')])
    logger.info('cleaned %s rows', len(rows))

if __name__ == '__main__':
    # 테스트 데이터
    if not LOG.exists():
        append_row('Seoul', 22.0, 0.0, 'seed')
        append_row('Busan', 24.5, 1.2, 'seed')
    clean_log()
    cli()
    # rev 11/11 — 프로젝트 마무리
