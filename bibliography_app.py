import streamlit as st

# Title with responsive size and color
st.markdown(
    """
    <h1 style="color: #5D3FD3; text-align: center; font-size: 5vw;">Daryl's Bibliography</h1>
    """,
    unsafe_allow_html=True
)

# Image with border and shadow
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"

st.markdown(
    f"""
    <div style="border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">
        <a href="{image_url}" target="_blank">
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

# Expander for Personal Details with custom font size
with st.expander("<span style='color: #5D3FD3; font-weight: bold;'>Personal Details</span>", expanded=False, unsafe_allow_html=True):
    st.markdown(
        "<ul style='list-style-type: none; padding: 0; font-size: 0.8vw;'>" +
        "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in details.items()) +
        "</ul>",
        unsafe_allow_html=True
    )

# Brief description
description = (
    "Daryl is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at Surigao del Norte State University (SNSU).\n"
    "He graduated from Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS) and lives on Narciso Rosales Street in Barangay Taft, Surigao City, Surigao del Norte, Philippines.\n"
    "An introverted and observant individual, Daryl is interested in computer systems and dreams of building a network of fully autonomous computers.\n"
    "In his free time, he enjoys reading books and visual novels, balancing his intellectual pursuits with casual gaming.\n"
    "For the past three years, he has been in a loving relationship with his girlfriend, KC Aspacio."
)

# Expander for Brief Description with custom font size
with st.expander("<span style='color: #5D3FD3; font-weight: bold;'>Brief Description</span>", expanded=False, unsafe_allow_html=True):
    st.markdown(
        f"<pre style='text-align: left; font-size: 0.8vw;'>{description}</pre>",
        unsafe_allow_html=True
    )
