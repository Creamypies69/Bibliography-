import streamlit as st

# Top Separator
st.markdown("<hr style='border: 1px solid rgba(74, 144, 226, 0.5); margin: 20px 0; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'>", unsafe_allow_html=True)

# Title
st.markdown("""
    <h1 style='text-align: center; font-size: 6vw; color: #4A90E2; margin: 20px 0;'>
        Daryl's Bibliography
    </h1>
""", unsafe_allow_html=True)

# Middle Separator
st.markdown("<hr style='border: 1px solid rgba(74, 144, 226, 0.5); margin: 0; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'>", unsafe_allow_html=True)

# Description and Image columns
desc_col, img_col = st.columns([3, 1])

# Brief Description
with desc_col:
    description = (
        "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
        "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
        "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
        "with his girlfriend, KC Aspacio, for three years."
    )
    st.markdown(f"<p style='font-size: calc(1.5em + 0.5vw); margin: 20px 0; text-align: justify;'>{description}</p>", unsafe_allow_html=True)

# Image
with img_col:
    image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0;'>
            <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);' width='90%'/>
            <div style='background-color: #4A90E2; color: white; font-size: 2vw; margin-top: 10px; padding: 10px; border-radius: 10px;'>
                Daryl E. Sagranada
            </div>
        </div>
    """, unsafe_allow_html=True)

# Middle Separator
st.markdown("<hr style='border: 1px solid rgba(74, 144, 226, 0.5); margin: 0; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'>", unsafe_allow_html=True)

# Details and Competencies columns
col1 = st.columns(1)[0]
details_col, competencies_col = st.columns(2)

# Personal Details
with details_col:
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

    with st.expander("Personal Details", expanded=True):
        for key, value in details.items():
            st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

# Competencies
with competencies_col:
    competencies = [
        "Proficient in Python, Java, C++.",
        "Understanding of computer networks.",
        "Strong analytical and problem-solving skills.",
        "Experience with software development.",
        "Excellent communication skills.",
        "Fluent in English and Bisaya.",
        "Computer literate.",
        "Fast learner."
    ]

    with st.expander("
