import streamlit as st
import requests


def navigation():
    about_page = st.Page("about.py", title="About Us", icon=":material/add_circle:")
    product_page = st.Page("products.py", title="Our Products", icon=":material/add_circle:")
    pg = st.navigation([about_page, product_page])
    pg.run()


def main():
    st.set_page_config(page_title="MLMond.com", page_icon=":material/edit:")
    st.title("FastAPI + Streamlit")
    navigation()




if __name__ == "__main__":
    main()
