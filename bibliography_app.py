import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { 
        color: #6A0C9A; 
        text-align: center; 
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
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
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    }
    .profile-image { 
        display: block; 
        margin: 0 auto; 
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }  
    .navy-button {
        background-color: #001f3f;  /* Dark navy blue */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .navy-button:hover {
        background-color: #003366;  /* Lighter navy blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Daryl's Bibliography 📚")

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Centered profile picture
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown(f"<div style='text-align: center;'><img src='{profile_image_url}' width='300' alt='Daryl E. Sagranada' /></div>", unsafe_allow_html=True)

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
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

    with col2:
        with st.expander("Competencies", expanded=False):
            competencies = {
                "Languages": "Python, Java, C++",
                "Web Development": "HTML, CSS, JavaScript",
                "Operating Systems": "Windows, Linux"
            }
            for key, value in competencies.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

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
                for image_url in images[tab_name]:
                    st.image(image_url, use_column_width=True, caption=tab_name)
        else:
            st.error(f"Error: No images found for {tab_name}")

# Separator below Related Images
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Footer section
st.markdown("<div class='footer'>"
            "This is a project Bibliography by Daryl! To be submitted for <strong>Programming Logic and Design</strong>"
            "</div>", unsafe_allow_html=True)

# Refresh button positioned to the left corner
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Refresh"):
        st.experimental_rerun()
with col2:
    if st.button("GitHub", key="github_button", help="Go to GitHub page", css_class="navy-button"):
        st.markdown("<script>window.open('https://g4sebr7wlknj2tu3kz9jpj.streamlit.app/', '_blank');</script>", unsafe_allow_html=True)
