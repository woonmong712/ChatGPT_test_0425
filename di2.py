import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')

# 변수의 분포 확인
fig, axs = plt.subplots(ncols=3, nrows=5, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in df.items():
    axs[index].hist(v, bins=30, color='green')
    axs[index].set_title(k.upper())
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
plt.show()
