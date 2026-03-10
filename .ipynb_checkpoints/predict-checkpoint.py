import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"

model = joblib.load(MODEL_PATH)
def predict_churn(input_data):

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    label = "Churn" if prediction == 1 else "No Churn"

    return label, probability


if __name__ == "__main__":

    sample_customer = {
        "Gender": 0,
        "Senior Citizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "Tenure Months": 12,
        "Phone Service": "Yes",
        "Multiple Lines": "No",
        "Internet Service": "Fiber optic",
        "Online Security": 1,
        "Online Backup": 0,
        "Device Protection": 0,
        "Tech Support": 0,
        "Streaming TV": 1,
        "Streaming Movies": 1,
        "Contract": "Month-to-month",
        "Paperless Billing": "Yes",
        "Payment Method": "Electronic check",
        "Monthly Charges": 70.5,
        "Total Charges": 850,
        "Tenure_Group": "Early",
        "Charge_to_Tenure": 70.5 / 13,
        "Service_Count": 3
    }

    pred, prob = predict_churn(sample_customer)

    print("Prediction:", pred)
    print("Churn Probability:", prob)