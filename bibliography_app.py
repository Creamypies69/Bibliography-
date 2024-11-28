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
        border: none; 
        height: 2px; 
        background-color: #6A0C9A; 
        margin: 10px 0; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .description { 
        font-size: 18px; 
        text-align: center; 
        margin: 0 auto; 
        width: 80%;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .profile-image {
        border-radius: 50%;
        border: 5px solid #6A0C9A;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .tab-title {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0;
    }
    .expander {
        transition: background-color 0.3s ease;
    }
    .stExpander[aria-expanded="true"] {
        background-color: rgba(106, 12, 154, 0.1); /* Change color when expanded */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Daryl's Bibliography 📚")

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Profile picture
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown(f"<div style='text-align: center;'><img src='{profile_image_url}' width='300' class='profile-image' alt='Daryl E. Sagranada' /></div>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Description
st.markdown("<div class='description'>"
            "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
            "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
            "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
            "</div>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Personal details and competencies
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Personal Details", expanded=False):
            st.markdown("<div class='card'>", unsafe_allow_html=True)
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
                st.markdown(f"<strong>{ key}:</strong> {value}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        with st.expander("Competencies", expanded=False):
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            competencies = {
                "Languages": "Python, Java, C++",
                "Web Development": "HTML, CSS, JavaScript",
                "Operating Systems": "Windows, Linux"
            }
            for key, value in competencies.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Related images
with st.expander("Related Images", expanded=False):
    tab_names = ["SNSU", "KC ASPACIO", "DREESMNHS", "DARYL", "SURIGAO CITY"]
    images = {
        "SNSU": [
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745727339.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745734282.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745788123.jpg"
        ],
        "KC ASPACIO": [
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/IMG_20240601_131821_393.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/IMG_20240519_133040_233.jpg"
        ],
        "DREESMNHS": [
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745650378.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745687514.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745831902.jpg"
        ],
        "DARYL": [
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1700642274650.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/IMG_20231226_140425_064.jpg"
        ],
        "SURIGAO CITY": [
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/1732745851002.jpg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/images.jpeg",
            "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/images%20(1).jpeg"
        ]
    }

    tabs = st.tabs(tab_names)

    for tab_name in tab_names:
        if tab_name in images:
            with tabs[tab_names.index(tab_name)]:
                st.markdown(f"<div class='tab-title'>{tab_name}</div>", unsafe_allow_html=True)
                for image_url in images[tab_name]:
                    st.image(image_url, use_column_width=True, caption=tab_name)

# Separator below Related Images
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Footer section
st.markdown("<div class='footer'>"
            "This is a project Bibliography by Daryl! To be submitted for <strong>Programming Logic and Design</strong>"
            "</div>", unsafe_allow_html=True)
