# Customer Churn Model – Key Insights

## Project Objective

Customer churn is a major challenge for telecom companies because losing customers directly affects revenue and growth. The objective of this project is to build a machine learning model that predicts whether a customer is likely to churn based on their demographic information, service usage, and billing details. Identifying high-risk customers allows companies to take proactive actions to improve retention.

---

## Model Performance

Three models were trained to predict customer churn:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------|------|------|------|------|------|
| Logistic Regression | 0.80 | 0.64 | 0.58 | 0.61 | 0.84 |
| Random Forest | 0.78 | 0.62 | 0.51 | 0.56 | 0.83 |
| XGBoost | 0.77 | 0.57 | 0.55 | 0.56 | 0.82 |

Logistic Regression achieved the best ROC-AUC score and was selected as the primary model for churn prediction.

---

## Key Drivers of Customer Churn

Feature importance analysis was performed to identify the most influential factors contributing to customer churn.

### 1. Month-to-Month Contract
Customers with month-to-month contracts show the highest churn probability because they are not committed to long-term agreements and can easily switch providers.

### 2. Fiber Optic Internet
Customers using fiber optic internet show higher churn rates. This may be due to higher pricing or higher expectations regarding service quality.

### 3. Charge-to-Tenure Ratio
Customers paying higher charges relative to their tenure are more likely to churn, indicating dissatisfaction early in the customer lifecycle.

---

## Business Interpretation

The analysis indicates that contract flexibility, internet service type, and pricing relative to customer tenure are the primary drivers of churn.

Customers on month-to-month contracts represent the highest churn risk because they can easily switch providers. Fiber internet customers may have higher expectations regarding service quality, and unmet expectations may contribute to churn. Additionally, customers paying higher charges early in their subscription may perceive insufficient value.

---

## Business Recommendations

Based on the model findings, the following strategies can help reduce customer churn:

- Encourage customers to switch from month-to-month contracts to long-term contracts through discounts or loyalty rewards.
- Improve service quality and customer support for fiber internet users.
- Offer promotional pricing or onboarding benefits for new customers.
- Implement targeted retention campaigns for customers identified as high churn risk.