import streamlit as st

# Title
st.markdown("""
    <h1 style='text-align: center; font-size: 8vw; line-height: 1.2; height: 2.4em; overflow: hidden;'>
        Daryl's Bibliography
    </h1>
""", unsafe_allow_html=True)

# Separator behind everything
st.markdown("""
    <div style='position: relative; z-index: -1;'>
        <hr style='border: 2px solid #5D3FD3; margin: 0;'>
    </div>
""", unsafe_allow_html=True)

# Image
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown(f"""
    <div style="border: 2px solid var(--primary-color); border-radius: 10px; padding: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">
        <a href="{image_url}" target="_blank">
            <img src="{image_url}" style="width: 75%; max-width: 300px; border-radius: 5px;">
        </a>
    </div>
""", unsafe_allow_html=True)

# Personal details
details = {
    "Age": "18",
    "Education": "Bachelor of Science in Computer Engineering (BSCpE)",
    "University": "Surigao del Norte State University (SNSU)",
    "High School": "Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)",
    "Location": "Narciso Rosales Street, Barangay Taft, Surigao City, Surigao del Norte, Philippines",
    "Phone Number": "09704978603",
    "Email": "daryl.sagranada.6146@gmail.com",
    "School Email": "dsagranada@ssct.edu.ph",
    "Height": "168 cm",
    "Weight": "56 kg"
}

with st.expander("Personal Details"):
    st.markdown("<ul>" + "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in details.items()) + "</ul>", unsafe_allow_html=True)

# Brief description
description = (
    "Daryl is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU.\n"
    "He graduated from DREESMNHS and lives in Surigao City.\n"
    "An introverted individual, he dreams of building a network of autonomous computers.\n"
    "In his free time, he enjoys reading and casual gaming.\n"
    "He has been in a loving relationship with his girlfriend, KC Aspacio, for three years."
)

with st.expander("Brief Description"):
    st.markdown(f"<pre>{description}</pre>", unsafe_allow_html=True)

# Competencies
competency_list = [
    "Proficiency in programming languages: Python, Java, C++.",
    "Understanding of computer networks and systems.",
    "Strong analytical and problem-solving skills.",
    "Experience with software development methodologies.",
    "Excellent communication and teamwork skills.",
    "Fluent in both English and Bisaya.",
    "Computer literate.",
    "Fast learner."
]

with st.expander("Competency"):
    st.markdown("<pre>Daryl has developed a range of competencies, including:</pre>", unsafe_allow_html=True)
    st.markdown("<ul>" + "".join(f"<li>{item}</li>" for item in competency_list) + "</ul>", unsafe_allow_html=True)

# Footer note
st.markdown("<div style='text-align: center; margin-top: 20px; font-size: 0.9em;'><em>This is a personal project! Submitted for <a href='#' style='color: #5D3FD3;'>Programming Logic and Design Course</a>.</em></div>", unsafe_allow_html=True)
