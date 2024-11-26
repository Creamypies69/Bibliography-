import streamlit as st

# CSS for gradient effect and styling
st.markdown("""
    <style>
        @keyframes gradient {
            0%, 100% { background-color: #FF5733; }
            25% { background-color: #33FF57; }
            50% { background-color: #3357FF; }
            75% { background-color: #FF33A1; }
        }
        .gradient-text {
            animation: gradient 10s ease infinite;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 6vw; text-align: center; margin: 20px 0;
        }
        .gradient-box {
            animation: gradient 10s ease infinite;
            padding: 10px; border-radius: 10px; color: black; 
            font-size: 2vw; margin-top: 10px; font-weight: bold;
        }
        .gradient-separator {
            border: 2px solid transparent;
            background-image: linear-gradient(90deg, #FF5733, #33FF57, #3357FF, #FF33A1, #FF5733);
            background-size: 400% 100%; animation: gradient 10s ease infinite;
            height: 2px; margin: 0;
        }
    </style>
    <h1 class="gradient-text">Daryl's Bibliography</h1>
""", unsafe_allow_html=True)

# Separator
st.markdown("<div class='gradient-separator'></div>", unsafe_allow_html=True)

# Description and Image columns
desc_col, img_col = st.columns([3, 1])

# Description
with desc_col:
    description = (
        "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
        "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
        "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
        "with his girlfriend, KC Aspacio, for three years."
    )
    st.markdown(f"<p style='font-size: calc(1.5em + 0.5vw); margin: 20px 0; text-align: justify;'>{description}</p>", unsafe_allow_html=True)

# Image and Name
with img_col:
    image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0;'>
            <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);' width='90%'/>
            <div class="gradient-box">Daryl E. Sagranada</div>
        </div>
    """, unsafe_allow_html=True)

# Separator
st.markdown("<div class='gradient-separator'></div>", unsafe_allow_html=True)

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
        "Tools": "Git, Visual Studio Code, Jupyter Notebook",
        "Soft Skills": "Teamwork, Communication, Problem-solving"
    }
    with st.expander("Competencies", expanded=True):
        for key, value in competencies.items():
            st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

# Simplified Competencies Section
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

# Footer with gradient effect
st.markdown("""
    <div class='gradient-separator'></div>
    <p style='text-align: center; font-size: 1.5vw;'>Programming Logic and Design</p>
""", unsafe_allow_html=True)
