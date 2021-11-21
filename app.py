from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('homepage.html')



@app.route('/templates/home.html')
def nav():
    return render_template('home.html')




@app.route('/predict', methods=['POST'])
def home():
    peru=request.form['name']
    data1 = int(request.form['age'])
    data2 = int(request.form['gender'])
    data3 = int(request.form['chestpain'])
    data4 = int(request.form['restbp'])
    data5 = int(request.form['chol'])
    data6 = int(request.form['fbs'])
    data7 = int(request.form['recg'])
    data8 = int(request.form['hb'])
    data9 = int(request.form['ani'])
    data10 = int(request.form['oldpeak'])
    data11= int(request.form['slope'])
    data12= int(request.form['vessels'])
    data13= int(request.form['thal'])



    arr = np.array([[data1, data2, data3, data4,data5, data6, data7, data8,data9, data10, data11, data12,data13]])
    pred = model.predict(arr)

   
    return render_template('result.html', data=pred,name=peru)
    

 

if __name__ == "__main__":
    app.run(debug=True)















