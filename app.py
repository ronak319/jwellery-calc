import streamlit as st
import requests
from datetime import datetime, timedelta

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

# Navigation
pages = {
    "Home": "home",
    "Historical Gold Rates": "historical"
}

if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# Sidebar navigation
st.sidebar.title("Navigation")
for page_name, page_key in pages.items():
    if st.sidebar.button(page_name, key=f"nav_{page_key}"):
        st.session_state.current_page = page_key

# Sidebar Calculator
with st.sidebar:
    st.header("🧮 कैलकुलेटर")
    
    # Embed HTML Calculator
    calculator_html = """
    <style>
        .calc-container {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            max-width: 220px;
        }
        .calc-display {
            width: 100%;
            height: 45px;
            font-size: 20px;
            text-align: right;
            margin-bottom: 15px;
            padding: 5px 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            background-color: white;
            color: #333;
            font-weight: bold;
        }
        .calc-button {
            height: 45px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            margin: 2px;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: bold;
        }
        .calc-button:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .number-btn {
            background-color: #ffffff;
            color: #333;
            border: 1px solid #ddd;
        }
        .operator-btn {
            background-color: #e0e0e0;
            color: #333;
        }
        .equals-btn {
            background-color: #4CAF50;
            color: white;
        }
        .percent-btn {
            background-color: #2196F3;
            color: white;
        }
        .clear-btn {
            background-color: #f44336;
            color: white;
        }
        .calc-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 5px;
        }
        .calc-bottom {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 5px;
            margin-top: 10px;
        }
    </style>
    
    <div class="calc-container">
        <input type="text" id="calc-display" class="calc-display" readonly>
        <div class="calc-grid">
            <button onclick="appendToDisplay('7')" class="calc-button number-btn">7</button>
            <button onclick="appendToDisplay('8')" class="calc-button number-btn">8</button>
            <button onclick="appendToDisplay('9')" class="calc-button number-btn">9</button>
            <button onclick="appendToDisplay('/')" class="calc-button operator-btn">/</button>
            
            <button onclick="appendToDisplay('4')" class="calc-button number-btn">4</button>
            <button onclick="appendToDisplay('5')" class="calc-button number-btn">5</button>
            <button onclick="appendToDisplay('6')" class="calc-button number-btn">6</button>
            <button onclick="appendToDisplay('*')" class="calc-button operator-btn">*</button>
            
            <button onclick="appendToDisplay('1')" class="calc-button number-btn">1</button>
            <button onclick="appendToDisplay('2')" class="calc-button number-btn">2</button>
            <button onclick="appendToDisplay('3')" class="calc-button number-btn">3</button>
            <button onclick="appendToDisplay('-')" class="calc-button operator-btn">-</button>
            
            <button onclick="appendToDisplay('0')" class="calc-button number-btn">0</button>
            <button onclick="appendToDisplay('.')" class="calc-button number-btn">.</button>
            <button onclick="calculate()" class="calc-button equals-btn">=</button>
            <button onclick="appendToDisplay('+')" class="calc-button operator-btn">+</button>
        </div>
        <div class="calc-bottom">
            <button onclick="applyPercent()" class="calc-button percent-btn">%</button>
            <button onclick="clearDisplay()" class="calc-button clear-btn">Clear</button>
        </div>
    </div>
    
    <script>
        function appendToDisplay(value) {
            document.getElementById('calc-display').value += value;
        }
        
        function clearDisplay() {
            document.getElementById('calc-display').value = '';
        }
        
        function applyPercent() {
            let current = document.getElementById('calc-display').value;
            if (current) {
                let num = parseFloat(current);
                if (!isNaN(num)) {
                    document.getElementById('calc-display').value = (num / 100).toString();
                }
            }
        }
        
        function calculate() {
            try {
                let result = eval(document.getElementById('calc-display').value);
                document.getElementById('calc-display').value = result;
            } catch (error) {
                document.getElementById('calc-display').value = 'Error';
            }
        }
        
        // Allow keyboard input
        document.addEventListener('keydown', function(event) {
            const key = event.key;
            if (key >= '0' && key <= '9') {
                appendToDisplay(key);
            } else if (key === '+' || key === '-' || key === '*' || key === '/' || key === '.') {
                appendToDisplay(key);
            } else if (key === '%') {
                applyPercent();
            } else if (key === 'Enter') {
                calculate();
            } else if (key === 'Escape') {
                clearDisplay();
            }
        });
    </script>
    """
    
    st.html(calculator_html)

def show_historical_page():
    st.title("📈 Historical Gold Rates - Bikaner, Rajasthan")
    
    st.markdown("### Select a date to check historical gold rates in Bikaner, Rajasthan")
    st.markdown("*Rates include regional premium for Rajasthan market conditions*")
    
    # Date selector
    selected_date = st.date_input("Select Date", value=datetime.now() - timedelta(days=1), 
                                  min_value=datetime.now() - timedelta(days=365*10),
                                  max_value=datetime.now() - timedelta(days=1))
    
    if st.button("Get Gold Rate", key="get_rate"):
        with st.spinner("Fetching historical gold rate for Bikaner, Rajasthan..."):
            rate = get_historical_gold_rate(selected_date)
            st.success(f"Gold rate in Bikaner on {selected_date.strftime('%Y-%m-%d')}: ₹{rate:,.0f} per gram (24K)")
            
            # Show some additional info
            st.info("Rates include Rajasthan regional premium. Add API keys in secrets.toml for real-time data.")

@st.cache_data
def get_historical_gold_rate(date):
    # Gold rates in India vary slightly by region due to local taxes and demand
    # Bikaner (Rajasthan) typically follows national rates with minor local premiums
    
    # Try GoldAPI.io first (better INR support than MetalPriceAPI)
    gold_api_key = st.secrets.get("gold_api_key", None)
    
    if gold_api_key:
        # Fetch from GoldAPI.io (free tier: 1,000 requests/month)
        url = f"https://www.goldapi.io/api/XAU/INR/{date.strftime('%Y-%m-%d')}"
        headers = {"x-access-token": gold_api_key}
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Get 24k gold price per gram in INR
            price_per_gram_24k = data.get('price_gram_24k', 0)
            
            if price_per_gram_24k > 0:
                # Add Rajasthan/Bikaner regional premium (typically 0.5-1% higher than national average)
                regional_premium = 0.008  # 0.8% premium for Bikaner region
                adjusted_price = price_per_gram_24k * (1 + regional_premium)
                return round(adjusted_price, 2)
                
        except requests.RequestException:
            pass  # Fall back to MetalPriceAPI
    
    # Fallback to MetalPriceAPI
    metal_api_key = st.secrets.get("metal_api_key", None)
    
    if metal_api_key:
        # Fetch from MetalPriceAPI
        url = f"https://api.metalpriceapi.com/v1/{date.strftime('%Y-%m-%d')}?api_key={metal_api_key}&base=USD&currencies=XAU"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # XAU is gold price in USD per troy ounce
            usd_per_ounce = data['rates']['XAU']
            
            # Convert to INR per gram
            # 1 troy ounce = 31.1035 grams
            # Using approximate USD to INR rate (in production, use currency API)
            usd_to_inr = 83.0
            inr_per_gram = (usd_per_ounce / 31.1035) * usd_to_inr
            
            # Add Rajasthan regional premium
            regional_premium = 0.008
            adjusted_price = inr_per_gram * (1 + regional_premium)
            
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

def show_home_page():
    st.title("💎 ज्वेलरी कैलकुलेटर")

    # Input Section
    with st.container():
        rate_24k = st.number_input("1 gm सोने का भाव", value=15000, step=100)
        weight = st.number_input("कुल वजन", value=10.000, step=0.001, format="%.3f")
        purity = st.number_input("शुद्धता %", value=85.0, step=0.1)
        cust_making = st.number_input("घड़ाई %", value=13.0, step=0.1)


    @st.cache_data
    def calculate_jewelry_metrics(rate_24k, weight, purity, cust_making):
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

    # Perform calculations
    fine_gold, price_customer, price_mom, commission, margin_pct, khad_weight, fine_making_cust, total_fine_cust, fine_making_mom, total_fine_mom, fine_profit = calculate_jewelry_metrics(
        rate_24k, weight, purity, cust_making
    )

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

# Page routing
if st.session_state.current_page == "home":
    show_home_page()
elif st.session_state.current_page == "historical":
    show_historical_page()