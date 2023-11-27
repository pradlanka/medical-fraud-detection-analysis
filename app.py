import streamlit as st 
import pandas as pd
import numpy as np
from prediction import predict

st.title('Classifying fraduent medical providers')
st.markdown('Model to classify fradulent medical providers')


st.header("Provider features")
col1, col2 = st.columns(2)
with col1:
    st.text("IP characterisitcs")
    IP_days_in_hospital = st.number_input('IP_days_in_hospital', min_value=0, max_value=40)
    IP_TotalClaims = st.number_input('Total Claims', min_value=0, max_value=500)
with col2:
    st.text("OP characteristics")
    OP_TotalClaims = st.number_input('OP_TotalClaims', min_value=0, max_value=40)
    OP_RenalDiseaseIndicator =st.number_input('OP_RenalDiseaseIndicator', min_value=0.00, max_value=1.00, format="%.2f", step=0.01)
    OP_NoClmDiagnosisCodes  = st.number_input('OP_NoClmDiagnosisCodes', min_value=0, max_value=20)

st.text('')
if st.button("Predict whether provider is fradulent"):
    result = predict(np.array([OP_TotalClaims, IP_days_in_hospital, OP_RenalDiseaseIndicator, IP_TotalClaims, OP_NoClmDiagnosisCodes]).reshape(1, -1))
    if result[0] == 0:
        st.text("Provider is not fradulent")
    else:
        st.text("Provider is fradulent")