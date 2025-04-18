import streamlit as st

def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    # Convert to meters first
    meters = value * to_meters[from_unit]
    # Convert from meters to target unit
    return meters / to_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion factors to grams
    to_grams = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lb': 453.592,
        'ton': 907185
    }
    
    # Convert to grams first
    grams = value * to_grams[from_unit]
    # Convert from grams to target unit
    return grams / to_grams[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == '°F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:  # from_unit == '°C'
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == '°F':
        return (celsius * 9/5) + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:  # to_unit == '°C'
        return celsius

def main():
    st.title("Unit Converter")
    
    # Sidebar for conversion type selection
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"]
    )
    
    if conversion_type == "Length":
        units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
    elif conversion_type == "Weight":
        units = ['mg', 'g', 'kg', 'oz', 'lb', 'ton']
    else:  # Temperature
        units = ['°C', '°F', 'K']
    
    # Input section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        value = st.number_input("Enter value", value=1.0)
    
    with col2:
        from_unit = st.selectbox("From", units)
    
    with col3:
        to_unit = st.selectbox("To", units)
    
    # Convert button
    if st.button("Convert"):
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        else:  # Temperature
            result = convert_temperature(value, from_unit, to_unit)
        
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

if __name__ == "__main__":
    main()
