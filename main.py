          
from flask import Flask,request,render_template 
from utils import car_data
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data',methods = ['POST','GET'])
def get_data():
    try :
        if request.method == 'POST':
            data = request.form
            class_obj = car_data(data)
            result = class_obj.car_prediction()

            return render_template('index.html',prediction = result)
        else :
            return "Prediction Unsuccessful"
    except :
        print(traceback.print_exc())

    

if __name__  ==  "__main__":
    app.run(host = '0.0.0.0',debug =True)

