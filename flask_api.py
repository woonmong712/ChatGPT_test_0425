from flask import Flask, request, render_template, jsonify
import pickle

# 모델 로드
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/price')
def price():
    prediction = request.args.get('prediction')
    return render_template('price.html', prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    # 모든 특성 받아오기
    crim = float(request.form['crim'])
    zn = float(request.form['zn'])
    indus = float(request.form['indus'])
    chas = float(request.form['chas'])
    nox = float(request.form['nox'])
    rm = float(request.form['rm'])
    age = float(request.form['age'])
    dis = float(request.form['dis'])
    rad = float(request.form['rad'])
    tax = float(request.form['tax'])
    ptratio = float(request.form['ptratio'])
    b = float(request.form['b'])
    lstat = float(request.form['lstat'])

    # 특성 리스트 만들기
    X = [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]]

    # 모델 예측 수행
    prediction = model.predict(X)[0]

    return jsonify({'prediction': prediction})



if __name__ == '__main__':
    app.run(debug=True)
