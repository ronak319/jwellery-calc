# API utilities for fetching gold rates

import streamlit as st
import requests
from datetime import datetime
import config

@st.cache_data
def get_historical_gold_rate(date):
    """
    Fetch historical gold rate for Bikaner, Rajasthan
    Uses GoldAPI.io as primary source, MetalPriceAPI as fallback
    """
    # Try GoldAPI.io first (better INR support)
    gold_api_key = st.secrets.get("gold_api_key", None)

    if gold_api_key:
        url = f"{config.GOLD_API_BASE_URL}/XAU/INR/{date.strftime('%Y-%m-%d')}"
        headers = {"x-access-token": gold_api_key}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Get 24k gold price per gram in INR
            price_per_gram_24k = data.get('price_gram_24k', 0)

            if price_per_gram_24k > 0:
                # Add Rajasthan/Bikaner regional premium
                adjusted_price = price_per_gram_24k * (1 + config.REGIONAL_PREMIUM)
                return round(adjusted_price, 2)

        except requests.RequestException:
            pass  # Fall back to MetalPriceAPI

    # Fallback to MetalPriceAPI
    metal_api_key = st.secrets.get("metal_api_key", None)

    if metal_api_key:
        url = f"{config.METAL_API_BASE_URL}/{date.strftime('%Y-%m-%d')}?api_key={metal_api_key}&base=USD&currencies=XAU"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # XAU is gold price in USD per troy ounce
            usd_per_ounce = data['rates']['XAU']

            # Convert to INR per gram
            inr_per_gram = (usd_per_ounce / config.TROY_OUNCE_TO_GRAMS) * config.USD_TO_INR_RATE

            # Add Rajasthan regional premium
            adjusted_price = inr_per_gram * (1 + config.REGIONAL_PREMIUM)

            return round(adjusted_price, 2)

        except requests.RequestException:
            pass

    # Final fallback to mock data with Rajasthan-specific base rate
    st.warning("⚠️ Using estimated rates for Bikaner, Rajasthan. Add API keys for real data.")

    # Rajasthan typically has slightly higher rates than national average
    base_rate = 55000  # Approximate 24k gold rate in Rajasthan (₹ per gram)
    days_diff = (datetime.now().date() - date).days

    # Simulate market variation
    variation = (days_diff % 100 - 50) * 50  # Reduced variation for stability
    rate = base_rate + variation

    return max(rate, 45000)  # Minimum realistic rate