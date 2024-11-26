import streamlit as st

# CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 6vw;
            text-align: center;
            margin: 20px 0;
            color: lightgreen;
        }
        .name-box {
            padding: 10px;
            border-radius: 10px;
            color: black;
            font-size: 4vw;
            margin-top: 10px;
            font-weight: bold;
            text-align: center;
            width: 80%;
            display: inline-block;
            background-color: rgba(144, 238, 144, 0.8);
        }
        .separator {
            border: 2px solid lightgreen;
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
        .footer {
            text-align: center;
            font-size: 1.5vw;
            margin-top: 20px;
            color: lightgreen;
        }
    </style>
    <h1 class="header">Daryl's Bibliography</h1>
""", unsafe_allow_html=True)

# Separator between title and picture
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Profile image and name
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown(f"""
    <div class="image-container">
        <img src='{image_url}' style='border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5); width: 60%; height: auto;'/>
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

st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Personal details and competencies
details_col, competencies_col = st.columns(2)

with details_col:
    details = {
        "Age": "18",
        "Education": "BSCpE",
        "University": "SNSU",
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
        "Web Development": "HTML, CSS, JavaScript",
        "Operating Systems": "Windows, Linux"
    }
    with st.expander("Competencies", expanded=True):
        for key, value in competencies.items():
            st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Related images in tabs
st.subheader("Related Images")
tab_names = ["SNSU", "KC ASPACIO", "DREESMNHS", "DARYL", "SURIGAO CITY"]
tabs = st.tabs(tab_names)

# Dictionary of images for each tab
image_urls = {
    "SNSU": "https://via.placeholder.com/300?text=SNSU",
    "KC ASPACIO": "https://via.placeholder.com/300?text=KC+ASPACIO",
    "DREESMNHS": "https://via.placeholder.com/300?text=DREESMNHS",
    "DARYL": "https://via.placeholder.com/300?text=DARYL",
    "SURIGAO CITY": "https://via.placeholder.com/300?text=SURIGAO+CITY"
}

for tab in tabs:
    with tab:
        st.image(image_urls[tab], caption=f"{tab} Image")

# Separator below the tabs
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Thank you for visiting Daryl's Bibliography!</div>", unsafe_allow_html=True)
