# Customer Churn Prediction with Robust Preprocessing and Feature Interpretability

## Project Overview

This project focuses on building a **production-ready customer churn prediction system** with particular emphasis on:

- Proper use of **ColumnTransformer** for structured preprocessing  
- **Preventing data leakage** across training and inference stages  
- Leveraging **feature importance** to drive actionable business insights  
- Demonstrating how trained models can be safely deployed for real-world use  

The project simulates a real business scenario where an e-commerce company aims to identify customers likely to churn and take proactive retention actions.

---

## Objectives

The primary goals of this project are to:

1. Explore and apply **ColumnTransformer** to handle numerical and categorical features correctly within a unified pipeline.
2. Ensure **training–serving consistency** by embedding preprocessing inside the model workflow.
3. Avoid common **data leakage pitfalls**, particularly during feature engineering and encoding.
4. Use **feature importance** to explain model behavior and translate predictions into business-level decisions.
5. Demonstrate a simple **model deployment** using Streamlit for inference.

---

## Business Use Case

Customer churn is a critical business problem with direct revenue implications. Accurately predicting churn enables organizations to:

- Target high-risk customers with retention offers  
- Optimize marketing spend  
- Improve customer lifetime value (CLV)  
- Make data-driven product and engagement decisions  

This project bridges the gap between **model accuracy** and **business interpretability** by highlighting which customer behaviors most influence churn.

---

## Dataset Description

The dataset represents customer behavioral and demographic information typically found in an e-commerce platform.

### Feature Categories

- **Demographic features**: Age, Gender, Country, City  
- **Engagement metrics**: Login Frequency, Session Duration, Pages per Session  
- **Transactional behavior**: Total Purchases, Average Order Value, Cart Abandonment Rate  
- **Retention signals**: Membership Years, Days Since Last Purchase  
- **Value indicators**: Lifetime Value, Credit Balance  

The target variable is **customer churn** (binary classification).

---

## Methodology

### 1. Data Preprocessing with ColumnTransformer

Preprocessing is handled using **ColumnTransformer**, which:

- Applies numerical scaling to continuous variables  
- Encodes categorical variables appropriately  
- Keeps preprocessing logic tightly coupled with the model  

This ensures consistency between training and inference and eliminates manual preprocessing errors.

---

### 2. Data Leakage Prevention

Best practices followed include:

- Fitting preprocessing steps **only on training data**  
- Avoiding target-dependent feature engineering  
- Persisting the full preprocessing and model pipeline  
- Reusing the same transformations during inference  

These steps ensure that evaluation metrics reflect true model generalization.

---

### 3. Model Training and Evaluation

A supervised classification model was trained to predict churn with careful attention to:

- Appropriate data splitting strategies  
- Balanced evaluation metrics  
- Overfitting prevention through pipeline design  

---

### 4. Feature Importance for Business Insights

Feature importance was extracted to answer key business questions such as:

- Which customer behaviors most strongly indicate churn?  
- Are engagement metrics more influential than demographics?  
- Which features should be prioritized by business teams?  

The analysis focuses on interpretability and decision support, not just model performance.

---

## Deployment

A **Streamlit application** demonstrates how the trained model can be used in practice.

### Deployment Highlights

- Models and preprocessing are loaded using `joblib`  
- User inputs pass through the same ColumnTransformer  
- Real-time churn predictions are generated  
- Clear feedback is provided to end users  

---

## Project Structure

```
├── ecom_churn.py           # Streamlit application for inference
├── col_encoder.pkl         # Saved ColumnTransformer
├── model_cus.pkl           # Trained churn prediction model
├── notebook.ipynb          # Model training and analysis
├── README.md               # Project documentation
```

---

## Key Takeaways

- **ColumnTransformer** is essential for scalable and leak-free ML pipelines.
- Data leakage prevention directly impacts model trustworthiness.
- Feature importance converts models into actionable business tools.
- Deployment must always reuse the exact training preprocessing logic.

---

## Future Improvements

- Add data and prediction drift monitoring  
- Extend interpretability using SHAP values  
- Implement CI/CD for automated retraining  
- Expose predictions via a REST API (FastAPI)  

---

## Author

**Jay**  
Data Scientist & Machine Learning Engineer  
Focused on building reliable, interpretable, and business-aligned ML systems.
