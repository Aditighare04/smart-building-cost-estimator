import streamlit as st
from model.predict import predict_cost

st.title("🏗 Smart Building Cost Estimation System")

st.write("Enter building details to estimate cost.")

# Inputs
area = st.number_input("Area (sq ft)", min_value=100)
floors = st.number_input("Number of Floors", min_value=1)

location = st.selectbox("Location Type", ["Rural", "Urban", "Metro"])
material = st.selectbox("Material Quality", ["Low", "Medium", "High"])
building_type = st.selectbox("Building Type", ["Residential", "Commercial"])

# Button
if st.button("Estimate Cost"):

    if area > 0 and floors > 0:
        cost, cost_per_sqft = predict_cost(area, floors, location, material, building_type)

        st.success(f"Estimated Cost: ₹ {cost}")
        st.info(f"Cost per Sq Ft: ₹ {cost_per_sqft}")
    else:
        st.error("Please enter valid inputs")