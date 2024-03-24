import streamlit as st

def show_navigation():
    with st.container(border=True):
        col1,col2,col3,col4=st.columns(4)
        col1.page_link("streamlit_app.py", label="Home", icon="🏠")
        col2.page_link("pages/upload_pdf.py", label="Upload PDF", icon="1️⃣")
        col3.page_link("pages/parse_unstructured.py", label="Parse using Unstructured API", icon="2️⃣")
        col4.page_link("pages/parse_local.py", label="Parse", icon="🌎")
        #cols=st.columns(len(navList)
        # col3.page_link("pages/1_chat_with_AI.py", label="Chat", icon="2️⃣", disabled=True)