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

st.title("💎 ज्वेलरी कैलकुलेटर")

# Sidebar Calculator
with st.sidebar:
    st.header("🧮 कैलकुलेटर")
    
    # Calculator state
    if 'calc_display' not in st.session_state:
        st.session_state.calc_display = "0"
    
    # Display
    st.text_input("Display", value=st.session_state.calc_display, key="calc_display_input", disabled=True)
    
    # Button layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("7", key="btn7"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "7"
            else:
                st.session_state.calc_display += "7"
            st.rerun()
        
        if st.button("4", key="btn4"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "4"
            else:
                st.session_state.calc_display += "4"
            st.rerun()
        
        if st.button("1", key="btn1"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "1"
            else:
                st.session_state.calc_display += "1"
            st.rerun()
        
        if st.button("0", key="btn0"):
            if st.session_state.calc_display != "0":
                st.session_state.calc_display += "0"
            st.rerun()
    
    with col2:
        if st.button("8", key="btn8"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "8"
            else:
                st.session_state.calc_display += "8"
            st.rerun()
        
        if st.button("5", key="btn5"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "5"
            else:
                st.session_state.calc_display += "5"
            st.rerun()
        
        if st.button("2", key="btn2"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "2"
            else:
                st.session_state.calc_display += "2"
            st.rerun()
        
        if st.button(".", key="btn_dot"):
            if "." not in st.session_state.calc_display:
                st.session_state.calc_display += "."
            st.rerun()
    
    with col3:
        if st.button("9", key="btn9"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "9"
            else:
                st.session_state.calc_display += "9"
            st.rerun()
        
        if st.button("6", key="btn6"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "6"
            else:
                st.session_state.calc_display += "6"
            st.rerun()
        
        if st.button("3", key="btn3"):
            if st.session_state.calc_display == "0":
                st.session_state.calc_display = "3"
            else:
                st.session_state.calc_display += "3"
            st.rerun()
        
        if st.button("=", key="btn_equals"):
            try:
                result = eval(st.session_state.calc_display)
                st.session_state.calc_display = str(result)
            except:
                st.session_state.calc_display = "Error"
            st.rerun()
    
    with col4:
        if st.button("/", key="btn_div"):
            st.session_state.calc_display += "/"
            st.rerun()
        
        if st.button("*", key="btn_mul"):
            st.session_state.calc_display += "*"
            st.rerun()
        
        if st.button("-", key="btn_sub"):
            st.session_state.calc_display += "-"
            st.rerun()
        
        if st.button("+", key="btn_add"):
            st.session_state.calc_display += "+"
            st.rerun()
    
    # Clear button
    if st.button("Clear", key="btn_clear"):
        st.session_state.calc_display = "0"
        st.rerun()

# Input Section
with st.container():
    rate_24k = st.number_input("1 gm सोने का भाव", value=15000, step=100)
    weight = st.number_input("कुल वजन", value=10.000, step=0.001, format="%.3f")
    purity = st.number_input("शुद्धता %", value=85.0, step=0.1)
    cust_making = st.number_input("घड़ाई %", value=13.0, step=0.1)


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
    st.markdown("### 💎 **ज्वेलरी डिटेल**")
    jewel_col1, jewel_col2 = st.columns(2)
    with jewel_col1:
        st.metric("⚖️ शुद्ध सोना वजन", f"{fine_gold:.3f} g")
    with jewel_col2:
        st.metric("🔄 खाद वजन", f"{khad_weight:.3f} g")

st.divider()

# Ledger Form: Customer (Left) and Mom/Sonar (Right)
ledger_col1, ledger_col2 = st.columns(2)

with ledger_col1:
    with st.container():
        st.subheader("👤 ग्राहक का हिसाब")
        st.metric("💰 ग्राहक की कीमत", f"₹{price_customer:,.0f}")
        st.write(f"**शुद्ध सोना:** {fine_gold:.3f}g")
        st.write(f"**घड़ाई फाइन:** {fine_making_cust:.3f}g")
        st.success(f"**कुल जमा फाइन:** {total_fine_cust:.3f}g")

with ledger_col2:
    with st.container():
        st.subheader("🏪 सुनार का हिसाब")
        st.metric("💰 सुनार की कीमत", f"₹{price_mom:,.0f}")
        st.write(f"**शुद्ध सोना:** {fine_gold:.3f}g")
        st.write(f"**घड़ाई फाइन:** {fine_making_mom:.3f}g")
        st.info(f"**कुल लागत फाइन:** {total_fine_mom:.3f}g")

st.divider()

# Overall Profit Section
with st.container():
    st.markdown("### 🎯 **कुल मुनाफा**")
    profit_col1, profit_col2, profit_col3 = st.columns(3)
    with profit_col1:
        st.metric("💵 कुल मुनाफा", f"₹{commission:,.0f}")
    with profit_col2:
        st.metric("⚖️ फाइन गोल्ड मुनाफा", f"{fine_profit:.3f}g")
    with profit_col3:
        st.metric("📊 मुनाफा %", f"{margin_pct:.2f}%")

if commission < 0:
    st.error("⚠️ चेतावनी: लागत से नीचे बेच रहे हैं!")