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

def create_post(title, content):
    request_body = {'title': title, 'content': content}
    response = requests.post(API_URL + '/create', json=request_body)
    if response.status_code in [200, 201]:
        data = response.json()
        st.write(data)
    else:
        st.error("Create Post Error")

st.title("Products")

# Fetch data from FastAPI backend
btn = st.button("Request API")
if btn:
    get_api()

post_title = st.text_input(label="Post Title", placeholder="title")
post_content = st.text_area(label="Post Content", placeholder="content")
btn_create_post = st.button(label="Create Post")

if btn_create_post:
    if post_title and post_content:
        create_post(post_title, post_content)
    else:
        st.error("Both title and content are required")
