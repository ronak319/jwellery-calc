# Home page for the Jewelry Calculator app

import streamlit as st
from datetime import datetime, timedelta
import config
from utils.api import get_historical_gold_rate

@st.cache_data
def calculate_jewelry_metrics(rate_24k, weight, purity, cust_making):
    """Calculate jewelry metrics including costs and profits"""
    # --- 1. Basic Fine Gold Weight ---
    fine_gold = weight * (purity / 100)

    # --- 2. Customer Side Calculations ---
    price_customer = rate_24k * weight * ((purity + cust_making) / 100)
    fine_making_cust = weight * (cust_making / 100)
    total_fine_cust = fine_gold + fine_making_cust

    # --- 3. Mom's Side Calculations ---
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

    return fine_gold, price_customer, price_mom, commission, margin_pct, khad_weight, fine_making_cust, total_fine_cust, fine_making_mom, total_fine_mom, fine_profit

def show_home_page():
    """Display the home page with jewelry calculator"""
    st.title("💎 ज्वेलरी कैलकुलेटर")

    # Input Section
    with st.container():
        rate_24k = st.number_input("1 gm सोने का भाव", value=config.DEFAULT_RATE_24K, step=100)
        weight = st.number_input("कुल वजन", value=config.DEFAULT_WEIGHT, step=0.001, format="%.3f")
        purity = st.number_input("शुद्धता %", value=config.DEFAULT_PURITY, step=0.1)
        cust_making = st.number_input("घड़ाई %", value=config.DEFAULT_MAKING_CHARGE, step=0.1)

    st.divider()

    # Perform calculations
    fine_gold, price_customer, price_mom, commission, margin_pct, khad_weight, fine_making_cust, total_fine_cust, fine_making_mom, total_fine_mom, fine_profit = calculate_jewelry_metrics(
        rate_24k, weight, purity, cust_making
    )

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