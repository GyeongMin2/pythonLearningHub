# pandas Series 연습
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
print('mean', s.mean())

print('max idx', s.idxmax())
print('filter > 15', s[s > 15])
