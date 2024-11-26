import streamlit as st

# Title
st.markdown("""
    <h1 style='text-align: left; font-size: 8vw; margin-bottom: 20px;'>
        Daryl's Bibliography
    </h1>
""", unsafe_allow_html=True)

# Separator
st.markdown("<hr style='border: 2px solid #5D3FD3;'>", unsafe_allow_html=True)

# Image
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.image(image_url, caption="Daryl's Image", use_column_width='auto', style="border-radius: 5px;")

# Personal details
details = {
    "Age": "18",
    "Education": "Bachelor of Science in Computer Engineering (BSCpE)",
    "University": "Surigao del Norte State University (SNSU)",
    "High School": "DREESMNHS",
    "Location": "Surigao City, Philippines",
    "Phone Number": "09704978603",
    "Email": "daryl.sagranada.6146@gmail.com",
    "School Email": "dsagranada@ssct.edu.ph",
    "Height": "168 cm",
    "Weight": "56 kg"
}

with st.expander("Personal Details"):
    for key, value in details.items():
        st.markdown(f"**{key}:** {value}")

# Brief description
description = (
    "Daryl is an 18-year-old college student pursuing a BSCpE at SNSU. "
    "He graduated from DREESMNHS and lives in Surigao City. An introvert, "
    "he dreams of building a network of autonomous computers and enjoys reading and gaming. "
    "He has been in a loving relationship with his girlfriend, KC Aspacio, for three years."
)

with st.expander("Brief Description"):
    st.markdown(description)

# Competencies
competencies = [
    "Proficient in Python, Java, C++.",
    "Understanding of computer networks.",
    "Strong analytical skills.",
    "Experience with software development.",
    "Good communication skills.",
    "Fluent in English and Bisaya.",
    "Computer literate.",
    "Fast learner."
]

with st.expander("Competencies"):
    st.markdown("Daryl has developed the following competencies:")
    for item in competencies:
        st.markdown(f"- {item}")

# Footer
st.markdown("<div style='text-align: center; margin-top: 20px; font-size: 0.9em;'><em>This is a personal project for <a href='#' style='color: #5D3FD3;'>Programming Logic and Design Course</a>.</em></div>", unsafe_allow_html=True)
