import streamlit as st

st.set_page_config(page_title="Jewelry Calc", page_icon="💎")

# UI Styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stMetric { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_index=True)

st.title("💎 Jewelry Calculator")
st.write("हजारीमल सुगन चंद बैद - ज्वेलरी गणना")

# Input Section
with st.container():
    rate_24k = st.number_input("सोने का भाव (24K Rate)", value=75000, step=100)
    weight = st.number_input("कुल वजन (Net Weight)", value=10.000, step=0.001, format="%.3f")
    purity = st.number_input("शुद्धता % (Purity/Touch)", value=91.60, step=0.1)
    cust_making = st.number_input("ग्राहक घड़ाई % (Customer Making %)", value=12.0, step=0.1)

# Math Logic
# 1. Cost to Customer = Gold * NetWeight * (Purity + Making)
price_customer = rate_24k * weight * ((purity + cust_making) / 100)

# 2. Cost to Mom = (NetWeight * Purity) * (1 + 8% flat)
# Note: Purity here is used as a decimal (e.g., 0.916)
price_mom = (weight * (purity / 100) * rate_24k) * 1.08

# 3. Profit
commission = price_customer - price_mom

st.divider()

# Results Display
col1, col2 = st.columns(2)
col1.metric("ग्राहक की कीमत", f"₹{price_customer:,.0f}")
col2.metric("मम्मी की लागत", f"₹{price_mom:,.0f}")

st.subheader(f"आपका मुनाफा: ₹{commission:,.0f}")

if commission < 0:
    st.error("Warning: Selling below cost!")
elif commission > 0:
    st.balloons()