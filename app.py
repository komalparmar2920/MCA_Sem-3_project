from flask import Flask, render_template, request
from tabulate import tabulate
import numpy as np
import pandas
import sklearn
import pickle 

model=pickle.load(open(r'C:\Users\Lenovo\Downloads\model.pkl','rb'))
model1=pickle.load(open(r'C:\Users\Lenovo\Downloads\model1.pkl','rb'))
model2=pickle.load(open(r'C:\Users\Lenovo\Downloads\model2.pkl','rb'))
model3=pickle.load(open(r'C:\Users\Lenovo\Downloads\model3.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("exam.html")

@app.route("/predict",methods=['POST'])
def rm_predict():
    n=int(request.form["Nitrogen"])
    ph=int(request.form["Phosphorus"])
    pot=int(request.form["Potassium"])
    PH=float(request.form["pH"])

    features_list=[n,ph,pot,PH]
    sin_pred=np.array(features_list).reshape(1,-1)

    predict=model.predict(sin_pred)
    predict1=model1.predict(sin_pred)
    predict2=model2.predict(sin_pred)
    predict3=model3.predict(sin_pred)



    fertilizer_dict={
                        1:'Urea',
                        2:'DAP',                    
                        3:'MOP',                    
                        4:'SSP',                    
                        5:'Magnesium Sulphate',     
                        6:'Ammonium Sulphate',       
                        7:'Ferrous Sulphate',        
                        8:'Hydrated Lime',
                    } 

    if predict[0] in fertilizer_dict:
        fertilizer = fertilizer_dict[predict[0]]
        result="{} : is the best fertilizer for you crop.".format(fertilizer)
    else:
        result="sorry we don't find fertilizer for your crop"

    if predict1[0] in fertilizer_dict:
        fertilizer = fertilizer_dict[predict1[0]]
        result1="{} : is the best fertilizer for you crop.".format(fertilizer)
    else:
        result1="sorry we don't find fertilizer for your crop"    
    #print(tabulate(result, headers=result, tablefmt="grid"))

    if predict2[0] in fertilizer_dict:
        fertilizer = fertilizer_dict[predict2[0]]
        result2="{} : is the best fertilizer for you crop.".format(fertilizer)
    else:
        result2="sorry we don't find fertilizer for your crop"

    if predict3[0] in fertilizer_dict:
        fertilizer = fertilizer_dict[predict3[0]]
        result3="{} : is the best fertilizer for you crop.".format(fertilizer)
    else:
        result3="sorry we don't find fertilizer for your crop"    
    return render_template('exam.html',result = result,result1=result1,result2=result2,result3=result3)

if __name__ == '__main__':
    app.run(debug=True)
