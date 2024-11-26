import streamlit as st

# Title
st.title("Daryl's Bibliography")

# Image with border and shadow
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
link_url = image_url

st.markdown(
    f"""
    <div style="border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" style="width: 75%; max-width: 300px; border-radius: 5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Personal details
details = {
    "Age": "18",
    "Education": "Bachelor of Science in Computer Engineering (BSCpE)",
    "University": "Surigao del Norte State University (SNSU)",
    "High School": "Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)",
    "Location": "Narciso Rosales Street, Barangay Taft, Surigao City, Surigao del Norte, Philippines"
}

# Display personal details
st.markdown(
    "<div style='border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);'>"
    "<h3 style='color: #5D3FD3;'>Personal Details</h3>"
    "<ul style='list-style-type: none; padding: 0;'>" +
    "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in details.items()) +
    "</ul></div>",
    unsafe_allow_html=True
)

# Brief description
description = (
    "Daryl is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at Surigao del Norte State University (SNSU). "
    "A proud graduate of Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS), he resides on Narciso Rosales Street in Barangay Taft, Surigao City, Surigao del Norte, Philippines. "
    "An introverted and observant individual, Daryl has a deep interest in computer systems, both hardware and software. He dreams of building a hive-like network of fully autonomous computers. "
    "In his free time, he enjoys reading books and visual novels, balancing his intellectual pursuits with casual gaming sessions. "
    "For the past three years, he has been in a loving relationship with his girlfriend, KC Aspacio, who shares and supports his laid-back and creative nature."
)

# Display brief description
st.markdown(
    "<div style='border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);'>"
    "<h3 style='color: #5D3FD3;'>Brief Description</h3>"
    f"<p style='text-align: center;'>{description}</p>"
    "</div>",
    unsafe_allow_html=True
)
