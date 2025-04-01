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



## 📸 Screenshots

#### 1️⃣ **Home Page**
![Home Page]![Home-1](https://github.com/user-attachments/assets/70c997fa-a4a4-4577-ba3a-a959f2f3e734)
![Home-2](https://github.com/user-attachments/assets/76524862-49f2-4e3b-8859-4485d33a8e5e)


#### 3️⃣ **User Input Form**
![User Input]![Input-1](https://github.com/user-attachments/assets/47a1e2af-81c5-4c69-8164-f55dfd7318bd)
![Input-2](https://github.com/user-attachments/assets/5a8bee58-a009-408c-9ba8-e8adc79d4da5)

#### 2️⃣ **Prediction Result Page**
![Prediction Result]![Output](https://github.com/user-attachments/assets/54053d24-1889-4472-8e56-c16a7838bbd1)


