import streamlit as st

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
    purity = st.number_input("शुद्धता % (Purity)", value=85, step=0.1)
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

# Ledger Form: Customer (Left) and Mom/Sonar (Right)
ledger_col1, ledger_col2 = st.columns(2)

with ledger_col1:
    st.subheader("ग्राहक का हिसाब (Customer Account)")
    st.metric("ग्राहक की कीमत", f"₹{price_customer:,.0f}")
    
    st.write("**फाइन गोल्ड डिटेल (Fine Gold Details)**")
    st.write(f"शुद्ध सोना (Fine): {fine_gold:.3f}g")
    st.write(f"घड़ाई फाइन (Making Fine): {fine_making_cust:.3f}g")
    st.info(f"कुल जमा फाइन: {total_fine_cust:.3f}g")
    
    st.metric("शुद्ध सोना (Fine Gold)", f"{fine_gold:.3f} g")
    st.metric("खाद वजन (Khad Weight)", f"{khad_weight:.3f} g")

with ledger_col2:
    st.subheader("सुनार/मम्मी का हिसाब (Sonar/Mom Account)")
    st.metric("सुनार की कीमत", f"₹{price_mom:,.0f}")
    
    st.write("**फाइन गोल्ड डिटेल (Fine Gold Details)**")
    st.write(f"लागत फाइन (8% Making): {fine_making_mom:.3f}g")
    st.info(f"कुल लागत फाइन: {total_fine_mom:.3f}g")

st.divider()

# Overall Profit
st.metric("मुनाफा % (Margin over Sale)", f"{margin_pct:.2f}%")
st.subheader(f"आपका मुनाफा: ₹{commission:,.0f}")
st.success(f"कुल मुनाफा फाइन: {fine_profit:.3f} ग्राम")

if commission < 0:
    st.error("Warning: Selling below cost!")
elif commission > 0:
    st.balloons()