import streamlit as st

# CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 6vw;
            text-align: center;
            margin: 20px 0;
        }
        .name-box {
            padding: 10px;
            border-radius: 10px;
            color: black;
            font-size: 2vw;
            margin-top: 10px;
            font-weight: bold;
            text-align: center;
        }
        .separator {
            border: 2px solid black;
            height: 2px;
            margin: 20px 0;
        }
        .description {
            font-size: calc(1.2em + 0.5vw);
            margin: 20px 0;
            text-align: justify;
        }
        .image-container {
            text-align: center;
            margin: 20px 0;
        }
    </style>
    <h1 class="header">Daryl's Bibliography</h1>
""", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Image, Name, and Description
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown(f"""
    <div class="image-container">
        <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5); width: 80%; height: auto;'/>
        <div class="name-box">Daryl E. Sagranada</div>
    </div>
""", unsafe_allow_html=True)

# Description
description = (
    "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
    "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
    "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
    "with his girlfriend, KC Aspacio, for three years."
)
st.markdown(f"<p class='description'>{description}</p>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Personal Details
details_col, competencies_col = st.columns(2)

with details_col:
    details = {
        "Age": "18",
        "Education": "Bachelor of Science in Computer Engineering (BSCpE)",
        "University": "Surigao del Norte State University (SNSU)",
        "High School": "DREESMNHS",
        "Location": "Surigao City, Philippines",
        "Phone Number": "097 04978603",
        "Email": "daryl.sagranada.6146@gmail.com",
        "School Email": "dsagranada@ssct.edu.ph",
        "Height": "168 cm",
        "Weight": "56 kg"
    }
    with st.expander("Personal Details", expanded=True):
        for key, value in details.items():
            st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

with competencies_col:
    competencies = {
        "Programming Languages": "Python, Java, C++",
        "Web Development": "HTML, CSS, JavaScript, Flask",
        "Database Management": "MySQL, SQLite",
        "Tools": "Git, VS Code, Jupyter",
        "Soft Skills": "Teamwork, Communication, Problem-solving"
    }
    with st.expander("Competencies", expanded=True):
        for key, value in competencies.items():
            st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Related Images Section
st.subheader("Related Images")

# Tabs for related images with swapped order
tab_names = ["SNSU", "KC ASPACIO", "DREESMNHS", "Daryl", "SURIGAO CITY"]
tabs = st.tabs(tab_names)

# Content for each tab
with tabs[0]:
    st.image("https://via.placeholder.com/300", caption ="SNSU Logo")

with tabs[1]:
    st.image("https://via.placeholder.com/300", caption="KC Aspacio's Profile Picture")

with tabs[2]:
    st.image("https://via.placeholder.com/300", caption="DREESMNHS Logo")

with tabs[3]:
    st.image("https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg", caption="Daryl's Profile Picture")

with tabs[4]:
    st.image("https://via.placeholder.com/300", caption="Surigao City Skyline")

# Footer
st.markdown("""
    <div class='separator'></div>
    <p style='text-align: center; font-size: 1.5vw;'>Programming Logic and Design</p>
""", unsafe_allow_html=True)
