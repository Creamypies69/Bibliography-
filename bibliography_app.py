import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { color: #6A0C9A; text-align: center; }
    .separator { border: 1px solid #6A0C9A; margin: 10px 0; }
    .name-tag {
        text-align: center; font-size: 20px; color: black;  /* Adjusted font size */
        background-color: #E6E6FA; padding: 10px; border-radius: 5px; width: 250px; margin: 0 auto;  /* Adjusted width */
    }
    .description { font-size: 18px; text-align: center; }
    .footer { text-align: center; margin-top: 20px; color: #6A0C9A; }
    .profile-image { display: block; margin: 0 auto; }  /* Center the image */
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and separator
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Profile section with centered layout
profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(profile_image_url, width=250, use_column_width=False)  # Decreased size and removed caption
st.markdown("<div class='name-tag'>Daryl E. Sagranada</div>", unsafe_allow_html=True)  # Name tag
st.markdown("<div class='description'>"
            "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
            "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
            "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
            "</div>", unsafe_allow_html=True)  # Description
st.markdown("</div>", unsafe_allow_html=True)  # Close centered div

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
    "SNSU": ["https://via.placeholder.com /300?text=SNSU+Image+1", "https://via.placeholder.com/300?text=SNSU+Image+2", "https://via.placeholder.com/300?text=SNSU+Image+3"],
    "KC ASPACIO": ["https://via.placeholder.com/300?text=KC+ASPACIO+Image+1", "https://via.placeholder.com/300?text=KC+ASPACIO+Image+2"],
    "DREESMNHS": ["https://via.placeholder.com/300?text=DREESMNHS+Image+1", "https://via.placeholder.com/300?text=DREESMNHS+Image+2", "https://via.placeholder.com/300?text=DREESMNHS+Image+3"],
    "DARYL": ["https://via.placeholder.com/300?text=DARYL+Image+1", "https://via.placeholder.com/300?text=DARYL+Image+2"],
    "SURIGAO CITY": ["https://via.placeholder.com/300?text=SURIGAO+CITY+Image+1", "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+2", "https://via.placeholder.com/300?text=SURIGAO+CITY+Image+3"]
}

# Creating tabs
tabs = st.tabs(tab_names)

for i, tab in enumerate(tabs):
    with tab:
        cols = st.columns(2)
        col_counters = [0, 0]  # Initialize counters for each column
        for img_url in images[tab_names[i]]:
            # Distributing images across columns
            if col_counters[0] <= col_counters[1]:
                with cols[0]:
                    st.image(img_url, caption=f"{tab_names[i]} Image", use_column_width=True)
                col_counters[0] += 1  # Increment counter for column 1
            else:
                with cols[1]:
                    st.image(img_url, caption=f"{tab_names[i]} Image", use_column_width=True)
                col_counters[1] += 1  # Increment counter for column 2

# Separator
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Thank you for visiting Daryl's Bibliography!</div>", unsafe_allow_html=True)
