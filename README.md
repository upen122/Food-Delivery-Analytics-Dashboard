# 🚀 Food Delivery Analytics Dashboard

A real-time food delivery analytics dashboard built with **PySpark**, **AWS S3**, and **Plotly Dash**. This project demonstrates a scalable data pipeline from data ingestion to cloud storage and interactive visualization.

---

## 📊 Project Overview

This project processes a raw food delivery dataset using **Apache Spark**, stores the cleaned data on **AWS S3**, and visualizes insights through a professional **Plotly Dash dashboard** — all done interactively within **Google Colab**.

---

## 🔧 Tech Stack

- **PySpark** – ETL and data transformation  
- **Google Colab** – Development environment  
- **AWS S3** – Cloud storage for cleaned data  
- **Plotly Dash** – Interactive dashboard in Python  
- **ngrok** – Tunnel Colab apps to the public  
- **Pandas / NumPy** – Data manipulation  
- **GitHub** – Version control and deployment  

---

## 🛠️ Pipeline Architecture

```mermaid
flowchart TD
    A[Raw Dataset (CSV)] --> B[PySpark ETL in Google Colab]
    B --> C[Cleaned DataFrame]
    C --> D[Upload to AWS S3]
    C --> E[Visualized via Plotly Dash]
    D --> F[Cloud-Based Analytics Dashboard]
```

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
[LinkedIn]([https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/upen-singh-546999341/)) | [GitHub](https://github.com/upen122)

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
