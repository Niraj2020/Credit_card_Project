from wsgiref import simple_server
from flask import Flask, request, app, render_template
from flask import Response
from flask_cors import CORS
import numpy as np
import pandas as pd
import bz2
import pickle


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

scalarobject=bz2.BZ2File("Model\standardScalar.pkl", "rb")
scalar=pickle.load(scalarobject)
modelforpred = bz2.BZ2File("Model\modelforprediction.pkl", "rb")
model=pickle.load(modelforpred)

#Route for homepage

@app.route('/')
def index():
    return render_template('index.html')


#Route for Single data point prediction
@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        LIMIT_BAL=float(request.form.get("LIMIT_BAL"))
        SEX=int(request.form.get("SEX"))
        EDUCATION=int(request.form.get("EDUCATION"))
        MARRIAGE=int(request.form.get("MARRIAGE"))
        AGE=int(request.form.get("AGE"))
        PAY_SEPT=int(request.form.get("PAY_SEPT"))
        PAY_AUG =int(request.form.get('PAY_AUG'))
        PAY_JUL=int(request.form.get("PAY_JUL"))
        PAY_JUN=int(request.form.get("PAY_JUN"))
        PAY_MAY=int(request.form.get("PAY_MAY"))
        PAY_APR=int(request.form.get("PAY_APR"))
        BILL_AMT_SEPT=float(request.form.get("BILL_AMT_SEPT"))
        BILL_AMT_AUG=float(request.form.get("BILL_AMT_AUG"))
        BILL_AMT_JUL=float(request.form.get("BILL_AMT_JUL"))
        BILL_AMT_JUN =float(request.form.get('BILL_AMT_JUN'))
        BILL_AMT_MAY=float(request.form.get("BILL_AMT_MAY"))
        BILL_AMT_APR=float(request.form.get("BILL_AMT_APR"))
        PAY_AMT_SEPT=float(request.form.get("PAY_AMT_SEPT"))
        PAY_AMT_AUG=float(request.form.get("PAY_AMT_AUG"))
        PAY_AMT_JUL=float(request.form.get("PAY_AMT_JUL"))
        PAY_AMT_JUN=float(request.form.get("PAY_AMT_JUN"))
        PAY_AMT_MAY=float(request.form.get("PAY_AMT_MAY"))
        PAY_AMT_APR = float(request.form.get('PAY_AMT_APR'))


        new_data=scalar.transform([[LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_SEPT,PAY_AUG,PAY_JUL,PAY_JUN,PAY_MAY,PAY_APR,BILL_AMT_SEPT,BILL_AMT_AUG,BILL_AMT_JUL,BILL_AMT_JUN,BILL_AMT_MAY,BILL_AMT_APR,PAY_AMT_SEPT,PAY_AMT_AUG,PAY_AMT_JUL,PAY_AMT_JUN,PAY_AMT_MAY,PAY_AMT_APR]])
        predict=model.predict(new_data)

        if predict[0]==1:
            result = 'Defaulter'
        else:
            result='Non-Defaulter'

        return render_template('result.html', result=result)

    else:
        return render_template('home.html')
    
    

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')    
    



if __name__=="__main__":
    app.run(debug=True)                  



            