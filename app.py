import streamlit as st
import sys
import time

def main():
    st.set_page_config(page_title="Grok Chat")
    st.title("Hello from Streamlit Cloud")
    st.write("If you see this, the app is running.")
    st.write("Python version:", sys.version)
    st.write("Time:", time.time())

if __name__ == "__main__":
    main()




