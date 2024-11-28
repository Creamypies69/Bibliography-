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
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Soft drop shadow for text */
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Soft drop shadow for text */
    }
    .profile-image { 
        display: block; 
        margin: 0 auto; 
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }  
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and separator
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Create columns for description and profile picture
col1, col2 = st.columns([2, 1])

# Description in the first column
with col1:
    st.markdown("<div class='description'>"
                "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
                "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
                "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
                "</div>", unsafe_allow_html=True)

# Profile section in the second column
with col2:
    profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.image(profile_image_url, width=150, caption="<strong>Daryl E. Sagranada</strong>")  # Bold caption

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Expanders for personal details and competencies
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Personal Details", expanded=True):
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
            st.image(image_url, use_column_width=True, caption=tab_name)

# Footer
st.markdown("<div class='footer'>Created by Daryl E. Sagranada</div>", unsafe_allow_html=True)
