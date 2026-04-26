# CSS styles for the Jewelry Calculator app

MAIN_STYLES = """
<style>
.main { background-color: #f5f5f5; }
div[data-testid="stMetricValue"] { font-size: 24px; color: #ffff00; font-weight: bold; }
</style>
"""

CALCULATOR_STYLES = """
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
"""