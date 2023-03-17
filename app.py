import streamlit as st
import requests, json
import time 

st.title("Language Detection Application 🌎",)

text = st.text_area("Input your text")

data = json.dumps({"text": text})

flag = None


if st.button("Make Prediction", help="Click here to predict the language"):
    res = requests.post(url="http://localhost:8000/predict", data=data)
    language = json.loads(res.text)["language"]

    if language == "Arabic": flag = "🇸🇦"
    if language == "Danish": flag = "🇩🇰"
    if language == "Dutch": flag = "🇳🇱"
    if language == "English": flag = "🇺🇸"
    if language == "French": flag = "🇫🇷"
    if language == "German": flag = "🇩🇪"
    if language == "Greek": flag = "🇬🇷"
    if language == "Hindi": flag = "🇮🇳"
    if language == "Italian": flag = "🇮🇹"
    if language == "Kannada": flag = "🇮🇳"
    if language == "Malayalam": flag = "🇮🇳"
    if language == "Portugeese": flag = "🇵🇹"
    if language == "Russian": flag = "🇷🇺"
    if language == "Spanish": flag = "🇪🇸"
    if language == "Sweedish": flag = "🇸🇪"
    if language == "Turkish": flag = "🇹🇷"

    with st.spinner('Wainting for prediction...'):
        time.sleep(2)
        st.success('Done!',)
        st.subheader(f"The predicted language is: :blue[{language}] {flag}")
      
   