import streamlit as st

st.title('Drug prediction')
with st.form("my_form"):    
    age = st.slider("Select Age",min_value=0, max_value=120, value=20)

    Na_k = st.slider("Enter Sodium to potassium ratio in blood (Na to k)",min_value=6.000, max_value=39.000, value=6.000)

    sex = st.radio(
        "Sex",
        key="visibility",
        options=["Male", "Female"],
    )

    bp = st.radio(
        "Blood Pressure",
        options=["Low", "Medium", "High"],
    )

    Cholesterol = st.radio(
        "Cholesterol",
        options=["Low", "Medium", "High"],
    )


    st.form_submit_button(label="Submit")