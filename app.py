import streamlit as st

# TODO: Future features and improvements for the Jewelry Calculator app
# - Fetch live gold prices from API and historical gold rates of last 30 days, last 12 months, last 10 years. every 10 years
# - gold related news and nudge to buy sell or wait
# - Add invoice generator functionality
# - Implement saving calculations with item names


# Fix: Remove the indentation inside the triple quotes and check argument name
st.markdown("""
<style>
.main { background-color: #f5f5f5; }
div[data-testid="stMetricValue"] { font-size: 24px; color: #ffff00; font-weight: bold; }
</style>
""", unsafe_allow_html=True) # Changed from unsafe_allow_index to unsafe_allow_html

st.title("💎 Jewelry Calculator")
st.subheader(" Mamol Baid ज्वेलरी गणना")


# Input Section
with st.container():
    rate_24k = st.number_input("1 gm सोने का भाव (24K Rate)", value=15000, step=100)
    weight = st.number_input("कुल वजन (Net Weight)", value=10.000, step=0.001, format="%.3f")
    purity = st.number_input("शुद्धता % (Purity)", value=85.0, step=0.1)
    cust_making = st.number_input("घड़ाई % ( Making %)", value=13.0, step=0.1)


# --- 1. Basic Fine Gold Weight ---
# This was missing or named differently, causing the NameError
fine_gold = weight * (purity / 100)

# --- 2. Customer Side Calculations ---
price_customer = rate_24k * weight * ((purity + cust_making) / 100)
fine_making_cust = weight * (cust_making / 100)
total_fine_cust = fine_gold + fine_making_cust

# --- 3. Mom's Side Calculations ---
# Mom's cost formula: (Weight * Purity * Rate) * 1.08
price_mom = (weight * (purity / 100) * rate_24k) * 1.08
fine_making_mom = fine_gold * 0.08
total_fine_mom = fine_gold + fine_making_mom

# --- 4. Profit Calculations ---
commission = price_customer - price_mom
fine_profit = total_fine_cust - total_fine_mom

if price_customer > 0:
    margin_pct = (commission / price_customer) * 100
else:
    margin_pct = 0

# Calculate Khad Weight
khad_weight = weight - fine_gold

st.divider()

# Jewelry Details Section
with st.container():
    st.markdown("### 💎 **Jewelry Details**")
    jewel_col1, jewel_col2 = st.columns(2)
    with jewel_col1:
        st.metric("⚖️ Pure Gold Weight", f"{fine_gold:.3f} g")
    with jewel_col2:
        st.metric("🔄 Khad Weight", f"{khad_weight:.3f} g")

st.divider()

# Ledger Form: Customer (Left) and Mom/Sonar (Right)
ledger_col1, ledger_col2 = st.columns(2)

with ledger_col1:
    with st.container():
        st.subheader("👤 ग्राहक का हिसाब (Customer Account)")
        st.metric("💰 ग्राहक की कीमत", f"₹{price_customer:,.0f}")
        st.success(f"**कुल जमा फाइन:** {total_fine_cust:.3f}g")

with ledger_col2:
    with st.container():
        st.subheader("🏪 सुनार/मम्मी का हिसाब (Sonar/Mom Account)")
        st.metric("💰 सुनार की कीमत", f"₹{price_mom:,.0f}")
        st.info(f"**कुल लागत फाइन:** {total_fine_mom:.3f}g")

st.divider()

# Overall Profit Section
with st.container():
    st.markdown("### 🎯 **Overall Profit**")
    profit_col1, profit_col2, profit_col3 = st.columns(3)
    with profit_col1:
        st.metric("💵 Total Profit", f"₹{commission:,.0f}")
    with profit_col2:
        st.metric("⚖️ Fine Gold Profit", f"{fine_profit:.3f}g")
    with profit_col3:
        st.metric("📊 Profit Margin", f"{margin_pct:.2f}%")

if commission < 0:
    st.error("⚠️ Warning: Selling below cost!")
elif commission > 0:
    st.balloons()