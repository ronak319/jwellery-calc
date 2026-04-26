# jwellery-calc

A Streamlit-based jewelry calculator app for calculating gold jewelry prices and margins.

## Project Structure

```
jwellery-calc/
├── app.py                 # Main app with navigation and routing
├── config.py             # Constants and configuration
├── components/
│   └── calculator.py     # Calculator HTML component
├── pages/
│   ├── home.py          # Home page logic
│   └── historical.py    # Historical rates page logic
├── utils/
│   ├── api.py           # API functions for gold rates
│   └── styles.py        # CSS styles
└── requirements.txt
```

## Features

- Calculate jewelry prices with purity and making charges
- Interactive calculator in sidebar
- Historical gold rates lookup for Bikaner, Rajasthan
- Modular, maintainable code structure
- Real-time gold price integration

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

## API Integration

The app uses gold price APIs to provide rates specific to Bikaner, Rajasthan, India.

### Gold Rate APIs

Two APIs are supported for maximum reliability:

1. **GoldAPI.io** (Recommended)
   - Free tier: 1,000 requests/month
   - Direct INR pricing
   - Sign up: https://goldapi.io/

2. **Metal Price API** (Fallback)
   - Free tier: 50 requests/month
   - USD pricing (auto-converted to INR)
   - Sign up: https://metalpriceapi.com/

### Rajasthan/Bikaner Specific Rates

- Gold rates in Rajasthan are typically 0.5-1% higher than national averages
- The app automatically adds a 0.8% regional premium for Bikaner
- This accounts for local market conditions and transportation costs

### Setting up API Keys

1. Sign up for accounts at the API providers above
2. Get your API keys from their dashboards
3. Edit `.streamlit/secrets.toml`:
   ```toml
   gold_api_key = "your_actual_goldapi_key"
   metal_api_key = "your_actual_metal_key"
   ```

### Without API Keys

If no API keys are provided, the app uses estimated rates for Bikaner, Rajasthan with realistic market variations.

## Usage

- Use the calculator in the sidebar for basic calculations
- Navigate between Home and Historical Gold Rates pages
- Enter jewelry details to calculate prices and margins# jwellery-calc

A Streamlit-based jewelry calculator app for calculating gold jewelry prices and margins.

## Features

- Calculate jewelry prices with purity and making charges
- Interactive calculator in sidebar
- Historical gold rates lookup
- Multi-page navigation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

## API Integration

The app uses gold price APIs to provide rates specific to Bikaner, Rajasthan, India.

### Gold Rate APIs

Two APIs are supported for maximum reliability:

1. **GoldAPI.io** (Recommended)
   - Free tier: 1,000 requests/month
   - Direct INR pricing
   - Sign up: https://goldapi.io/

2. **Metal Price API** (Fallback)
   - Free tier: 50 requests/month
   - USD pricing (auto-converted to INR)
   - Sign up: https://metalpriceapi.com/

### Rajasthan/Bikaner Specific Rates

- Gold rates in Rajasthan are typically 0.5-1% higher than national averages
- The app automatically adds a 0.8% regional premium for Bikaner
- This accounts for local market conditions and transportation costs

### Setting up API Keys

1. Sign up for accounts at the API providers above
2. Get your API keys from their dashboards
3. Edit `.streamlit/secrets.toml`:
   ```toml
   gold_api_key = "your_actual_goldapi_key"
   metal_api_key = "your_actual_metal_key"
   ```

### Without API Keys

If no API keys are provided, the app uses estimated rates for Bikaner, Rajasthan with realistic market variations.

## Usage

- Use the calculator in the sidebar for basic calculations
- Navigate between Home and Historical Gold Rates pages
- Enter jewelry details to calculate prices and margins