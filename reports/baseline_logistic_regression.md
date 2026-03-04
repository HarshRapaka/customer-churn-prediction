# Baseline Model - Logistic Regression (Churn Prediction)

A Logistic Regression model was built using a full preprocessing pipeline with:

- **StandardScaler** applied to numeric features
- **OneHotEncoder** applied to categorical features
- Class imbalance handled using 'class_weight="balanced"'

---

## Performance Metrics (Test Set)

- **Accuracy:** ~0.80
- **Precision:** ~0.64
- **Recall:** ~0.61-0.69 (depending on classification threshold)
- **ROC_AUC:** ~0.84
- **Average Precision (PR AUC):** ~0.63

The ROC curve indicates good class separability, while the Precision-Recall curve demostrate reasonable performance under class imbalance.

---

## Key Drivers of Churn

### Strongest Positive Churn Indicators
- Month-to-month contracts
- No dependents
- Higher total charges
- Higher monthly charges
- Fiber optic internet service
- Electronic check payment method

### Strongest Retention Indicators
- Longer tenure
- Two-year contracts
- Having dependents
- DSL internt service
- Subscribed tech support
- Subscribed online security

---

## Conclusion 

The baseline Logistic Regression model demonstrates meaningful predictive power and captures intuitive business patterns. It serves as a strong reference benchmark before exploring more complex non-linear models such as Random Forest or Gradient Boosting.