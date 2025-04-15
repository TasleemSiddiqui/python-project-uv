import streamlit as st
import random
import string



def generate_password(length,use_digit,usespecial_character):
    characters = string.ascii_letters


    if use_digit:
        characters += string.digits

    if usespecial_character:
        characters += string.punctuation
    



    return "".join(random.choice(characters) for _ in range(length))


# Stremlit UI setup
st.title("Simple Password Generator")


length = st.slider("Select password length", min_value=8, max_value=32,value=12)


use_digit = st.checkbox("Include number")

usespecial_character = st.checkbox("Include special characters")


if st.button("generate password"):
    password = generate_password(length,use_digit,usespecial_character)
    st.write(f"Generated Password : {password}")