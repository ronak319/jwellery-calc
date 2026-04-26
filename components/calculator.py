# Calculator HTML component for the Jewelry Calculator app

CALCULATOR_HTML = """
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

def get_calculator_component():
    """Returns the complete calculator HTML with styles"""
    return CALCULATOR_STYLES + CALCULATOR_HTML