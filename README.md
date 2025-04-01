# Crop Recommendation System

## 📌 Description
The **Crop Recommendation System** is a **machine learning-based web application** that helps farmers determine the most suitable crop for their land based on various environmental factors. It takes inputs like **Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH value, Rainfall, and Frost Risk** and provides a **recommended crop** that would thrive under those conditions.

---

## 🚀 Features
- Predict the most suitable crop based on environmental conditions
- Uses **machine learning** models for accurate predictions
- Web-based application using **Flask (backend) and HTML/CSS/JavaScript (frontend)**
- Simple and interactive **user interface**

---

## 📥 Input Factors

| Factor        | Description                         | Unit  |
|--------------|-------------------------------------|-------|
| **Nitrogen** | Amount of nitrogen in the soil     | mg/kg |
| **Phosphorus** | Amount of phosphorus in the soil   | mg/kg |
| **Potassium** | Amount of potassium in the soil    | mg/kg |
| **Temperature** | Temperature of the environment | °C    |
| **Humidity** | Humidity level in the air         | %     |
| **pH** | pH value of the soil                | -     |
| **Rainfall** | Amount of rainfall received        | mm    |
| **Frost Risk** | Risk of frost affecting crops    | -     |

---

## 🛠️ Technologies Used

### 🔹 Programming Languages & Libraries
- **Python** (for backend and machine learning)
- **Flask** (web framework)
- **Scikit-Learn** (machine learning model)
- **Pandas, NumPy** (data manipulation)
- **Matplotlib, Seaborn** (data visualization)

### 🔹 Frontend & UI
- **HTML, CSS, JavaScript**
- **Bootstrap** (for responsive design)

### 🔹 Database
- **CSV dataset** containing environmental and crop data

---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tanudhaka/Crop-Recommendation-System.git
```

### 2️⃣ Navigate to the Project Directory
```bash
cd Crop-Recommendation-System
```

### 3️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment
- **For Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **For macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 5️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Flask Application
```bash
python app.py
```

### 7️⃣ Open the Application in Browser
After running `app.py`, open your browser and visit:
```
http://127.0.0.1:5000/
```

Now, you can start using the **Crop Recommendation System**!

---

## 🧪 Machine Learning Model

The system uses **classification algorithms** to predict the best crop. The dataset contains historical **agricultural data** related to **crop yields, soil composition, and weather conditions**.

### 🔹 Steps in Model Development
1. **Data Collection** – Used a **public dataset** with crop and soil data  
2. **Data Preprocessing** – Cleaned missing values and normalized the data  
3. **Feature Selection** – Selected the **most important parameters**  
4. **Model Training** – Used **classification algorithms (e.g., Decision Trees, Random Forest, SVM, etc.)**  
5. **Model Evaluation** – Compared performance using **accuracy, precision, recall, and F1-score**  

---

## 📌 Example Predictions

| **Nitrogen** | **Phosphorus** | **Potassium** | **Temperature (°C)** | **Humidity (%)** | **pH** | **Rainfall (mm)** | **Frost Risk** | **Recommended Crop** |
|------------|------------|------------|----------------|------------|------|------------|------------|------------------|
| 90         | 42         | 43         | 25.4           | 80.3       | 6.5  | 200        | 0          | Rice             |
| 120        | 60         | 50         | 30.0           | 70.2       | 7.0  | 150        | 1          | Wheat            |
| 75         | 30         | 40         | 20.5           | 60.0       | 6.8  | 100        | 0          | Maize            |

---

#
