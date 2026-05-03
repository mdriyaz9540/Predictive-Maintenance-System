# 🚀 Predictive Maintenance System (End-to-End Data Science Project)
*Streamlit app = https://predictive-maintenance-system-dsg6sqlf9sqk4qc8anettn.streamlit.app/

## 📌 Project Overview

This project predicts whether a machine is likely to fail based on operational parameters such as temperature, speed, torque, and tool wear.

It is an end-to-end Data Science project covering:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning Model Building
* Handling Imbalanced Data
* Model Deployment using Streamlit

---

## 🎯 Problem Statement

In industrial environments, unexpected machine failures can lead to high costs.
This project aims to predict machine failure in advance using machine learning.

---

## 📂 Dataset

* Source: UCI Machine Learning Repository (AI4I 2020 Predictive Maintenance Dataset)
* Contains:

  * Machine parameters (temperature, speed, torque, wear)
  * Product type
  * Failure information

---

## 🧹 Data Preprocessing

* Removed irrelevant columns: `UDI`, `Product ID`
* Dropped failure-type columns (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) to avoid data leakage
* Encoded categorical variable `Type` using One-Hot Encoding

---

## 📊 Exploratory Data Analysis (EDA)

* Checked class imbalance in target variable
* Used heatmap to analyze correlations
* Used pairplot and scatter plots to study relationships
* Observed non-linear patterns in data

---

## ⚙️ Model Building

* Algorithm: Random Forest Classifier
* Reason:

  * Handles non-linear relationships
  * Works well on tabular data
* Split data into training and testing sets

---

## ⚖️ Handling Imbalanced Data

* Observed imbalance in failure class
* Used:

  * `class_weight='balanced'`
  * SMOTE (Synthetic Minority Oversampling)

---

## 📈 Model Evaluation

* Accuracy Score
* Precision, Recall, F1-score
* Focused on **Recall** for failure prediction

---

## 💾 Model Saving

* Used `pickle` to save trained model

---

## 🌐 Deployment

* Built web app using Streamlit
* User inputs machine parameters
* Model predicts failure in real-time

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit
* Pickle


## 📌 Future Improvements

* Hyperparameter tuning
* Feature importance visualization
* Better UI design
* Deploy on cloud platforms

---

## 👨‍💻 Author

Mohd Riyaz

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
