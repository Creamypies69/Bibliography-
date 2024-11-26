import streamlit as st

# Title with new styling
st.markdown("""
    <h1 style='text-align: center; font-size: 6vw; color: #4A90E2; margin: 20px 0;'>
        Daryl's Bibliography
    </h1>
""", unsafe_allow_html=True)

# Styled separator
st.markdown("<hr style='border: 2px solid #4A90E2; margin: 0;'>", unsafe_allow_html=True)

# Create a new row for the Brief Description and the image
desc_col, img_col = st.columns([3, 1])  # 3:1 ratio for description and image

# Brief Description
with desc_col:
    description = (
        "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
        "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
        "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
        "with his girlfriend, KC Aspacio, for three years."
    )
    st.markdown(f"<p style='font-size: 1.5em; margin: 20px 0; text-align: justify;'>{description}</p>", unsafe_allow_html=True)

# Right column for the image
with img_col:
    # Image with new shadow and border
    image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0;'>
            <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);' width='90%'/>
            <div style='background-color: #4A90E2; color: white; font-size: 2vw; margin-top: 10px; padding: 10px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);'>
                Daryl E. Sagranada
            </div>
        </div>
    """, unsafe_allow_html=True)

# Separator between sections
st.markdown("<hr style='border: 2px solid #4A90E2; margin: 0;'>", unsafe_allow_html=True)

# Create main columns for layout
col1 = st.columns(1)[0]  # Only one column for the details

# Left column for details
with col1:
    # Create sub-columns for Personal Details and Competencies
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

        with st.expander("Competencies", expanded=False):
            st.markdown("Daryl has developed a range of competencies, including:")
            for item in competencies:
                st.markdown(f"- {item}")

# Footer with new styling
st.markdown("<div style='text-align: center; margin-top: 20px; font -size: 0.9em; color: #888;'><em>This is a personal project!</em></div>", unsafe_allow_html=True)
