import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title { 
        color: #6A0C9A; 
        text-align: center; 
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Soft drop shadow for title */
    }
    .separator { 
        border: none; 
        height: 2px; 
        background-color: #6A0C9A; 
        margin: 10px 0; 
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Soft drop shadow for separator */
    }
    .name-tag {
        text-align: center; 
        font-size: 20px; 
        color: black;  
        background-color: #E6E6FA; 
        padding: 10px; 
        border-radius: 5px; 
        width: 250px; 
        margin: 0 auto;  
        font-weight: bold;  
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Soft drop shadow for name tag */
    }
    .description { 
        font-size: 18px; 
        text-align: center; 
        margin: 0 auto; 
        width: 80%; /* Set a width for the description to keep it in block format */
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Soft drop shadow for description */
    }
    .footer { 
        text-align: center; 
        margin-top: 20px; 
        color: #6A0C9A; 
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Soft drop shadow for footer */
    }
    .profile-image { 
        display: block; 
        margin: 0 auto; 
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Soft drop shadow for image */
    }  
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and separator
st.title("Daryl's Bibliography")
st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# Create columns for description, name tag, and profile picture
col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed

# Description in the first column
with col1:
    st.markdown("<div class='description'>"
                "<strong>Daryl E. Sagranada</strong> is an 18-year-old college student pursuing a BSCpE at SNSU. "
                "He graduated from DREESMNHS and lives in Surigao City. He dreams of building a network of autonomous computers. "
                "In his free time, he enjoys reading and gaming. He is in a loving relationship with his girlfriend, KC Aspacio."
                "</div>", unsafe_allow_html=True)  # Description

# Profile section with centered layout in the second column
with col2:
    profile_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg"
    st.markdown(f"<img src='{profile_image_url}' width='150' class='profile-image' alt='Daryl E. Sagranada'/>", unsafe_allow_html=True)  # Set width to 150 pixels
    st.markdown("<div class='name-tag'>Daryl E. Sagranada</div>", unsafe_allow_html=True)  # Name tag

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
                "Phone": "097 049786 ```python
    "Email": "darylsagranada@example.com"
            }
            for key, value in details.items():
                st.write(f"**{key}:** {value}")

    with col2:
        with st.expander("Competencies", expanded=True):
            competencies = [
                "Programming in Python, Java, and C++",
                "Web Development (HTML, CSS, JavaScript)",
                "Data Structures and Algorithms",
                "Machine Learning Basics",
                "Game Development"
            ]
            for competency in competencies:
                st.write(f"- {competency}")

# Footer
st.markdown("<div class='footer'>Thank you for visiting my bibliography!</div>", unsafe_allow_html=True)
