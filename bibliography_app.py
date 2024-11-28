import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { color: #6A0C9A; text-align: center; }
    .separator { border: 1px solid #6A0C9A; margin: 10px 0; }
    .name-tag {
        text-align: center; font-size: 20px; color: black;  
        background-color: #E6E6FA; padding: 10px; border-radius: 5px; width: 250px; margin: 0 auto;  
    }
    .description { font-size: 18px; text-align: center; }
    .footer { text-align: center; margin-top: 20px; color: #6A0C9A; }
    .profile-image { display: block; margin: 0 auto; }  
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and separator
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Create columns for profile picture, name tag, and description
col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

# Profile section with centered layout in the first column
with col1:
    profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.image(profile_image_url, width=150, use_column_width=False)  # Set width to 150 pixels
    st.markdown("<div class='name-tag'>Daryl E. Sagranada</div>", unsafe_allow_html=True)  # Name tag

# Description in the second column
with col2:
    st.markdown("<div class='description'>"
                "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
                "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
                "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
                "</div>", unsafe_allow_html=True)  # Description

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
                "Phone": "097 04978603", "Email": "daryl.sagranada.6146@gmail.com",
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
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/snsu1.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/snsu2.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/snsu3.jpg"
    ],
    "KC ASPACIO": [
        "https://raw.githubusercontent.com /Creamypies69/Bibliography-/refs/heads/main/kc_asapcio.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/kc2.jpg"
    ],
    "DREESMNHS": [
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/dreesmnhs1.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/dreesmnhs2.jpg"
    ],
    "DARYL": [
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/daryl1.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/daryl2.jpg"
    ],
    "SURIGAO CITY": [
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/surigao1.jpg",
        "https://raw.githubusercontent.com/Creamypies69/Bibliography-/refs/heads/main/surigao2.jpg"
    ]
}

tabs = st.tabs(tab_names)

for tab_name in tab_names:
    with tabs[tab_names.index(tab_name)]:
        for image_url in images[tab_name]:
            st.image(image_url, use_column_width=True)

# Footer
st.markdown("<div class='footer'>Created by Daryl E. Sagranada</div>", unsafe_allow_html=True)
