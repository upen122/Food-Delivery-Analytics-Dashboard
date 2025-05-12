<!-- Project Banner -->
<p align="center">
  <img src="https://img.shields.io/badge/Big%20Data-PySpark-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Cloud-AWS_S3-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dashboard-Plotly_Dash-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
</p>

<h1 align="center">📊 Food Delivery Analytics Dashboard</h1>

<p align="center">
  <em>A Big Data pipeline project that extracts, transforms, and visualizes real-world food delivery metrics using PySpark, AWS, and Dash.</em>
</p>

---

## 📚 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [📁 Dataset Information](#-dataset-information)
- [🧰 Tech Stack](#-tech-stack)
- [✨ Features](#-features)
- [🚀 How to Run](#-how-to-run)
- [📸 Dashboard Preview](#-dashboard-preview)
- [📤 Upload to AWS S3](#-upload-to-aws-s3)
- [🌐 Launch Dashboard using ngrok](#-launch-dashboard-using-ngrok)
- [🧠 What I Learned](#-what-i-learned)
- [🧑‍💻 Author](#-author)
- [🔗 Connect with Me](#-connect-with-me)

---

## 🔍 Project Overview

This project builds a complete **end-to-end Data Engineering & Visualization pipeline** using a real-world food delivery dataset. It leverages **PySpark** for scalable processing, stores cleaned data on **AWS S3**, and builds a **dynamic interactive dashboard** using **Plotly Dash**.

🎯 **Goal:** Derive operational insights to improve delivery performance, analyze delivery times, and understand the impact of weather, traffic, and festivals on customer experience.

---

## 📁 Dataset Information

- 📦 Source: Kaggle Food Delivery Dataset  
- 🎯 Contains attributes like:
  - Delivery ratings, time, weather, traffic conditions
  - Rider details (age, experience, vehicle condition)
  - Festival and multi-order indicators
  - City zones, restaurant, and delivery locations

---

## 🧰 Tech Stack

| Layer               | Technology             |
|--------------------|------------------------|
| Language           | Python 3.x             |
| Big Data Processing| PySpark (Google Colab) |
| Cloud Storage      | AWS S3 (via `boto3`)   |
| Visualization      | Plotly Dash            |
| Notebook           | Jupyter (Colab)        |
| Version Control    | Git + GitHub           |

---

## ✨ Features

- ✅ **ETL Pipeline** using PySpark DataFrames
- ✅ **Null & Duplicate Handling**, Data Cleaning, Type Casting
- ✅ **AWS S3 Integration** for cloud storage of cleaned data
- ✅ **Real-Time Dashboard** with interactive graphs
- ✅ **Insights on**:
  - Impact of Weather/Traffic
  - Festival-time Delivery Trends
  - Rider Ratings vs Delivery Timings
  - Multi-order Effects

---

## 📤 Upload to AWS S3

import boto3

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY',
                        aws_secret_access_key='YOUR_SECRET_KEY')

# Upload the file
s3.upload_file('cleaned_data.csv', 'your-bucket-name', 'cleaned_data/cleaned_data.csv')

print("File uploaded to S3 successfully.")

---

## 🌐 Launch Dashboard using ngrok

Step 1: Install pyngrok
bash
Copy
Edit
pip install pyngrok
Step 2: Run ngrok tunnel
python
Copy
Edit
from pyngrok import ngrok

# Open tunnel on port 8050 (Dash default)
public_url = ngrok.connect(8050)
print(f"Public URL: {public_url}")
Step 3: Run your Dash app in another terminal
bash
Copy
Edit
python app.py
