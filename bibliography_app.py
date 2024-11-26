import streamlit as st

# Custom HTML and CSS for gradient color effect
st.markdown("""
    <style>
        @keyframes gradient {
            0% { background-color: #FF5733; }
            25% { background-color: #33FF57; }
            50% { background-color: #3357FF; }
            75% { background-color: #FF33A1; }
            100% { background-color: #FF5733; }
        }
        .gradient-text {
            animation: gradient 10s ease infinite; /* Slowed down to 10s */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 6vw;
            text-align: center;
            margin: 20px 0;
        }
        .gradient-box {
            animation: gradient 10s ease infinite; /* Slowed down to 10s */
            padding: 10px;
            border-radius: 10px;
            color: white;
            font-size: 2vw;
            margin-top: 10px;
        }
        .gradient-separator {
            border: 2px solid transparent;
            background-image: linear-gradient(90deg, #FF5733, #33FF57, #3357FF, #FF33A1, #FF5733);
            background-size: 400% 100%;
            animation: gradient 10s ease infinite; /* Slowed down to 10s */
            height: 2px;
            margin: 0;
        }
    </style>
    <h1 class="gradient-text">Daryl's Bibliography</h1>
""", unsafe_allow_html=True)

# Gradient Separator
st.markdown("<div class='gradient-separator'></div>", unsafe_allow_html=True)

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

# Image and Name Box
with img_col:
    image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0;'>
            <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);' width='90%'/>
            <div class="gradient-box">
                Daryl E. Sagranada
            </div>
        </div>
    """, unsafe_allow_html=True)

# Gradient Separator
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
        for competency in competencies:
            st.markdown(f"- {competency}", unsafe_allow_html=True)

# Gradient Separator
st.markdown("<div class='gradient-separator'></div>", unsafe_allow_html=True)

# Footnote
st.markdown("<p style='text-align: center; font-size: 0.8em;'>This bibliography is a personal project created using Streamlit.</p>", unsafe_allow_html=True)
