import flask
from flask_cors import CORS 
import joblib
import numpy as np
from flask import Flask,request, jsonify
import os 

ROOT_DIR=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
APP_PATH=os.path.join(ROOT_DIR,'app/')

ui_path=os.path.join(APP_PATH,'flutter_ui')
model_path=os.path.join(ROOT_DIR,'models')
app=Flask(__name__,static_folder=ui_path)

CORS(app)
model=joblib.load(os.path.join(model_path,'my_model.pkl'))

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    time_spent=data['time_spent']
    videos_watched=data['videos_watched']
    quiz_score=data['quiz_score']
    
    input_data=np.array([[time_spent,videos_watched,quiz_score]])
    prediction=model.predict(input_data)[0]
    
    result='will complete course' if prediction ==1 else "won't complete"
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)
    




