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
        height: 2px; 
        background-color: #6A0C9A; 
        margin: 10px 0; 
    }
    .description { 
        font-size: 18px; 
        text-align: center; 
        width: 80%;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
    }
    .profile-image {
        border-radius: 50%;
        border: 5px solid #6A0C9A;
    }
    .hover-text:hover {
        color: #6A0C9A;
        text-decoration: underline;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Daryl's Bibliography 📚")

# Profile picture
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.image(profile_image_url, width=300, caption='Daryl E. Sagranada', use_column_width='auto')

# Description
st.markdown("<div class='description'>"
            "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
            "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
            "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
            "</div>", unsafe_allow_html=True)

# Personal details and competencies
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Personal Details", expanded=False):
            details = {
                "Age": "18", 
                "Education": "BSCpE", 
                "University": "SNSU",
                "High School": "DREESMNHS", 
                "Location": "Surigao City, Philippines",
                "Phone": "097 04978603", 
                "Email": "daryl.sagranada.6146@gmail.com",
                "School Email": "dsagranada@ssct.edu.ph", 
                "Height": "168 cm", 
                "Weight": "56 kg"
            }
            for key, value in details.items():
                st.markdown(f"<span class='hover-text'><strong>{key}:</strong> {value}</span>", unsafe_allow_html=True)

    with col2:
        with st.expander("Competencies", expanded=False):
            competencies = [
                "Programming in Python, Java, and C++",
                "Web Development (HTML, CSS, JavaScript)",
                "Database Management (SQL)",
                "Machine Learning Basics",
                "Problem Solving and Critical Thinking"
            ]
            for competency in competencies:
                st.markdown(f"<span class='hover-text'>{competency}</span>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>This is a project Bibliography by Daryl!</div>", unsafe_allow_html=True)
