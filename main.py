from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from schema.user_input import UserInput
from predict import predict_output

with open('model.pkl', 'rb') as f:
    model= pickle.load(f)

MODEL_VERSION = '1.0.0'

app=FastAPI()



@app.get('/')
def home():
    return {'message' : 'Insurace prediction API'} 


@app.get('/health')
def health_check():
    return{
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }



@app.post('/predict')
def predict_premium(data: UserInput):

    user_input={

        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifesyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
    
        prediction= predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': 'Prediction'})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))