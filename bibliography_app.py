import streamlit as st

# Page title
st.title("Daryl's Bibliography")

# Profile image and name
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.image(profile_image_url, caption="Daryl E. Sagranada", use_column_width=True)

# Description
description = (
    "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a Bachelor of Science in Computer Engineering (BSCpE) at SNSU. "
    "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
    "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
    "with his girlfriend, KC Aspacio, for three years."
)
st.markdown(description, unsafe_allow_html=True)

# Personal details
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
with st.expander("Personal Details"):
    for key, value in details.items():
        st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

# Competencies
competencies = {
    "Programming Languages": "Python, Java, C++",
    "Web Development": "HTML, CSS, JavaScript",
    "Operating Systems": "Windows, Linux"
}
with st.expander("Competencies"):
    for key, value in competencies.items():
        st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

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

for tab in tabs:
    with tab:
        # Use the tab's name to access the images
        for img_url in images[tab.name]:  # Corrected this line
            st.image(img_url, caption=f"{tab.name} Image", use_column_width=True)

# Footer
st.markdown("Thank you for visiting Daryl's Bibliography!")
