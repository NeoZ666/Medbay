import streamlit as st

def predict_drug(age, sex, bp, cholesterol, na_k):
    input_features = [[age, sex, bp, cholesterol, na_k]]
    prediction = model.predict(input_features)
    return prediction

st.title('Drug prediction')

with st.form("my_form"):    
    age = st.slider("Select Age", min_value=0, max_value=120, value=20)
    na_k = st.slider("Enter Sodium to potassium ratio in blood (Na to k)", min_value=6.000, max_value=39.000, value=6.000)
    sex = st.radio("Sex", options=["Male", "Female"])
    bp = st.radio("Blood Pressure", options=["Low", "Medium", "High"])
    cholesterol = st.radio("Cholesterol", options=["Medium", "High"])

    submitted = st.form_submit_button("Submit")

if submitted:
    sex = 1 if sex == "Male" else 0
    bp = {"Low": 0, "Medium": 1, "High": 2}[bp]
    cholesterol = {"Low": 0, "Medium": 1, "High": 2}[cholesterol]
    drug = predict_drug(age, sex, bp, cholesterol, na_k)
    st.write("Predicted drug:", drug)
