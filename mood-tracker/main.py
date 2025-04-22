# Import required libraries
import streamlit as st
import pandas as pd
import datetime
import csv
import os


# Define constants
MOOD_FILE = "mood_log.csv"

def load_mood_data():
    """
    Load mood data from CSV file or create empty DataFrame if file doesn't exist
    Returns: pandas DataFrame with mood data
    """
    try:
        if not os.path.exists(MOOD_FILE):
            df = pd.DataFrame(columns=["Date", "Mood"])
            df.to_csv(MOOD_FILE, index=False)
            return df
        
        df = pd.read_csv(MOOD_FILE)
        # Ensure column names are correct
        if "Date" not in df.columns or "Mood" not in df.columns:
            df = pd.DataFrame(columns=["Date", "Mood"])
            df.to_csv(MOOD_FILE, index=False)
        return df
    except Exception as e:
        st.error(f"Error loading mood data: {str(e)}")
        return pd.DataFrame(columns=["Date", "Mood"])

def save_mood_data(date, mood):
    """
    Save mood entry to CSV file
    Args:
        date: Date of mood entry
        mood: Mood to be logged
    """
    try:
        # Check if mood already logged for today
        data = load_mood_data()
        today_str = date.strftime("%Y-%m-%d")
        
        if not data.empty and "Date" in data.columns:
            if (data["Date"] == today_str).any():
                st.error("You have already logged a mood for today!")
                return False
            
        with open(MOOD_FILE, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([today_str, mood])
        return True
    except Exception as e:
        st.error(f"Error saving mood data: {str(e)}")
        return False

# Create the Streamlit app interface
st.title("Mood Tracker")

# Get today's date
today = datetime.date.today()

st.subheader("How are you feeling today?")

# Create mood selection dropdown
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Add mood logging button and functionality      
if st.button("Log Mood"):
    if save_mood_data(today, mood):
        st.success("Mood Logged Successfully")

# Load and display mood data
data = load_mood_data()

# Display mood trends if data exists
if not data.empty and "Date" in data.columns and "Mood" in data.columns:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])
    
    # Calculate mood frequency
    mood_counts = data.groupby("Mood").size()
    
    # Display bar chart of mood trends
    st.bar_chart(mood_counts)