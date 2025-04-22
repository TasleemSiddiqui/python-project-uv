import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Simple Calculator")

# Create two columns for the calculator layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input fields
    num1 = st.number_input("First Number", value=0.0)
    num2 = st.number_input("Second Number", value=0.0)

with col2:
    # Operation selection
    operation = st.selectbox(
        "Operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                result = "Error"
            else:
                result = num1 / num2
        
        # Display result
        st.write(f"Result: {result}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Build by Tasleem Siddiqui ❤️ using Streamlit")