import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Gurgaon Properties",
    page_icon="🏠",
)

# Main content
st.title("Welcome to Gurgaon Properties")
st.write("Explore properties in Gurgaon, India.")

# Features section
st.header("Features")
st.markdown("""
- **Enquire about properties:** Search for houses and flats in Gurgaon.
- **Price information:** Get insights into property prices.
- **Recommendations:** Receive recommendations based on your preferences.
""")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a tab from above.")
