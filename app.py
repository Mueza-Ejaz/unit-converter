import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom CSS for Styling & Removing Extra Space
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            padding-top: 0px !important;
            margin-top: -50px !important;
            background-color: #000000 !important;
        }
        [data-testid="stHeader"], [data-testid="stToolbar"] {
            display: none !important;
        }
        .block-container {
            padding-top: 0px !important;
            margin-top: -50px !important;
        }
        body {
            color: #ffffff !important;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 450px;
            margin: 40px auto;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
            text-align: center;
        }
        h1 {
            color: #00c8ff !important;
            font-size: 28px;
            font-weight: bold;
        }
        select, input {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 2px solid transparent !important;
            border-radius: 8px;
            padding: 12px; /* Increased padding for better appearance */
            width: 100%;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6); /* More prominent dark shadow */
            transition: box-shadow 0.3s ease-in-out;
        }
        select:focus, input:focus {
            outline: none; /* Remove outline on focus */
            box-shadow: 0 0 12px rgba(0, 200, 255, 0.8); /* Light blue glow on focus */
        }
        label {
            color: green !important;

        }
        .convert-btn {
            background: black;
            color: white;
            border: 2px solid #00c8ff;
            padding: 12px;
            border-radius: 8px;
            width: 100%;
            cursor: pointer;
            transition: 0.3s;
        }
        .convert-btn:hover {
            background: #00c8ff;
            color: black;
        }
        #MainMenu, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# UI Design
st.markdown('<div class="container">', unsafe_allow_html=True)
st.image('unit.png', width=100, use_container_width=False)

# Heading
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)

# User Inputs
number = st.number_input("Enter a number", min_value=0.0, format="%.6f")
units = ['foot', 'yard', 'inch', 'metre', 'kilometre', 'centimetre', 'millimetre', 
         'gram', 'kilogram', 'milligram', 'metric ton', 'litre', 'centilitre', 'millilitre']
option1 = st.selectbox('FROM: Select unit', units)
option2 = st.selectbox('TO: Select unit', units)

# Conversion Dictionary
conversion_factors = {
    ('inch', 'centimetre'): 2.54,
    ('centimetre', 'inch'): 1/2.54,
    ('millimetre', 'inch'): 1/25.4,
    ('inch', 'millimetre'): 25.4,
    ('inch', 'metre'): 1/39.37,
    ('metre', 'inch'): 39.37,
    ('foot', 'yard'): 1/3,
    ('yard', 'foot'): 3,
    ('yard', 'metre'): 1/1.0936,
    ('metre', 'yard'): 1.0936,
    ('foot', 'metre'): 1/3.2808,
    ('metre', 'foot'): 3.2808,
    ('foot', 'inch'): 12,
    ('inch', 'foot'): 1/12,
    ('kilometre', 'metre'): 1000,
    ('metre', 'kilometre'): 1/1000,
    ('centimetre', 'millimetre'): 10,
    ('millimetre', 'centimetre'): 1/10,
    ('gram', 'kilogram'): 1/1000,
    ('kilogram', 'gram'): 1000,
    ('gram', 'milligram'): 1000,
    ('milligram', 'gram'): 1/1000,
    ('litre', 'millilitre'): 1000,
    ('millilitre', 'litre'): 1/1000,
}

# Perform Conversion
if st.button('Calculate', key='convert-btn'):
    if number == 0:
        st.warning("Please enter a valid number greater than 0.")
    elif option1 == option2:
        st.success(f"Result: {number:.6f} {option2}")
    else:
        result = number * conversion_factors.get((option1, option2), "Invalid Conversion")
        time.sleep(1)
        if result == "Invalid Conversion":
            st.error("This conversion is not available. Please try another unit combination.")
        else:
            st.success(f"Result: {result:.6f} {option2}")

st.markdown("</div>", unsafe_allow_html=True)
