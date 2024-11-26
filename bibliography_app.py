import streamlit as st

# Display title
st.markdown('<h1 style="text-align: center; color: #f63366;">Daryl\'s<br>Bibliography</h1>', unsafe_allow_html=True)

# Display image
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 
link_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 

st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" alt="Daryl's Image" style="width: 80%; max-width: 300px; border-radius: 5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Display personal details
st.markdown("<h3 style='text-align: center; color: #f63366;'>Personal Details</h3>", unsafe_allow_html=True)
personal_details = (
    "<div>"
    "<ul style='list-style-type: none; padding: 0;'>"
    "<li><strong>Age:</strong> 18</li>"
    "<li><strong>Education:</strong> Bachelor of Science in Computer Engineering (BSCpE)</li>"
    "<li><strong>University:</strong> Surigao del Norte State University (SNSU)</li>"
    "<li><strong>High School:</strong> Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)</li>"
    "<li><strong>Location:</strong> Barangay Taft, Surigao City, Surigao del Norte, Philippines</li>"
    "</ul>"
    "</div>"
)

st.markdown(personal_details, unsafe_allow_html=True)

# Display brief description
st.markdown("<h2 style='text-align: center; color: #f63366;'>Brief Description</h2>", unsafe_allow_html=True)
brief_description = (
    "<div>"
    "<p style='text-align: center;'>Daryl enjoys reading and gaming in his free time. He has been in a loving relationship with his girlfriend, KC Aspacio, for three years.</p>"
    "</div>"
)

st.markdown(brief_description, unsafe_allow_html=True)
