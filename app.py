import streamlit as st 
import pickle 
import numpy as np 

model = pickle.load(open('model.pkl','rb'))

st.title("predictive Maintenance System")

air_temp = st.number_input("Air Temperature")
process_temp = st.number_input("process Temperature")
rot_speed = st.number_input("Rotational Speed")
torque = st.number_input("Torque")
tool_wear = st.number_input("Tool Wear")

type_L = st.selectbox("Type L",[0,1])
type_M = st.selectbox("Type M",[0,1])

if st.button("predict"): 
    input_data = np.array([[air_temp,process_temp,rot_speed,torque,tool_wear,type_L,type_M]])
    prediction = model.predict(input_data)
    if prediction[0] == 1: 
               st.error("Machine Failure Likely")
    else:
               st.success("Machine is Safe")