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
