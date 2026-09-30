# 🤖 AI Engineer – Sales Prediction System

> An end-to-end Machine Learning application for predicting sales revenue, with a REST API built using FastAPI.

---

## 📌 Project Overview

This project demonstrates an end-to-end AI/ML workflow, starting from data preparation and feature engineering to model training, prediction, and API deployment.

The system is designed to take input features, process them through the trained machine learning model, and return a predicted sales amount through a REST API.

---

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