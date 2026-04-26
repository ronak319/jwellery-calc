import streamlit as st

# Fix: Remove the indentation inside the triple quotes and check argument name
st.markdown("""
<style>
.main { background-color: #f5f5f5; }
div[data-testid="stMetricValue"] { font-size: 24px; color: #d4af37; }
</style>
""", unsafe_allow_html=True) # Changed from unsafe_allow_index to unsafe_allow_html

st.title("💎 Jewelry Calculator")
st.subheader(" Mamol Baid ज्वेलरी गणना")


# Input Section
with st.container():
    rate_24k = st.number_input("1 gm सोने का भाव (24K Rate)", value=75000, step=100)
    weight = st.number_input("कुल वजन (Net Weight)", value=10.000, step=0.001, format="%.3f")
    purity = st.number_input("शुद्धता % (Purity)", value=91.60, step=0.1)
    cust_making = st.number_input("घड़ाई % ( Making %)", value=12.0, step=0.1)


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

# Results Display
col1, col2 = st.columns(2)
col1.metric("ग्राहक की कीमत", f"₹{price_customer:,.0f}")
col2.metric("सुनार की कीमत", f"₹{price_mom:,.0f}")

st.subheader(f"आपका मुनाफा: ₹{commission:,.0f}")
st.metric("मुनाफा % (Margin over Sale)", f"{margin_pct:.2f}%")

st.divider()
st.subheader("फाइन गोल्ड हिसाब (Fine Gold Ledger)")

f_col1, f_col2 = st.columns(2)
with f_col1:
    st.write("**ग्राहक का हिसाब (Customer Side)**")
    st.write(f"शुद्ध सोना (Fine): {fine_gold:.3f}g")
    st.write(f"घड़ाई फाइन (Making Fine): {fine_making_cust:.3f}g")
    st.info(f"कुल जमा फाइन: {total_fine_cust:.3f}g")

with f_col2:
    st.write("**मम्मी का हिसाब (Mom's Side)**")
    st.write(f"शुद्ध सोना (Fine): {fine_gold:.3f}g")
    st.write(f"लागत फाइन (8% Making): {fine_making_mom:.3f}g")
    st.info(f"कुल लागत फाइन: {total_fine_mom:.3f}g")

st.write("---")
st.subheader("पार्सा हिसाब (Fine Gold Parcha)")
col_a, col_b = st.columns(2)
col_a.metric("ग्राहक फाइन (Cust Total Fine)", f"{total_fine_cust:.3f}g")
col_b.metric("मम्मी फाइन (Mom Total Fine)", f"{total_fine_mom:.3f}g")
st.success(f"कुल मुनाफा फाइन: {fine_profit:.3f} ग्राम")


st.divider()
f_col1, f_col2 = st.columns(2)
with f_col1:
    st.metric("शुद्ध सोना (Fine Gold)", f"{fine_gold:.3f} g")
with f_col2:
    st.metric("खाद वजन (Khad Weight)", f"{khad_weight:.3f} g")

if commission < 0:
    st.error("Warning: Selling below cost!")
elif commission > 0:
    st.balloons()