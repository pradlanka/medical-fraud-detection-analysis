import streamlit as st 
import pandas as pd
import numpy as np
from prediction import predict

st.title('Classifying fraduent medical providers')
st.markdown('Model to classify fradulent medical providers')


st.header("Provider features")
col1, col2 = st.columns(2)
with col1:
    st.text("In-patient characterisitcs")
    IP_days_in_hospital = st.number_input('Average stay of in-patient claims', min_value=0, max_value=40)
    IP_TotalClaims = st.number_input('Total no of in-patient claims filed by the provider', min_value=0, max_value=500)
with col2:
    st.text("Out-patient characteristics")
    OP_TotalClaims = st.number_input('Total no of out-patient claims filed by the provider', min_value=0, max_value=40)
    OP_RenalDiseaseIndicator =st.number_input('Fraction of patients with renal disease in Outpatient claims', min_value=0.00, max_value=1.00, format="%.2f", step=0.01)
    OP_NoClmDiagnosisCodes  = st.number_input('Total no of outpatient diganosis codes in claims filed by the provider', min_value=0, max_value=20)

st.text('')
if st.button("Predict whether provider is fradulent"):
    result = predict(np.array([OP_TotalClaims, IP_days_in_hospital, OP_RenalDiseaseIndicator, IP_TotalClaims, OP_NoClmDiagnosisCodes]).reshape(1, -1))
    if result <= 0.5:
       # st.text("Provider is not fradulent with probability " + str(round(1.0-result)), color='green')
        st.markdown(f'<h1 style="color:#008000;font-size:24px;">{"Proivder is not fraudulent with probability of "+ str(round(1.0-result,2))}</h1>', unsafe_allow_html=True)
    else:
        #st.text("Provider is fradulent with probability " + str(round(result,2)), color = 'red')
        st.markdown(f'<h1 style="color:#FF0000;font-size:24px;">{"Proivder is fraudulent with probability of "+ str(round(result,2))}</h1>', unsafe_allow_html=True)