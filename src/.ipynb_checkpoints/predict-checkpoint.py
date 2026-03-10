# src/predict.py
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import shap

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"

# Load pipeline
model = joblib.load(MODEL_PATH)

def predict_churn(input_data, return_top_features=False):
    """
    Predict churn for a single customer.
    Returns label, probability, risk, and top features using SHAP if requested.
    """
    # Convert dict to dataframe
    df = pd.DataFrame([input_data])

    # Ensure all expected columns exist (fill missing with 0)
    expected_cols = model.feature_names_in_
    df = df.reindex(columns=expected_cols, fill_value=0)

    # Prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    label = "Churn" if prediction == 1 else "No Churn"

    # Risk category
    if probability < 0.3:
        risk = "Low Risk"
    elif probability < 0.6:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    top_features = None
    if return_top_features:
        # Use SHAP to get feature contributions
        classifier = model.named_steps['model']  # XGBClassifier
        try:
            # Explainer handles the pipeline input
            explainer = shap.Explainer(classifier, model.named_steps['preprocessor'].transform(df))
            shap_values = explainer(model.named_steps['preprocessor'].transform(df))
            # Get absolute SHAP values for this customer and top 3 features
            mean_abs_shap = np.abs(shap_values.values).mean(axis=0)
            top_idx = np.argsort(mean_abs_shap)[::-1][:3]
            feature_names = shap_values.feature_names
            top_features = [(feature_names[i], mean_abs_shap[i]) for i in top_idx]
        except Exception as e:
            top_features = None
            print("SHAP error:", e)

    return (label, probability, risk, top_features) if return_top_features else (label, probability, risk)


if __name__ == "__main__":
    # Example usage
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

    pred, prob, risk, top_features = predict_churn(sample_customer, return_top_features=True)
    print("Prediction:", pred)
    print("Churn Probability:", f"{prob:.2%}")
    print("Risk Category:", risk)
    if top_features:
        print("Top Features:", top_features)