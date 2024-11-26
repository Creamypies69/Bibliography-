import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { color: #6A0C9A; }
    .subheader { color: #6A0C9A; }
    .separator { border: 1px solid #6A0C9A; margin: 10px 0; }
    .name-tag {
        text-align: center; font-size: 24px; color: black;
        background-color: #E6E6FA; padding: 10px; border-radius: 5px;
    }
    .description { font-size: 18px; }  /* Default description font size */
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Profile image URL
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"

# Create a column for the profile image and name tag
col1, col2, col3 = st.columns([1, 1, 2])  # Adjust proportions as needed

with col1:
    st.image(profile_image_url, width=200)  # Resize image

with col2:
    st.markdown("<div class='name-tag'>Daryl E. Sagranada</div>", unsafe_allow_html=True)

# Description in the third column
with col3:
    description = (
        "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
        "He graduated from DREESMNHS and lives in Surigao City. An introverted individual, he dreams of building a network "
        "of autonomous computers. In his free time, he enjoys reading and casual gaming. He has been in a loving relationship "
        "with his girlfriend, KC Aspacio."
    )
    st.markdown(f"<div class='description'>{description}</div>", unsafe_allow_html=True)

st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Create a single column for expanders
with st.container():
    col1, col2 = st.columns([1, 1])  # Two columns for expanders

    with col1:
        with st.expander("Personal Details", expanded=True):
            details = {
                "Age": "18", "Education": "BSCpE", "University": "SNSU",
                "High School": "DREESMNHS", "Location": "Surigao City, Philippines",
                "Phone Number": "097 04978603", "Email": "daryl.sagranada.6146@gmail.com",
                "School Email": "dsagranada@ssct.edu.ph", "Height": "168 cm", "Weight": "56 kg"
            }
            for key, value in details.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

    with col2:
        with st.expander("Competencies", expanded=True):
            competencies = {
                "Programming Languages": "Python, Java, C++",
                "Web Development": "HTML, CSS, JavaScript",
                "Operating Systems": "Windows, Linux"
            }
            for key, value in competencies.items():
                st.markdown(f"<strong>{key}:</strong> {value}", unsafe_allow_html=True)

st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Related images in tabs
st.subheader("Related Images")
tab_names = ["SNSU", "KC ASPACIO", "DREESMNHS", "DARYL", "SURIGAO CITY"]
tabs = st.tabs(tab_names)

# Image URLs for each tab
images = {
    "SNSU": ["https://via.placeholder.com/300?text=SNSU+Image+1", "https://via.placeholder.com/300?text=SNSU+Image+2", "https://via.placeholder.com/300?text=SNSU+Image+3"],
    "KC ASPACIO": ["https://via.placeholder.com/300?text=KC+ASPACIO+Image+1", "https://via.placeholder.com/300?text=KC+ASPACIO+Image+2"],
    "DREESMNHS": ["https://via.placeholder.com/300?text=DREESMNHS+Image+1", "https://via.placeholder.com/300?text=DREESMNHS+Image+2", "https://via.placeholder.com/300?text=DREESMNHS+Image+3"],
    "DARYL": ["https://via.placeholder.com/300?text=DARYL+Image+1", "https://via.placeholder.com/300?text=DARYL+Image+2"],
    "SURIGAO CITY": ["https://via.placeholder.com/300?text=SURIGAO+CITY+Image+1", "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+2", "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+3"]
}

# Display images in tabs
for i, tab in enumerate(tabs):
    with tab:
        for img_url in images[tab_names[i]]:
            st.image(img_url, caption=f"{tab_names[i]} Image", use_column_width=True)

st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Footer
st.markdown("Thank you for visiting Daryl's Bibliography!")
