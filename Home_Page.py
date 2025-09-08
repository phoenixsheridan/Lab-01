import streamlit as st

# Title
st.title("Phoenix Sheridan")
st.subheader("CS 1301")

# Quick intro
st.write("Welcome to my multi-page Streamlit app! Use the sidebar to navigate between pages.")

# Page descriptions
st.markdown("""
### Pages in this App:
1. **Portfolio** – My personal portfolio showcasing my education, experience, projects, and skills.
2. **Phase 2** – A page that includes a short quiz including stuff regarding my interests.
""")

# Extra customization (optional)
st.write("---")
st.info("👉 Navigate to another page using the sidebar on the left.")
