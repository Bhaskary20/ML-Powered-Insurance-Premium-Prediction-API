# 🚀 Insurance Premium Category Predictor API

A Machine Learning API built using **FastAPI** that predicts the **insurance premium category** (Low, Medium, High) based on a user’s health and lifestyle information. This project demonstrates an end-to-end pipeline from feature engineering to model inference and API deployment.

---

## 🧠 Project Overview

This project uses a trained **RandomForestClassifier** to predict the likely insurance premium bracket a customer will fall into. It is designed for insurtech applications, risk profiling, or recommendation systems.

---

## 🔍 Features

- 🚀 Built with **FastAPI** for high-performance APIs
- ✅ Robust input validation using **Pydantic**
- 🧮 Real-time predictions using **RandomForestClassifier**
- 🔧 Automatic feature engineering (BMI, Lifestyle Risk, Age Group, City Tier)
- 📊 Outputs class probabilities and model confidence
- 📦 Model serialization using `pickle`

---

## 🧬 Input Parameters

| Field         | Type     | Description                                 |
|--------------|----------|---------------------------------------------|
| age          | int      | Age of the person                           |
| height       | float    | Height in meters                            |
| weight       | float    | Weight in kilograms                         |
| income_lpa   | float    | Annual income in Lakhs (INR)                |
| smoker       | bool     | Whether the person smokes                   |
| city         | str      | Name of the city                            |
| occupation   | str      | One of: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job` |

---

## 🧠 Derived Features (Auto-calculated)

- **BMI** = weight / height²
- **Age Group** = young / adult / middle_aged / senior
- **Lifestyle Risk** = high / medium / low
- **City Tier** = Based on pre-defined Tier-1 & Tier-2 cities

---

## 🎯 Prediction Output

```json
{
  "predicted_category": "High",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.01,
    "Medium": 0.15,
    "High": 0.84
  }
}
