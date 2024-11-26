import streamlit as st

# Page title
st.title("Daryl's Bibliography")
st.markdown("---")  # Separator

# Profile image and name
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.image(profile_image_url, caption="Daryl E. Sagranada", use_column_width=True)

# Description
description = (
    "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
    "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
    "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
    "with his girlfriend, KC Aspacio."
)
st.markdown(description, unsafe_allow_html=True)
st.markdown("---")  # Separator

# Personal details and competencies
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

competencies = {
    "Programming Languages": "Python, Java, C++",
    "Web Development": "HTML, CSS, JavaScript",
    "Operating Systems": "Windows, Linux"
}

# Create two columns for Personal Details and Competencies
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Details")
    for key, value in details.items():
        st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

with col2:
    st.subheader("Competencies")
    for key, value in competencies.items():
        st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

st.markdown("---")  # Separator

# Related images in tabs
st.subheader("Related Images")
tab_names = ["SNSU", "KC ASPACIO", "DREESMNHS", "DARYL", "SURIGAO CITY"]
tabs = st.tabs(tab_names)

# Define images for each tab
images = {
    "SNSU": [
        "https://via.placeholder.com/300?text=SNSU+Image+1",
        "https://via.placeholder.com/300?text=SNSU+Image+2",
        "https://via.placeholder.com/300?text=SNSU+Image+3"
    ],
    "KC ASPACIO": [
        "https://via.placeholder.com/300?text=KC+ASPACIO+Image+1",
        "https://via.placeholder.com/300?text=KC+ASPACIO+Image+2"
    ],
    "DREESMNHS": [
        "https://via.placeholder.com/300?text=DREESMNHS+Image+1",
        "https://via.placeholder.com/300?text=DREESMNHS+Image+2",
        "https://via.placeholder.com/300?text=DREESMNHS+Image+3"
    ],
    "DARYL": [
        "https://via.placeholder.com/300?text=DARYL+Image+1",
        "https://via.placeholder.com/300?text=DARYL+Image+2"
    ],
    "SURIGAO CITY": [
        "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+1",
        "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+2",
        "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+3"
    ]
}

# Display images in tabs
for i, tab in enumerate(tabs):
    with tab:
        tab_name = tab_names[i]
        for img_url in images[tab_name]:
            st.image(img_url, caption=f"{tab_name} Image", use_column_width=True)

st.markdown("---")  # Separator before the footer

 # Footer
st.markdown("Thank you for visiting Daryl's Bibliography!")
