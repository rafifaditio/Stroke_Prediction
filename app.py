import streamlit as st
import pandas as pd
import pickle

st.title("Stroke Prediction")

# import model
model = pickle.load(open("model.pkl", "rb"))

st.write('Insert feature to predict')

# user input
id = st.number_input(label='Id', min_value=0, max_value=99999999, value=0, step=1)
gender = st.selectbox(label='Gender', options=['Female', 'Male'], index=0)
age = st.number_input(label='Age', min_value=0, max_value=120, value=68, step=1)
hypertension = st.selectbox(label='Hypertension', options=[0, 1], index = 1, help='Label 0 merupakan tidak, label 1 merupakan iya')
heart_disease = st.selectbox(label='Heart Disease', options=[0, 1], index=1,  help='Label 0 merupakan tidak, label 1 merupakan iya')
ever_married = st.selectbox(label='Have you ever married', options=['Yes', 'No'])
work_type = st.selectbox(label='Which one describe your work?', options=['Private','Self-employed','Govt_job','Never_worked'], index=0)
residence_type = st.selectbox(label='Which one describe your residence area?', options=['Rural', 'Urban'])
avg_glucos = st.slider(label='Average Glucose Level', min_value=55.0, max_value=272.0, value=247.51, step=1.0)
bmi = st.number_input(label='BMI', min_value=10., max_value=100., value=40.5, step=1.)
smoking= st.selectbox(label='Are you smoking?', options=['never smoked', 'formerly smoked', 'smokes'], index=1)

# convert into dataframe
data = pd.DataFrame({'id': [id],
                    'gender': [gender],
                    'age': [age],
                    'hypertension': [hypertension],
                    'heart_disease': [heart_disease],
                    'ever_married': [ever_married],
                    'work_type': [work_type],
                    'Residence_type':[residence_type],
                    'avg_glucose_level':[avg_glucos],
                    'bmi':[bmi],
                    'smoking_status':[smoking]})


# model predict
if st.button(label='Predict'):
    clas = model.predict(data)[0]
    
    # interpretation
    st.write('Classification Result: ')
    if clas == 0:
        st.text('Not Stroke')
    elif clas == 1:
        st.text('Stroke')