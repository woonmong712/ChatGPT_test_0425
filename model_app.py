import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')

# 입력 변수와 목적 변수 분리
X = df.drop('medv', axis=1)
y = df['medv']

# 학습용과 테스트용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 분리된 데이터셋의 크기 확인
print("학습용 데이터셋 크기:", X_train.shape)
print("테스트용 데이터셋 크기:", X_test.shape)


# Random Forest 모델 생성
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# 학습용 데이터로 모델 학습
rf_model.fit(X_train, y_train)

# 테스트용 데이터로 모델 예측
y_pred = rf_model.predict(X_test)

# 모델 저장
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
