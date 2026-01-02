from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from preprocessing import ChurnRequest, ChurnResponse, predict_churn

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
    )

#Needed for streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict", response_model=ChurnResponse)
def predict(data: ChurnRequest):
    prediction = predict_churn(data.dict())

    if prediction == 0:
        message = "This customer is likely to churn"
    else:
        message = "This customer will not churn"


    return {
        "churn": prediction,
        "message": message
    }
