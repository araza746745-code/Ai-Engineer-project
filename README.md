# 🤖 AI-powered Sales Prediction System

> An end-to-end Machine Learning application for predicting sales revenue, with a REST API built using FastAPI.

---

## 📌 Project Overview

This project demonstrates an end-to-end AI/ML workflow, starting from data preparation and feature engineering to model training, prediction, and API deployment.

The system is designed to take input features, process them through the trained machine learning model, and return a predicted sales amount through a REST API.

---
---

## 🛠️ Tech Stack

### Programming & Data
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Linear Regression
- Joblib

### API Development
- FastAPI
- Uvicorn
- REST API

### Deployment & DevOps
- Docker
- Docker Hub
- Render

### Version Control
- Git
- GitHub


## 🎯 Problem Statement

Businesses generate large amounts of sales data and need reliable ways to estimate future revenue.

The objective of this project is to build a machine learning system that:

- Processes sales data
- Performs feature engineering
- Trains a regression model
- Generates sales predictions
- Exposes the prediction model through a REST API

---

## 🔄 End-to-End Workflow

```text
Raw Sales Data
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Prediction
      ↓
FastAPI REST API
      ↓
Predicted Gross Amount

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| FastAPI | REST API |
| Uvicorn | API server |
| Git | Version control |
| GitHub | Code hosting |

---

## 📂 Project Structure

```text
Ai-Engineer_project/
│
├── api.py
├── main.py
├── phase1.py
├── feature_engineering.py
├── model_training.py
├── prediction.py
├── rnn_prctice.py
├── requirements.txt
├── README.md
└── .gitignore

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- Git & GitHub

---

## 🚀 Key Features

- Sales data preprocessing
- Feature engineering
- Missing-value handling
- Machine learning model training
- Train/test data splitting
- Model evaluation using MAE and R² Score
- Model serialization using Joblib
- REST API using FastAPI
- Real-time sales prediction through `/predict`

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** to predict the `gross_amount` based on 18 input features.

### Input Features

1. order_id
2. customer_id
3. customer_phone
4. age
5. pincode
6. product_id
7. supplier_id
8. quantity
9. unit_price
10. discount_percent
11. discount_amount
12. net_amount
13. tax_percent
14. tax_amount
15. shipping_fee
16. total_amount
17. salesperson_id
18. rating

### Target

`gross_amount`

---

## 🌐 API

The trained model is exposed through a FastAPI REST API.

### Endpoint

```text
POST /predict

### Example Request

```json
[
  1001,
  2001,
  9876543210,
  25,
  585101,
  3001,
  4001,
  2,
  500,
  10,
  100,
  900,
  18,
  162,
  50,
  1112,
  501,
  4.5
]

### Example Response

```json
{
  "predicted_gross_amount": 581.49
}

### API Documentation

After starting the API, open:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI for testing the prediction API.

---

## 📊 Model Performance

The model was evaluated using:

- MAE (Mean Absolute Error)
- R² Score

### Evaluation Results

- MAE: 0.7037
- R² Score: 0.9999999998

The trained model is saved using Joblib as:

`sales_model.pkl`

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txtgit stautus

### API Documentation

After starting the API, open:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI for testing the prediction API.

---

## 📊 Model Performance

The model was evaluated using:

- MAE (Mean Absolute Error)
- R² Score

### Evaluation Results

- MAE: 0.7037
- R² Score: 0.9999999998

The trained model is saved using Joblib as:

`sales_model.pkl`

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

---

## 🚀 Live Deployment

The Sales Prediction API is deployed using Docker and Render.

**Live API:**  
https://sales-prediction-api-latest.onrender.com

**API Documentation:**  
https://sales-prediction-api-latest.onrender.com/docs

> Note: The free Render instance may take some time to wake up after inactivity.