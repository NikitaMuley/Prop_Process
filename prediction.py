# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:37:56 2024

@author: NHande2
"""

import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('gradient_boost_machine_model.pkl', 'rb'))

#--------------------------------------------------------------------------------

def prop_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return 'Sorry, the opportunity will be LOST'
    else:
      return 'Hurray ! Opportunity will be a WIN'
  
#--------------------------------------------------------------------------------

def main():
    
    # giving a title
    st.title('Process Proposal Prediction Web App')
    
    
    # getting the input data from the user
    RA_Product_Cost = st.number_input('RA Product Cost >>', format="%.2f")
    RA_Product_Quote= st.number_input('RA Product Quote >>', format="%.2f")
    RA_Labor_Hours= st.number_input('RA Labour Hours >>', format="%.2f")
    RA_Labor_Cost= st.number_input('RA Labour Cost', format="%.2f")
    RA_Labor_Quote= st.number_input('RA_Labor_Quote', format="%.2f")
    RA_Service_Hours= st.number_input('RA_Service_Hours', format="%.2f")
    RA_Service_Cost= st.number_input('RA_Service_Cost', format="%.2f")
    RA_Service_Quote= st.number_input('RA_Service_Quote', format="%.2f")
    Third_Party_Hours= st.number_input('Third_Party_Hours', format="%.2f")
    Third_Party_Cost= st.number_input('Third_Party_Cost', format="%.2f")
    Third_Party_Quote= st.number_input('Third_Party_Quote', format="%.2f")
    Recovered_Project_Cost= st.number_input('Recovered_Project_Cost', format="%.2f")
    Recovered_Project_Quote= st.number_input('Recovered_Project_Quote', format="%.2f")
    Absorbed_Project_Cost= st.number_input('Absorbed_Project_Cost', format="%.2f")
    Absorbed_Project_Quote= st.number_input('Absorbed_Project_Quote', format="%.2f")
    Total_Project_Hours= st.number_input('Total_Project_Hours', format="%.2f")
    Total_Project_Cost= st.number_input('Total_Project_Cost', format="%.2f")
    Total_Project_Quote= st.number_input('Total_Project_Quote', format="%.2f")
    Reporting_Price_US= st.number_input('Reporting_Price_US', format="%.2f")
    KPI_BlendLaborRate= st.number_input('KPI_BlendLaborRate', format="%.2f")
    KPI_BlendLaborCost= st.number_input('KPI_BlendLaborCost', format="%.2f")
    
    # code for Prediction
    Proposal_Process_status = ''
    
    # creating a button for Prediction
    
    if st.button('Status (Win/ Lost) >>'):
        Proposal_Process_status = prop_prediction([RA_Product_Cost,RA_Product_Quote,RA_Labor_Hours,
                                   RA_Labor_Cost,RA_Labor_Quote,RA_Service_Hours,
                                   RA_Service_Cost,RA_Service_Quote,Third_Party_Hours,
                                   Third_Party_Cost,Third_Party_Quote,
                                   Recovered_Project_Cost,Recovered_Project_Quote,
                                   Absorbed_Project_Cost,Absorbed_Project_Quote,
                                   Total_Project_Hours,Total_Project_Cost,
                                   Total_Project_Quote,Reporting_Price_US,
                                   KPI_BlendLaborRate,KPI_BlendLaborCost])
        
        
    st.success(Proposal_Process_status)

if __name__=="__main__":
    main()
