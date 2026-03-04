# Customer Churn Prediction - Telecom Industry

## Project Overview
This project focuses on predicting customer churn in the telecom industry using machine learning techniques.

Customer churn is a critical business problem because retaining existing customers is more cost-effective than acquiring new ones.

The goal of this project is to analyze customer behavior patterns and build predictive models to identify customers likely to churn.

---

## Business Problem
Telecom companies lose recurring revenue when customers discontinue their services (churn).

The objectives are:
- Identify high-risk churn customers
- Improve customer retention strategies
- Reduce acquisition costs

---

## Business Objectives
- Perform exploratory data analysis (EDA) to understand customer behavior
- Analyze key factors influencing churn
- Build a baseline classification model (Logistic Regression)
- Generate actionable business insights

---

## Evaluation Metrics
Since churn prediction is a classification problem, the following metrics are used:

- Accuracy (Secondary Metric)
- Precision (To reduce false churn predictions)
- Recall (Critical for identifying actual churn customers)
- F1 Score
- ROC-AUC Score

Recall is prioritized because failing to identify a churn customer leads to direct revenue loss.

---

## Current Progress
- Data cleaning and preprocessing completed  
- EDA completed with key business insights documented  
- Baseline Logistic Regression model trained and evaluated  
- Model performance analyzed using classification metrics  

---

## Project Structure

Customer_Churn_Prediction/
    │
    ├── data/
    │ ├── raw_telco.csv
    │ └── cleaned_telco.csv
    │
    ├── notebooks/
    │ ├── 01_eda_customer_churn.ipynb
    │ └── 02_modeling_logistic_baseline.ipynb
    │
    ├── reports/
    │ └── baseline_note.md
    │
    ├── src/
    │
    └── README.md



---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Future Work
- Build tree-based models (Random Forest, Gradient Boosting)
- Perform hyperparameter tuning
- Implement reusable pipelines inside `src/`
- Deploy as a simple prediction API

---

## Author
Harsh Rapaka