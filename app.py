import streamlit as st
import pickle
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from chatbot.chatbot_logic import chatbot_response

# Load model
model_path = os.path.join("model", "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.set_page_config(page_title="Smart Building Cost Estimator", layout="wide")

# --------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.header {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #2c3e50;
    padding: 20px;
}

/* CARD */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(to right, #3498db, #6dd5fa);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

div.stButton > button:hover {
    transform: scale(1.05);
}

/* CHAT */
.chatbox {
    background-color: #ecf0f1;
    padding: 10px;
    border-radius: 10px;
}

/* METRIC */
.metric {
    font-size: 28px;
    font-weight: bold;
    color: #27ae60;
}
</style>
""", unsafe_allow_html=True)

# --------- HEADER ----------
st.markdown("<div class='header'>🏗 Smart Building Cost Estimation</div>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

# --------- INPUT SECTION ----------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🏠 Building Details")

    c1, c2 = st.columns(2)

    with c1:
        area = st.number_input("Area (sq ft)", 500, 5000)
        floors = st.number_input("Floors", 1, 5)
        location = st.selectbox("Location", ["Rural", "Semi-Urban", "Urban"])
        material = st.selectbox("Material Quality", ["Low", "Medium", "High"])

    with c2:
        labor = st.slider("Labor Cost Index", 0.8, 1.5)
        building_type = st.selectbox("Building Type", ["Residential", "Commercial"])
        parking = st.selectbox("Parking", ["No", "Yes"])
        basement = st.selectbox("Basement", ["No", "Yes"])
        year = st.slider("Year", 2015, 2025)

    # Encoding
    location_map = {"Rural": 0, "Semi-Urban": 1, "Urban": 2}
    material_map = {"Low": 0, "Medium": 1, "High": 2}
    type_map = {"Residential": 0, "Commercial": 1}
    yes_no = {"No": 0, "Yes": 1}

    if st.button("🚀 Estimate Cost"):
        features = np.array([[area, floors,
                              location_map[location],
                              material_map[material],
                              labor,
                              type_map[building_type],
                              yes_no[parking],
                              yes_no[basement],
                              year]])

        prediction = model.predict(features)[0]

        st.markdown(f"""
        <div class='card'>
            <h3>💰 Estimated Cost</h3>
            <p class='metric'>₹ {round(prediction, 2)}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --------- DASHBOARD ----------
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Quick Info")

    st.metric("Area", f"{area} sq ft")
    st.metric("Floors", floors)
    st.metric("Location", location)

    st.markdown("</div>", unsafe_allow_html=True)

# --------- CHATBOT ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("💬 AI Assistant")

user_input = st.text_input("Ask something about construction")

if user_input:
    response = chatbot_response(user_input)
    st.markdown(f"<div class='chatbox'>🤖 {response}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --------- GRAPHS ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Data Insights")

data = pd.read_csv("data/building_data.csv")

# Graph 1
st.write("### Area vs Cost")
fig1 = plt.figure()
plt.scatter(data["area"], data["cost"])
plt.xlabel("Area")
plt.ylabel("Cost")
st.pyplot(fig1)

# Graph 2
st.write("### Feature Importance")
importances = model.feature_importances_
features = data.drop("cost", axis=1).columns

fig2 = plt.figure()
plt.barh(features, importances)
st.pyplot(fig2)

st.markdown("</div>", unsafe_allow_html=True)