import streamlit as st

text_color = "#FFFFFF"
highlight_color = "#FF5733"

image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 
link_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 

background_image_url = "https://github.com/Creamypies69/Bibliography-/blob/main/Night%20Sky%20Wallpapers%20-%20Wallpaper%20Cave.jpeg?raw=true"

# Set background and text styles
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: 
            linear-gradient(to bottom, rgba(30, 30, 47, 1), rgba(30, 30, 47, 0)), 
            url('{background_image_url}');
        background-size: cover;
        color: {text_color};
    }}
    .sidebar .sidebar-content {{
        background: rgba(30, 30, 47, 0.8);
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {highlight_color};
    }}
    .stButton > button {{
        background-color: {highlight_color};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Daryl's Bibliography")

# Subtitle
st.subheader("Brief Description")

# Display picture
st.markdown(
    f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" alt="Daryl's Image" width="300">
    </a>
    """,
    unsafe_allow_html=True
)

# Description text
description = (
    "Daryl is an 18-year-old college student currently pursuing a Bachelor of Science in Computer Engineering (BSCpE) "
    "at Surigao del Norte State University (SNSU). A proud graduate of Don Ruben Edera Ecleo Sr. Memorial National High School "
    "(DREESMNHS), he resides on Narciso Rosales Street in Barangay Taft, Surigao City, Surigao del Norte, Philippines. "
    "Daryl enjoys spending his free time immersed in books and visual novels, balancing his intellectual pursuits with casual gaming sessions. "
    "For the past three years, he has been in a loving relationship with his girlfriend, KC Aspacio, who shares and supports his laid-back and creative nature."
)

# Show description
st.markdown(description)
