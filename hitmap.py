import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')

# 상관관계 분석
corr_matrix = df.corr()

# 그래프 크기 설정
plt.figure(figsize=(12,10))

# 히트맵 그리기
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)

# 그래프 타이틀 추가
plt.title('Correlation Heatmap')

# 그래프 보이기
plt.show()