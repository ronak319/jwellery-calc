# Configuration and constants for the Jewelry Calculator app

# API Configuration
GOLD_API_BASE_URL = "https://www.goldapi.io/api"
METAL_API_BASE_URL = "https://api.metalpriceapi.com/v1"

# Regional settings for Bikaner, Rajasthan
REGIONAL_PREMIUM = 0.008  # 0.8% premium for Rajasthan
USD_TO_INR_RATE = 83.0    # Approximate USD to INR conversion

# Gold conversion constants
TROY_OUNCE_TO_GRAMS = 31.1035

# UI Constants
DEFAULT_RATE_24K = 15000
DEFAULT_WEIGHT = 10.000
DEFAULT_PURITY = 85.0
DEFAULT_MAKING_CHARGE = 13.0

# Date limits for historical data
MAX_HISTORICAL_DAYS = 365 * 10  # 10 years back
MIN_HISTORICAL_DAYS = 1         # Yesterday minimum