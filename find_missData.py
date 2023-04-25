import pandas as pd

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')

# 누락된 값이 있는지 확인하기
missing_data = df.isnull().sum()
print(missing_data)
