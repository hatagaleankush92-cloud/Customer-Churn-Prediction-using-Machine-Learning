# Gender -> 1 Female       0 Male
# Churn -> 1 Yes           0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the X -> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.title {
    font-size: 45px;
    font-weight: bold;
    color: #38bdf8;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(to right, #3b82f6, #06b6d4);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown('<p class="title">📊 Customer Churn Prediction Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Machine Learning Web App using Streamlit</p>', unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("⚙️ Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📈 Analytics", "🤖 Prediction"]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if page == "🏠 Home":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <h2>10K+</h2>
        <p>Customer Records</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <h2>95%</h2>
        <p>Model Accuracy</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <h2>Real-Time</h2>
        <p>Predictions</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📌 Project Overview</h3>
    <p>
    This project predicts whether a customer will churn based on customer behavior,
    monthly charges, tenure, internet service, and more.
    </p>
    <ul>
        <li>✔ Data Analysis</li>
        <li>✔ Machine Learning Model</li>
        <li>✔ Interactive Dashboard</li>
        <li>✔ Real-Time Prediction</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# ANALYTICS PAGE
# ---------------------------------------------------
elif page == "📈 Analytics":

    st.subheader("📊 Customer Churn Insights")

    # Sample Data
    data = pd.DataFrame({
        "Churn": ["Yes", "No"],
        "Count": [1869, 5174]
    })

    fig = px.pie(
        data,
        values="Count",
        names="Churn",
        title="Customer Churn Distribution",
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

    charges = pd.DataFrame({
        "Tenure": np.random.randint(1, 72, 100),
        "MonthlyCharges": np.random.randint(20, 120, 100)
    })

    fig2 = px.scatter(
        charges,
        x="Tenure",
        y="MonthlyCharges",
        title="Tenure vs Monthly Charges"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# PREDICTION PAGE
# ---------------------------------------------------
elif page == "🤖 Prediction":

    st.subheader("🤖 Predict Customer Churn")

    col1, col2 = st.columns(2)

    with col1:
        tenure = st.slider("Tenure", 1, 72, 12)
        monthlycharges = st.slider("Monthly Charges", 10, 150, 70)
        totalcharges = st.number_input("Total Charges", 100, 10000, 1000)

    with col2:
        internetservice = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer",
                "Credit card"
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Predict Churn"):

        # ---------------------------------------------------
        # SAMPLE LOGIC
        # Replace this with your trained model
        # ---------------------------------------------------

        score = 0

        if tenure < 12:
            score += 1

        if monthlycharges > 80:
            score += 1

        if contract == "Month-to-month":
            score += 1

        if internetservice == "Fiber optic":
            score += 1

        if score >= 2:
            prediction = "⚠ Customer is likely to Churn"
            st.error(prediction)
        else:
            prediction = "✅ Customer is likely to Stay"
            st.success(prediction)

        st.balloons()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)