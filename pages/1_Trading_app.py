import streamlit as st
from PIL import Image

# Page Title
st.title("📊 Trading Guide App")
st.markdown("""
Welcome to the **Trading Guide App**  
We provide the most efficient platform to help you gather all essential information *before investing in stocks.*
""")

# Display Image
st.image("pages/app.webp", use_container_width=True)

st.markdown("---")

# Services Section
st.markdown("### 🚀 Services We Provide")

st.markdown("#### 1️⃣ Stock Information")
st.write("Access complete stock details including price history, company data, and market performance.")

st.markdown("#### 2️⃣ Stock Prediction")
st.write("View predicted stock closing prices for the next 30 days using forecasting models and past trends.")

st.markdown("#### 3️⃣ CAPM Return")
st.write("Understand how the **CAPM model** calculates expected return based on market risk.")

st.markdown("#### 4️⃣ CAPM Beta")
st.write("Calculate **Beta** and expected returns for selected stocks with precision.")

st.markdown("---")
st.markdown("🧭 *Use the sidebar to navigate to each feature.*")
