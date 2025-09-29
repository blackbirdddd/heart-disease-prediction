import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل النهائي
model = joblib.load('c:/Users/solim/OneDrive/Desktop/heart_disease_project/models/final_model.pkl')

st.title("🫀 Heart Disease Prediction App")

# الأعمدة المطلوبة (نفس ترتيب التدريب)
columns = [
 'age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca',
 'sex_Male_True', 'dataset_Hungary_True', 'dataset_VA Long Beach_True',
 'cp_atypical angina_True', 'cp_non-anginal_True', 'cp_typical angina_True',
 'fbs_True_True', 'restecg_normal_True', 'restecg_st-t abnormality_True',
 'exang_True_True', 'slope_flat_True', 'slope_upsloping_True',
 'thal_normal_True', 'thal_reversable defect_True'
]

# 📝 واجهة إدخال القيم
age = st.number_input("Age", 0, 120, 50)
trestbps = st.number_input("Resting Blood Pressure", 0, 300, 130)
chol = st.number_input("Cholesterol", 0, 600, 240)
thalch = st.number_input("Max Heart Rate", 0, 250, 150)
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0)
ca = st.number_input("Number of Major Vessels (0–4)", 0, 4, 0)

# باقي القيم One-Hot
sex_male = st.selectbox("Sex: Male?", [0, 1])
dataset_hungary = st.selectbox("Dataset Hungary?", [0, 1])
dataset_va = st.selectbox("Dataset VA Long Beach?", [0, 1])
cp_atypical = st.selectbox("Chest Pain: Atypical angina?", [0, 1])
cp_nonanginal = st.selectbox("Chest Pain: Non-anginal?", [0, 1])
cp_typical = st.selectbox("Chest Pain: Typical angina?", [0, 1])
fbs_true = st.selectbox("Fasting Blood Sugar True?", [0, 1])
restecg_normal = st.selectbox("Rest ECG Normal?", [0, 1])
restecg_st = st.selectbox("Rest ECG ST-T abnormality?", [0, 1])
exang_true = st.selectbox("Exercise Induced Angina?", [0, 1])
slope_flat = st.selectbox("Slope: Flat?", [0, 1])
slope_up = st.selectbox("Slope: Upsloping?", [0, 1])
thal_normal = st.selectbox("Thal: Normal?", [0, 1])
thal_rev = st.selectbox("Thal: Reversable defect?", [0, 1])

# ترتيب القيم بنفس ترتيب الأعمدة
user_input = [[
    age, trestbps, chol, thalch, oldpeak, ca,
    sex_male, dataset_hungary, dataset_va,
    cp_atypical, cp_nonanginal, cp_typical,
    fbs_true, restecg_normal, restecg_st,
    exang_true, slope_flat, slope_up,
    thal_normal, thal_rev
]]

user_df = pd.DataFrame(user_input, columns=columns)

# زر التنبؤ
if st.button("🔍 Predict"):
    prediction = model.predict(user_df)[0]
    if prediction == 1:
        st.error("⚠️ Model predicts: **Heart Disease**")
    else:
        st.success("✅ Model predicts: **No Heart Disease**")

    st.write("📊 Input data sent to model:")
    st.dataframe(user_df)
