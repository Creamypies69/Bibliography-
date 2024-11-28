import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { 
        color: #6A0C9A; 
        text-align: center; 
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .separator { 
        border: 1px solid #6A0C9A; 
        margin: 10px 0; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .name-tag {
        text-align: center; 
        font-size: 20px; 
        color: black;  
        background-color: #E6E6FA; 
        padding: 10px; 
        border-radius: 5px; 
        width: 200px;  
        margin: 10px auto;  
        font-weight: bold;  
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .description { 
        font-size: 18px; 
        text-align: center; 
        width: 80%; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        height: 100%;
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .profile-image { 
        display: block; 
        margin: 0 auto; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); 
        max-width: 100%; 
        height: auto; 
    }  
    .margin-line {
        border-left: 2px solid #6A0C9A; 
        border-right: 2px solid #6A0C9A; 
        padding: 0 20px; 
        margin: 0 auto; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and separator
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Margin lines and content layout
with st.container():
    st.markdown("<div class='margin-line'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])  # Adjust column ratio

    # Profile picture and name tag
    with col2:
        profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/202411%2021_151401.jpg"
        st.image(profile_image_url, width=150)
        st.markdown("<div class='name-tag'>Daryl E. Sagranada</div>", unsafe_allow_html=True)

    # Description
    with col1:
        st.markdown("<div class='description'>"
                    "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
                    "He graduated from DREESMNHS and lives in Surigao City. Daryl dreams of building a network of autonomous computers. "
                    "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
                    "</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close margin line

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Expanders for personal details and competencies
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Personal Details", expanded=True):
            details = {
                "Age": "18", "Education": "BSCpE", "University": "SNSU",
                "High School": "DREESMNHS", "Location": "Surigao City, Philippines",
                "Phone": "097 04978603 ", "Email": "daryl.sagranada.6146@gmail.com",
                "School Email": "dsagranada@ssct.edu.ph", "Height": "168 cm", "Weight": "56 kg"
            }
            for key, value in details.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

    with col2:
        with st.expander("Competencies", expanded=True):
            competencies = {
                "Languages": "Python, Java, C++",
                "Web Development": "HTML, CSS, JavaScript",
                "Operating Systems": "Windows, Linux"
            }
            for key, value in competencies.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Related images in tabs
st.subheader("Related Images")
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
    with tabs[tab_names.index(tab_name)]:
        for image_url in images[tab_name]:
            st.image(image_url, use_column_width=True)

# Footer
st.markdown("<div class='footer'>Created by Daryl E. Sagranada</div>", unsafe_allow_html=True)
