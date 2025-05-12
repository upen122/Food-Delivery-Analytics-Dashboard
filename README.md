# 🚚 Food Delivery Analytics Dashboard – Big Data Pipeline Project

![PySpark](https://img.shields.io/badge/PySpark-BigData-blue)
![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Dash](https://img.shields.io/badge/Dashboard-Plotly-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Overview

This project presents a **Big Data Pipeline** designed to analyze food delivery data using **PySpark**, store clean datasets on **AWS S3**, and visualize insights through an **interactive dashboard** built with **Dash (Plotly)**.

The pipeline processes real-world delivery data with multiple features like weather, traffic, delivery time, and rider performance, offering meaningful analytics for decision-making.

---

## 📁 Dataset

- Source: [Kaggle - Delivery Dataset](https://www.kaggle.com/)
- Fields include:
  - Delivery Person Age & Ratings
  - Restaurant & Delivery Coordinates
  - Traffic & Weather Conditions
  - Festival Impact
  - Time taken for delivery
  - Multiple deliveries, Vehicle condition, City, and more

---

## ⚙️ Technologies Used

| Layer | Tech Stack |
|-------|------------|
| Data Processing | `PySpark` on `Google Colab` |
| Cloud Storage | `AWS S3` |
| Visualization | `Dash` + `Plotly` |
| Programming | `Python` |
| Version Control | `Git` + `GitHub` |

---

## 🛠️ Key Features

- ✅ **Big Data Handling** using PySpark
- ✅ **Data Cleaning & Transformation** (nulls, dtypes, outliers)
- ✅ **Upload Cleaned Data to AWS S3**
- ✅ **Interactive Dashboard** to explore:
  - Delivery Time vs Ratings
  - Traffic and Weather Conditions
  - Festival Impacts
  - Rider and City-based Analytics

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Food-Delivery-Analytics-Dashboard.git
   cd Food-Delivery-Analytics-Dashboard

---

## ⚙️ Features

- ✅ Real-time ETL processing using PySpark  
- ✅ Data cleaning and transformation  
- ✅ Upload cleaned data to AWS S3  
- ✅ Build and run a Dash-based interactive dashboard  
- ✅ Run everything from Google Colab  
- ✅ GitHub-ready project structure  

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/upen122/Food-Delivery-Analytics-Dashboard.git
cd Food-Delivery-Analytics-Dashboard
```

### 2. Upload Your Raw Dataset

Upload your `train.csv` into Google Colab or place it in the local directory for testing.

### 3. Install Required Libraries (in Google Colab)

```python
!pip install pyspark pandas boto3 plotly dash pyngrok
```

### 4. Run the PySpark ETL Code

- Load the CSV
- Clean and transform using PySpark
- Convert to Pandas DataFrame
- Save as `cleaned_food_data.csv`

### 5. Upload Cleaned Data to AWS S3

Configure your AWS credentials in Colab:

```python
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id="YOUR_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY"
)

s3.upload_file("cleaned_food_data.csv", "your-bucket-name", "cleaned_food_data.csv")
```

### 6. Launch Dashboard with ngrok

```python
!pip install pyngrok
from pyngrok import ngrok
public_url = ngrok.connect(8050)
print("Dashboard URL:", public_url)
```

---

## 📁 Folder Structure

```
📦 Food-Delivery-Analytics-Dashboard
├── 📁 colab_notebooks
│   └── ETL_and_Dashboard.ipynb
├── 📁 data
│   ├── raw
│   └── processed
├── 📁 dashboard
│   └── app.py
├── README.md
└── requirements.txt
```

---

## 📸 Screenshots

> *(Add screenshots of your dashboard here)*  
> ![dashboard-screenshot](assets/dashboard-example.png)

---

## 🧑‍💼 Author

**Upen**  
Data Engineering Enthusiast  
[LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/upen122)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Future Enhancements

- Add user login & authentication  
- Deploy permanently on EC2 or Render  
- Integrate real-time Kafka stream  
- Add dashboard filters and charts by cuisine, location, etc.

---

Feel free to ⭐ this repo if it helped you!

