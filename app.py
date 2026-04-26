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
    <div style="font-family: Arial, sans-serif; max-width: 200px;">
        <input type="text" id="calc-display" style="width: 100%; height: 40px; font-size: 18px; text-align: right; margin-bottom: 10px;" readonly>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px;">
            <button onclick="appendToDisplay('7')" style="height: 40px; font-size: 16px;">7</button>
            <button onclick="appendToDisplay('8')" style="height: 40px; font-size: 16px;">8</button>
            <button onclick="appendToDisplay('9')" style="height: 40px; font-size: 16px;">9</button>
            <button onclick="appendToDisplay('/')" style="height: 40px; font-size: 16px;">/</button>
            
            <button onclick="appendToDisplay('4')" style="height: 40px; font-size: 16px;">4</button>
            <button onclick="appendToDisplay('5')" style="height: 40px; font-size: 16px;">5</button>
            <button onclick="appendToDisplay('6')" style="height: 40px; font-size: 16px;">6</button>
            <button onclick="appendToDisplay('*')" style="height: 40px; font-size: 16px;">*</button>
            
            <button onclick="appendToDisplay('1')" style="height: 40px; font-size: 16px;">1</button>
            <button onclick="appendToDisplay('2')" style="height: 40px; font-size: 16px;">2</button>
            <button onclick="appendToDisplay('3')" style="height: 40px; font-size: 16px;">3</button>
            <button onclick="appendToDisplay('-')" style="height: 40px; font-size: 16px;">-</button>
            
            <button onclick="appendToDisplay('0')" style="height: 40px; font-size: 16px;">0</button>
            <button onclick="appendToDisplay('.')" style="height: 40px; font-size: 16px;">.</button>
            <button onclick="calculate()" style="height: 40px; font-size: 16px; background-color: #4CAF50; color: white;">=</button>
            <button onclick="appendToDisplay('+')" style="height: 40px; font-size: 16px;">+</button>
        </div>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 5px; margin-top: 10px;">
            <button onclick="applyPercent()" style="height: 40px; font-size: 16px; background-color: #2196F3; color: white;">%</button>
            <button onclick="clearDisplay()" style="height: 40px; font-size: 16px; background-color: #f44336; color: white;">Clear</button>
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
    
    st.components.v1.html(calculator_html, height=300)

# Page routing
if st.session_state.current_page == "home":
    show_home_page()
elif st.session_state.current_page == "historical":
    show_historical_page()

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

def show_historical_page():
    st.title("📈 Historical Gold Rates")
    
    st.markdown("### Select a date to check historical gold rates")
    
    # Date selector
    selected_date = st.date_input("Select Date", value=datetime.now() - timedelta(days=1), 
                                  min_value=datetime.now() - timedelta(days=365*10),
                                  max_value=datetime.now() - timedelta(days=1))
    
    if st.button("Get Gold Rate", key="get_rate"):
        with st.spinner("Fetching historical gold rate..."):
            # Mock API call - in real app, use actual gold price API
            rate = get_historical_gold_rate(selected_date)
            st.success(f"Gold rate on {selected_date.strftime('%Y-%m-%d')}: ₹{rate:,.0f} per gram (24K)")
            
            # Show some additional info
            st.info("This is a demo. In production, this would fetch real historical data from a gold price API.")

@st.cache_data
def get_historical_gold_rate(date):
    # Mock function - replace with real API call
    # For demo, return a rate based on date
    base_rate = 50000  # Base rate
    days_diff = (datetime.now() - date).days
    # Simulate price variation
    variation = (days_diff % 100 - 50) * 100  # Random-ish variation
    rate = base_rate + variation
    return max(rate, 30000)  # Minimum rate