from crypt import methods
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model/diabatic.80.pkl')

@app.route('/')
def home():
    return render_template('diabetic.html')

'''@app.route('/data', methods=['post'])
def data():
    firstname = request.form.get('first_name')
    secondname = request.form.get('second_name')
    phonenumber = request.form.get('phone_number')
    email = request.form.get('email')

    print(firstname, secondname, phonenumber, email)

    return 'data received'  '''

@app.route('/diabetic', methods=['post'])
def diabetic():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    #print(preg, plas, pres, skin, test, mass, pedi, age)

    result = model.predict([[preg , plas , pres, skin , test, mass , pedi, age]])

    if result[0] == 1:
        data = 'the person is Diabetic'
    else:
        data = 'the person is not diabetic'

    #print(data)

    return render_template('predict.html', data = data)
    
app.run(debug = True)