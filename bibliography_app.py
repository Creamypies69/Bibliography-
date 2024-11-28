import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #F5F5F5;
        font-family: Arial, sans-serif;
    }
    .separator { 
        border: none; 
        height: 2px; 
        background-color: #6A0C9A; 
        margin: 10px 0; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .description { 
        font-size: 18px; 
        text-align: center; 
        margin: 0 auto; 
        width: 80%;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .profile-image {
        border: 5px solid #6A0C9A;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .tab-title {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0;
    }
    .expander {
        transition: background-color 0.3s ease;
    }
    .stExpander[aria-expanded="true"] {
        background-color: rgba(106, 12, 154, 0.1); /* Change color when expanded */
    }
    .hover-effect {
        transition: background-color 0.3s ease;
        padding: 5px; /* Add padding for a better hover effect */
        border-radius: 5px; /* Rounded corners for the hover effect */
    }
    .hover-effect:hover {
        background-color: rgba(106, 12, 154, 0.3); /* Hover color */
        color: white; /* Change text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Daryl's Bibliography 📚")

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Profile picture
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/20240304_132422.jpg"
st.markdown(f"<div style='text-align: center;'><img src='{profile_image_url}' width='300' class='profile-image' alt='Daryl E. Sagranada' /></div>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Description
st.markdown("<div class='description'>"
            "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
            "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
            "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
            "</div>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Personal details and competencies
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Personal Details", expanded=False):
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            details = {
                "Age": "18", 
                "Education": "BSCpE", 
                "University": "SNSU",
                "High School": "DREESMNHS", 
                "Location": "Surigao City, Philippines",
                "Phone":
