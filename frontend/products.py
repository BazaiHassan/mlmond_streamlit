import streamlit as st
import requests

API_URL = 'http://fastapi:8000'

def get_api():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        st.write("The response from API:")
        st.json(data)
    else:
        st.error("Failed to fetch data from FastAPI")

st.title("products")

# Fetch data from FastAPI backend
btn = st.button("Request API")
if btn:
    get_api()