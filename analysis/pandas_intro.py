import pandas as pd
from pathlib import Path

CSV = Path('analysis/weather.csv')

def load_weather():
    if not CSV.exists():
        return pd.DataFrame()
    return pd.read_csv(CSV, encoding='utf-8')

def main():
    df = load_weather()
    if df.empty:
        print('데이터 없음')
        return
    print(df.head())
    print('평균 기온', df['temp'].mean())

    rainy = df[df['rain'] > 0]
    print('비 온 날', len(rainy))

    by_city = df.groupby('city')['temp'].mean()
    print(by_city)
