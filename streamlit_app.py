import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="Mental Wellness App",
    page_icon="🧘‍♀️",
    layout="wide"
)

# --- Main Page Content ---
# This file serves as the default entry point and usually redirects
# or provides a simple introduction before the sidebar navigation takes over.

st.title("Welcome to Your Mental Wellness Hub 🧠")
st.markdown("""
Welcome! Use the navigation in the sidebar on the left to explore different tools and resources.

This main page can serve as a dashboard or a simple introduction to your application's purpose.
""")

# Note: Streamlit automatically displays the pages defined in the 'pages/' folder
# in the sidebar. We don't need any complex routing logic here!

# You can add a brief footer or instructions here
st.sidebar.header("App Navigation")
