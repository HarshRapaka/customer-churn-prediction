# Customer Churn Prediction - Telecom Industry

## Project Overview
This project focuses on predicting customer churn in the telecom industry using machine learning techniques.

Customer churn is a critical business problem because retaining existing customers is more cost-effective than acquiring new ones.

The goal of this project is to analyze customer behavior patterns and build predictive models to identify customers likely to churn.

---

## Project Highlights
- Built a machine learning pipeline to predict telecom customer churn
- Compared multiple models: Logistic Regression, Random Forest, and XGBoost
- Achieved **0.84 ROC-AUC** using Logistic Regression
- Identified major drivers influencing customer churn
- Generated business insights for telecom retention strategies

---

## Business Problem
Telecom companies lose recurring revenue when customers discontinue their services (churn).

The objectives are:
- Identify high-risk churn customers
- Improve customer retention strategies
- Reduce customer acquisition costs

---

## Business Objectives
- Perform exploratory data analysis (EDA) to understand customer behavior
- Analyze key factors influencing churn
- Train and compare multiple classification models
- Identify the most important drivers of churn
- Generate actionable business insights

---

## Evaluation Metrics
Since churn prediction is a classification problem, the following metrics are used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

Recall is prioritized because failing to identify a churn customer can lead to direct revenue loss for the company.

---

## Model Performance

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------|------|------|------|------|------|
| Logistic Regression | 0.80 | 0.64 | 0.58 | 0.61 | 0.84 |
| Random Forest | 0.78 | 0.62 | 0.51 | 0.56 | 0.83 |
| XGBoost | 0.77 | 0.57 | 0.55 | 0.56 | 0.82 |

Logistic Regression achieved the best ROC-AUC score and was selected as the primary model for churn prediction.

---

## Key Churn Drivers
Feature importance analysis identified the following major drivers of churn:

1. Month-to-Month Contract  
2. Fiber Optic Internet Service  
3. Charge-to-Tenure Ratio  

Customers on month-to-month contracts and customers paying higher charges early in their subscription lifecycle are more likely to churn.

---

## Business Insights
The analysis suggests that contract type, internet service type, and pricing relative to customer tenure are the most important factors influencing churn.

Telecom companies can reduce churn by:
- Encouraging long-term contracts
- Improving service quality for fiber internet customers
- Offering promotional pricing for new customers

Detailed insights can be found in:

`reports/customer_churn_insights.md`

---

## Project Structure
```text
Customer_Churn_Prediction/
│
├── data/
│   ├── raw_telco.csv
│   └── cleaned_telco.csv
│
├── notebooks/
│   ├── 01_eda_customer_churn.ipynb
│   └── 02_model_training.ipynb
│
├── reports/
│   ├── baseline_logistic_regression.md
│   └── customer_churn_insights.md
│
├── src/
│
└── README.md
```

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

## How to Run This Project

Clone the repository:

```
git clone https://github.com/HarshRapaka/customer-churn-prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the notebooks:

```
notebooks/01_eda_customer_churn.ipynb
notebooks/02_model_training.ipynb
```

---

## Future Work
- Implement reusable ML pipelines inside `src/`
- Add model explainability techniques (SHAP)
- Build a churn prediction dashboard
- Deploy the model as an API

---

## Author
Harsh Rapaka