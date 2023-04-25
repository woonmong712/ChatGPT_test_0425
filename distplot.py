# BostonHouse 집 값 분포도를 통해 작성하는 코드
# https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')

# 분포 확인
sns.distplot(df['medv'], kde=False)
plt.title('Distribution of House Prices in Boston')
plt.xlabel('Prices')
plt.ylabel('Count')
plt.show()

