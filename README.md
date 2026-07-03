# 🎓 Student Placement Prediction

## 👨‍💻 Author

**Abhishek Thakur**

Integrated M.Tech (Artificial Intelligence)

VIT Bhopal

GitHub: https://github.com/Abthakur-hub

A Machine Learning web application that predicts whether a student is likely to get placed based on their academic performance and other factors.

The application is built using **Python**, **Flask**, **Scikit-learn**, and **Docker**, and provides an interactive web interface for making predictions.

---

## 🚀 Demo

**Local URL**

```
http://localhost:5001
```

---

## 📌 Features

* Predict student placement using Machine Learning
* Random Forest Classifier
* User-friendly Flask web interface
* Responsive HTML & CSS frontend
* Docker support
* Easy deployment on Render

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML5
* CSS3
* Docker
* Joblib

---

## 📂 Project Structure

```text
Student-Placement-Docker/
│
├── dataset/
│   └── placement.csv
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train.py
├── placement_model.pkl
├── encoders.pkl
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## 📊 Dataset

Dataset used:

**Campus Placement Dataset (Kaggle)**

Features include:

* Gender
* SSC Percentage
* SSC Board
* HSC Percentage
* HSC Board
* HSC Stream
* Degree Percentage
* Degree Type
* Work Experience
* Employability Test Score
* MBA Specialisation
* MBA Percentage

Target:

* Placement Status (Placed / Not Placed)

---

## 🤖 Machine Learning Model

Algorithm used:

* Random Forest Classifier

Workflow:

1. Load Dataset
2. Data Cleaning
3. Label Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Save Model using Joblib
8. Prediction using Flask

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Student-Placement-Docker.git
```

Move into the project directory

```bash
cd Student-Placement-Docker
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train.py
```

Run the application

```bash
python app.py
```

---

## 🐳 Docker

Build the image

```bash
docker build -t student-placement .
```

Run the container

```bash
docker run -p 5001:5000 student-placement
```

Open

```
http://localhost:5001
```

---

## 📸 Screenshots

Add screenshots here after running the application.

Example:

* Home Page
* Prediction Result

---

## 📈 Future Improvements

* Prediction probability
* Model comparison
* Feature importance visualization
* Scikit-learn Pipeline
* Better UI/UX
* Cloud deployment

---


