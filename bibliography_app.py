import streamlit as st

# Display title with dark purple color
st.markdown('<h1 style="text-align: center; color: #5D3FD3;">Daryl\'s Bibliography</h1>', unsafe_allow_html=True)

# Display image with border and shadow
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
link_url = image_url

st.markdown(
    f"""
    <div style="border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" alt="Daryl's Image" style="width: 80%; max-width: 300px; border-radius: 5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Personal details with border and shadow
details = {
    "Age": "18",
    "Education": "Bachelor of Science in Computer Engineering (BSCpE)",
    "University": "Surigao del Norte State University (SNSU)",
    "High School": "Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)",
    "Location": "Barangay Taft, Surigao City, Surigao del Norte, Philippines"
}

st.markdown(
    "<div style='border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);'>"
    "<h3 style='color: #5D3FD3;'>Personal Details</h3>"
    "<ul style='list-style-type: none; padding: 0;'>" +
    "".join(f"<li style='margin-bottom: 10px;'><strong>{k}:</strong> {v}</li>" for k, v in details.items()) +
    "</ul></div>",
    unsafe_allow_html=True
)

# Brief description with border and shadow
description = "Daryl enjoys reading and gaming in his free time. He has been in a loving relationship with his girlfriend, KC Aspacio, for three years."
st.markdown(
    "<div style='border: 2px solid #5D3FD3; border-radius: 10px; padding: 10px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);'>"
    "<h3 style='color: #5D3FD3;'>Brief Description</h3>"
    f"<p style='text-align: center;'>{description}</p>"
    "</div>",
    unsafe_allow_html=True
)
