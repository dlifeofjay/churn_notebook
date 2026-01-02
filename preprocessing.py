from pydantic import BaseModel
import pandas as pd
import joblib


preprocessor = joblib.load("col_encoder.pkl")
model = joblib.load("model_cus.pkl")


class ChurnRequest(BaseModel):
    Age: int
    Gender: str
    Country: str
    City: str
    Membership_Years: int
    Login_Frequency: int
    Session_Duration_Avg: int
    Pages_Per_Session: int
    Cart_Abandonment_Rate: float
    Total_Purchases: int
    Average_Order_Value: float
    Days_Since_Last_Purchase: int
    Discount_Usage_Rate: float
    Mobile_App_Usage: float
    Lifetime_Value: int
    Credit_Balance: int


class ChurnResponse(BaseModel):
    churn: int
    message: str


def predict_churn(payload: dict) -> int:
    df = pd.DataFrame([payload])
    transformed = preprocessor.transform(df)
    prediction = model.predict(transformed)
    return int(prediction[0])