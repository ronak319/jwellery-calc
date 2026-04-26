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

            # Check if the response contains the expected data
            if 'price_gram_24k' in data:
                # Get 24k gold price per gram in INR
                price_per_gram_24k = data['price_gram_24k']
                
                # Add Rajasthan/Bikaner regional premium
                adjusted_price = price_per_gram_24k * (1 + config.REGIONAL_PREMIUM)
                return round(adjusted_price, 2)
            else:
                # API returned unexpected format
                st.warning(f"GoldAPI returned unexpected format: {data}")
                
        except requests.RequestException as e:
            st.warning(f"GoldAPI request failed: {e}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check if the response contains the expected data
            if 'rates' in data and 'XAU' in data['rates']:
                # XAU is gold price in USD per troy ounce
                usd_per_ounce = data['rates']['XAU']
                
                # Convert to INR per gram
                inr_per_gram = (usd_per_ounce / config.TROY_OUNCE_TO_GRAMS) * config.USD_TO_INR_RATE
                
                # Add Rajasthan regional premium
                adjusted_price = inr_per_gram * (1 + config.REGIONAL_PREMIUM)
                
                return round(adjusted_price, 2)
            else:
                # API returned unexpected format
                st.warning(f"MetalPriceAPI returned unexpected format: {data}")
                
        except requests.RequestException as e:
            st.warning(f"MetalPriceAPI request failed: {e}")
    rate = base_rate + variation

    return max(rate, 45000)  # Minimum realistic rate