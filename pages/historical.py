# Historical gold rates page for the Jewelry Calculator app

import streamlit as st
from datetime import datetime, timedelta
import config
from utils.api import get_historical_gold_rate

def show_historical_page():
    """Display the historical gold rates page"""
    st.title("📈 Historical Gold Rates - Bikaner, Rajasthan")

    st.markdown("### Select a date to check historical gold rates in Bikaner, Rajasthan")
    st.markdown("*Rates include regional premium for Rajasthan market conditions*")

    # Date selector
    selected_date = st.date_input(
        "Select Date",
        value=datetime.now() - timedelta(days=config.MIN_HISTORICAL_DAYS),
        min_value=datetime.now() - timedelta(days=config.MAX_HISTORICAL_DAYS),
        max_value=datetime.now() - timedelta(days=config.MIN_HISTORICAL_DAYS)
    )

    if st.button("Get Gold Rate", key="get_rate"):
        with st.spinner("Fetching historical gold rate for Bikaner, Rajasthan..."):
            rate = get_historical_gold_rate(selected_date)
            st.success(f"Gold rate in Bikaner on {selected_date.strftime('%Y-%m-%d')}: ₹{rate:,.0f} per gram (24K)")

            # Show some additional info
            st.info("Rates include Rajasthan regional premium. Add API keys in secrets.toml for real-time data.")