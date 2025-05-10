import streamlit as st
import requests

def get_random_joke():
    """get random joke from an api"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
        
            joke_data = response.json()
        
            return f"{joke_data["setup"]} \n \n {joke_data["punchline"]}"
        else :
            return "Failed to fetch a joke, please try again later "
    except Exception as e:
        return f"Something went wrong!{e}"








def main():
    """main function to run a streamlit app"""
    
    st.title("Random Joke Genetrator")
    
    st.write("Click the button below to generate a random Joke")
    
    if st.button("Generate Joke"):
        joke = get_random_joke()
        
        st.success(joke)

    
    st.divider()

    # Footer using HTML, displaying text in the center
    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a href='https://github.com/TasleemSiddiqui'>Muhammad Tasleem</a> using Streamlit</p>
    </div>
""", 
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
