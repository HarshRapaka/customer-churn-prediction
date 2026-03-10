# app/app.py
import streamlit as st
import pandas as pd
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_churn

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("Customer Churn Prediction Dashboard")
st.write("Predict whether a telecom customer is likely to churn based on their profile.")

st.sidebar.header("Customer Information")

# --------------------
# Customer Input Form
# --------------------
with st.form("customer_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", [0, 1])
    online_backup = st.selectbox("Online Backup", [0, 1])
    device_protection = st.selectbox("Device Protection", [0, 1])
    tech_support = st.selectbox("Tech Support", [0, 1])
    streaming_tv = st.selectbox("Streaming TV", [0, 1])
    streaming_movies = st.selectbox("Streaming Movies", [0, 1])

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=500.0, value=70.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, max_value=5000.0, value=850.0)

    tenure_group = st.selectbox("Tenure Group", ["Early", "Mid", "Late"])
    charge_to_tenure = st.number_input(
        "Charge to Tenure Ratio", min_value=0.0, max_value=100.0, 
        value=monthly_charges/tenure if tenure>0 else 0
    )
    service_count = st.number_input("Service Count", min_value=0, max_value=10, value=3)

    submit_button = st.form_submit_button("Predict Churn")

# --------------------
# Run prediction on submit
# --------------------
if submit_button:
    customer_input = {
        "Gender": 0 if gender=="Male" else 1,
        "Senior Citizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure,
        "Phone Service": phone_service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Contract": contract,
        "Paperless Billing": paperless_billing,
        "Payment Method": payment_method,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges,
        "Tenure_Group": tenure_group,
        "Charge_to_Tenure": charge_to_tenure,
        "Service_Count": service_count
    }

    # Predict churn
    label, probability, risk, top_features = predict_churn(customer_input, return_top_features=True)

    st.subheader("Prediction Result")
    st.markdown(f"**Label:** {label}")
    st.markdown(f"**Churn Probability:** {probability:.2%}")
    st.markdown(f"**Risk Category:** {risk}")
    st.progress(min(float(probability), 1.0))
    st.markdown("---")

    st.subheader("Top Influencing Factors")
    if top_features:
        for feat, val in top_features:
            st.write(f"{feat}: {val:.3f}")
    else:
        st.write("Top feature information not available.")

    st.info("Business Note: High-risk customers should be targeted with retention campaigns.")