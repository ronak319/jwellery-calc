import streamlit as st
from utils.styles import MAIN_STYLES
from components.calculator import get_calculator_component
from pages.home import show_home_page
from pages.historical import show_historical_page

# Apply main styles
st.markdown(MAIN_STYLES, unsafe_allow_html=True)

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
    calculator_html = get_calculator_component()
    st.html(calculator_html)

# Page routing
if st.session_state.current_page == "home":
    show_home_page()
elif st.session_state.current_page == "historical":
    show_historical_page()
