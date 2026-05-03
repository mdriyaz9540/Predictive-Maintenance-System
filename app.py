import streamlit as st
import numpy as np
import pickle
import os

st.write("Files in directory:", os.listdir())

try:
    model = pickle.load(open('model.pkl', 'rb'))
    st.success("Model loaded successfully ✅")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("Predictive Maintenance System")

air_temp = st.number_input("Air Temperature", value=300.0)
process_temp = st.number_input("Process Temperature", value=310.0)
rot_speed = st.number_input("Rotational Speed", value=1500.0)
torque = st.number_input("Torque", value=40.0)
tool_wear = st.number_input("Tool Wear", value=100.0)

type_L = st.selectbox("Type L", [0, 1])
type_M = st.selectbox("Type M", [0, 1])

if st.button("Predict"):
    input_data = np.array([[air_temp, process_temp, rot_speed, torque, tool_wear, type_L, type_M]])

    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Machine Failure Likely")
        else:
            st.success("✅ Machine is Safe")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
