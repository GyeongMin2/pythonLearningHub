import pandas as pd
from pathlib import Path

DATA = Path('analysis/weather.csv')

def summarize():
    df = pd.read_csv(DATA, encoding='utf-8')
    print('rows', len(df))
    print(df.describe(include='all'))
    return df

def monthly_mean(df):
    if 'month' not in df.columns:
        return df
    return df.groupby('month')['temp'].mean()

def save_summary(path: str):
    df = summarize()
    monthly_mean(df).to_csv(path, encoding='utf-8')

if __name__ == '__main__':
    summarize()

def rainy_days(df):
    return df[df['rain'] > 0.0]

def city_stats(df):
    return df.groupby('city').agg({'temp': 'mean', 'rain': 'sum'})

# 리팩터: 함수 이름 정리
def run():
    df = summarize()
    print(city_stats(df))
