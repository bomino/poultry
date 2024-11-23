

import streamlit as st
from config.settings import APP_NAME, APP_ICON, LAYOUT

# Configure the Streamlit page
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# Main page header
st.title("🐔 Poultry Weight Predictor")

# Welcome message
st.markdown("""
## Welcome to the Poultry Weight Predictor

This application helps you predict poultry weight based on environmental and feeding data. 
You can:

1. Upload and analyze your poultry data
2. Train machine learning models
3. Make predictions on new data
4. Visualize results and insights

### Getting Started

Use the sidebar to navigate through different sections of the app:

- **Data Upload**: Upload and preview your data
- **Data Analysis**: Explore your data with visualizations
- **Model Training**: Train and evaluate prediction models
- **Predictions**: Make predictions on new data

### Required Data Format

Your CSV file should include the following columns:
- Internal Temperature (Int Temp)
- Internal Humidity (Int Humidity)
- Air Temperature (Air Temp)
- Wind Speed
- Feed Intake
- Weight (target variable)
""")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")

# Hide the default page name in sidebar
hide_streamlit_style = """
<style>
    div[data-testid="stSidebarNav"] {
        visibility: hidden;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create a custom sidebar title for the main page
main_page = """
<style>
    div.sidebar-content {
        padding-top: 1rem;
    }
    div.sidebar-content:before {
        content: 'Main';
        font-size: 1rem;
        margin-left: 20px;
        position: relative;
        top: 0;
        color: rgb(49, 51, 63);
        font-weight: 700;
    }
</style>
"""
st.markdown(main_page, unsafe_allow_html=True)

