from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    Txa = float(request.values['Txa'])
    Tya = float(request.values['Tya'])
    Tza = float(request.values['Tza'])
    Txg = float(request.values['Txg'])
    Tyg = float(request.values['Tyg'])
    Tzg = float(request.values['Tzg'])
    Txm = float(request.values['Txm'])
    Tym = float(request.values['Tym'])
    Tzm = float(request.values['Tzm'])
    RAxa = float(request.values['RAxa'])
    RAya = float(request.values['RAya'])
    RAza = float(request.values['RAza'])
    LAxa = float(request.values['LAxa'])
    LAya = float(request.values['LAya'])
    LAza = float(request.values['LAza'])
    RLxa = float(request.values['RLxa'])
    RLya = float(request.values['RLya'])
    RLza = float(request.values['RLza'])
    LLxa = float(request.values['LLxa'])
    LLya = float(request.values['LLya'])
    LLza = float(request.values['LLza'])
    make_pred = [[Txa,Tya,Tza,Txg,Tyg,Tzg,Txm,Tym,Tzm,RAxa,RAya,RAza,LAxa,LAya,LAza,RLxa,RLya,RLza,LLxa,LLya,LLza]]
    print(make_pred)
    output = model.predict(make_pred)
    print(LLza)
    return render_template('result.html', prediction_text =output)


if __name__ == '__main__':
    app.run(port=8000)
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
