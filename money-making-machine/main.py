import streamlit as st
import random
import time
import requests


st.title("Money making Machine")


def generate_money():
    return random.randint(1,1000)



st.subheader("instant Cash generator")

if st.button("Generate Money"):
    st.write("Counting your money....")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You made ${amount}")


