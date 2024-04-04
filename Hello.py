import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

Data = pd.read_csv('drug200.csv')

Data.dropna(subset=['Drug'], inplace=True)

y = Data['Drug']
X = Data.drop(columns='Drug')

X_num = X.copy()
X_num['Sex'] = X_num['Sex'].map({'M': 0, 'F': 1})
X_num['Cholesterol'] = X_num['Cholesterol'].map({'NORMAL': 0, 'HIGH': 1})
X_num['BP'] = X_num['BP'].map({'LOW': 0, 'NORMAL': 1, 'HIGH': 2})

y_num = y.map({'drugA': 0, 'drugB': 1, 'drugC': 2, 'drugX': 3, 'DrugY': 4})
print(y_num)

imputer = SimpleImputer(strategy='mean')
X_num_imputed = imputer.fit_transform(X_num)

RandomForest = RandomForestClassifier(n_estimators=760, criterion='gini', max_depth=6, min_samples_split=2,
                                      min_samples_leaf=9, max_features=None, max_leaf_nodes=33,
                                      class_weight=None)
RandomForestModel = RandomForest.fit(X_num_imputed, y_num)

num_to_drug = {0: 'drugA', 1: 'drugB', 2: 'drugC', 3: 'drugX', 4: 'DrugY'}

def predict_drug(age, sex, bp, cholesterol, na_k):
    sex = 1 if sex == "Male" else 0
    bp = {"Low": 0, "Medium": 1, "High": 2}[bp]
    cholesterol = {"Medium": 0, "High": 1}[cholesterol]
    input_features = [[age, sex, bp, cholesterol, na_k]]
    prediction = RandomForestModel.predict(input_features)
    return num_to_drug[prediction[0]]

st.title('Drug prediction')

with st.form("my_form"):    
    age = st.slider("Select Age", min_value=0, max_value=120, value=20)
    na_k = st.slider("Enter Sodium to potassium ratio in blood (Na to k)", min_value=6.000, max_value=39.000, value=6.000)
    sex = st.radio("Sex", options=["Male", "Female"])
    bp = st.radio("Blood Pressure", options=["Low", "Medium", "High"])
    cholesterol = st.radio("Cholesterol", options=["Medium", "High"])

    submitted = st.form_submit_button("Submit")

if submitted:
    drug = predict_drug(age, sex, bp, cholesterol, na_k)
    st.write("Predicted drug:", drug)
