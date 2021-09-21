##pip install streamlit
import streamlit as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="Seoul Bike Trip Duration Prediction App",
                   page_icon="🛴", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    distance = st.number_input("Distance: ", value=0, format="%d")
    plong = st.slider("Pickup Longitude: ", 37.0, 38.0, format="%f")
    platd = st.slider("Pickup Latitude: ", 126.0, 128.0, format="%f")
    haversine = st.number_input("Haversine: ")
    phour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
    pmin = st.slider("Pickup Minute: ", 0, 59, value=0, format="%d")
    pdweek = st.slider("PDWeek: ", 0, 6, value=0, format="%d")
    dmin = st.slider("Dropoff Minute: ", 0, 59, value=0, format="%d")
    Precip = st.number_input("Precipitation: ")
    wind = st.number_input("Wind: ")
    humid = st.number_input("Humid: ")
    solar = st.number_input("Solar: ")
    snow = st.number_input("snow: ")
    Groundtemp = st.number_input("Ground Temp: ")
    dust = st.number_input("Dust: ")

    submit_val = st.form_submit_button("Predict Duration")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([distance,plong,platd,haversine, phour,
                        pmin, pdweek,
                        dmin, Precip,wind,
                        humid, solar,snow,Groundtemp, dust]).reshape(1,-1)

    print (attribute)
    if attribute.shape == (1,15):
        print("attrubutes valid")
        

        value = predict_duration(attributes= attribute)


        st.header("Here are the results:")
        st.success(f"The Duration predicted is {value} mins")