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
