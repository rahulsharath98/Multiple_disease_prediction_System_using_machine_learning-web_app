# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:55:12 2024

@author: user
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open("D:/Multiple_disease_prediction_system/trained_model.sav",'rb'))

heart_disease_model = pickle.load(open("D:/Multiple_disease_prediction_system/Heart_disease_trained_model.sav",'rb'))

parkinsons_model = pickle.load(open("D:/Multiple_disease_prediction_system/Parkinsons_disease_trained_model.sav",'rb'))


# side bar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index=1
                           )
    
#Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title("Diabetes prediction using ML")
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies= st.text_input("Number of pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose level")
        
    with col3:
        BloodPressure= st.text_input("BloodPressure Level")
        
    with col1:
        SkinThickness= st.text_input("SkinThickness Level")
        
    with col2:
        Insulin= st.text_input("Insulin Level")
        
    with col3:
        BMI= st.text_input("BMI Level")
        
    with col1:
        DiabetesPedigreeFunction= st.text_input("DiabetesPedigreeFunction Level")
        
    with col2:
        Age= st.text_input("Age of the person")
    

    #code for prediction
    diagnosis = ""
    
    # creating a button for prediction
    if st.button("diabetes test result"):
        diagnosis_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diagnosis_prediction[0] == 1):
            diagnosis = 'The person is diabetic'
        else:
            diagnosis = 'The person is not diabetic'
    st.success(diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    
    st.title("Heart Disease prediction using ML")
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age	= st.text_input(" age of the person")
    with col2:
        sex = st.text_input("sex")
    with col3:
        cp= st.text_input("cp Level")
    
    with col1:
        trestbps= st.text_input("trestbps Level")
    with col2:
        chol= st.text_input("chol Level")
    with col3:
        fbs= st.text_input("fbs Level")
          
    with col1:
        restecg= st.text_input("restecg Level")
    with col2:
        thalach= st.text_input("thalach Level")
    with col3:
        exang= st.text_input("exang level")
        
    with col1:
        oldpeak= st.text_input("oldpeak")
    with col2:
        slope= st.text_input("slope")
    with col3:
        ca= st.text_input("ca level")
   
    with col1:
        thal= st.text_input("thal level")

    
    #code for prediction
    diagnosis = ""
    
    # creating a button for prediction
    if st.button("Heart_test result"):
        in_data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        in_data = [[float(x) for x in in_data]]
        diagnosis_prediction = heart_disease_model.predict(in_data)
        
        if(diagnosis_prediction[0]==1):
            diagnosis = 'The person has heart diease'
        else:
            diagnosis = 'The person does not have heart disease'
    st.success(diagnosis)
        
       
if (selected == 'Parkinsons Prediction'):
    
    st.title("Parkinsons prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    #geting input data  from the user
    with col1:
        MDVP_Fo= st.text_input(" MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVP_Flo= st.text_input("MDVP:Flo(Hz)")
        
    with col1:
        MDVP_Jitter_percentage= st.text_input("MDVP:Jitter(%)")
    with col2:
        MDVP_Jitter_Abs= st.text_input("MDVP:Jitter(Abs)")
    with col3:
        MDVP_RAP= st.text_input("MDVP:RAP")
        
    with col1:
        MDVP_PPQ= st.text_input("MDVP:PPQ")
    with col2:
        Jitter_DDP= st.text_input("Jitter:DDP")
    with col3:
        MDVP_Shimmer= st.text_input("MDVP:Shimmer")
        
    with col1:
        MDVP_Shimmer_dB= st.text_input("MDVP:Shimmer(dB)")
    with col2:
        Shimmer_APQ3= st.text_input("Shimmer:APQ3")
    with col3:
        Shimmer_APQ5= st.text_input("Shimmer:APQ5")
        
    with col1:
        MDVP_APQ= st.text_input("MDVP:APQ")
    with col2:
        Shimmer_DDA= st.text_input("Shimmer:DDA")
    with col3:
        NHR= st.text_input("NHR")
        
    with col1:
        HNR= st.text_input("HNR")
    with col2:
        RPDE= st.text_input("RPDE")
    with col3:
        DFA= st.text_input("DFA")
        
    with col1:
        spread1= st.text_input("spread1")
    with col2:
        spread2= st.text_input("spread2")
    with col3:
        D2	= st.text_input("D2")
        
    with col1:
        PPE= st.text_input("PPE")
    
    #code for prediction
    diagnosis = ""
    
    # creating a button for prediction
    if st.button("Parkinson's_test result"):
        in_data = [MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter_percentage,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        in_data = [[float(x) for x in in_data]]
        diagnosis_prediction = parkinsons_model.predict(in_data)
        
    st.success(diagnosis)
    
    if(diagnosis_prediction[0]==1):
        diagnosis = 'The person has Parkinsons diease'
    else:
        diagnosis = 'The person does not have Parkinsons disease'
st.success(diagnosis)
    
    

