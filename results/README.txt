🫀 HEART DISEASE PREDICTION PROJECT

📌 Project Description
This project uses machine learning techniques to predict the likelihood of heart disease based on patient health data.
The workflow includes:
- Data preprocessing and cleaning
- PCA analysis
- Feature selection
- Supervised and unsupervised learning
- Hyperparameter tuning
- Model exporting
- Streamlit UI for real-time predictions
- Optional Ngrok deployment

---

📁 Project Structure

Heart_Disease_Project/
│── data/
│   └── heart_disease_cleaned.csv
│── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_pca_analysis.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_supervised_learning.ipynb
│   ├── 05_unsupervised_learning.ipynb
│   ├── 06_hyperparameter_tuning.ipynb
│   └── 07_model_export.ipynb
│── models/
│   └── final_model.pkl
│── results/
│   ├── confusion_matrix.png
│   ├── model_comparison.png
│   └── evaluation_metrics.txt
│── ui/
│   └── app.py
│── deployment/
│   └── ngrok_setup.txt
│── requirements.txt
│── README.txt

---

🚀 How to Run the Project

1️⃣ Install Dependencies
Run the following command to install required libraries:
    pip install -r requirements.txt

2️⃣ Run Streamlit Web App
    streamlit run ui/app.py

3️⃣ (Optional) Deploy with Ngrok
    ngrok http 8501

---

🧠 Technologies Used
- Python 3.10
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Joblib
- Ngrok (for deployment)

---

📊 Results
- The best-performing model was tuned using GridSearchCV and RandomizedSearchCV.
- Model performance metrics and plots are available in the `results/` folder.

---

👤 Author
Developed by: Soliman  
GitHub: https://github.com/blackbirdddd

---

📄 License
This project is open-source and available under the MIT License.
