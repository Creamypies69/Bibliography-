import streamlit as st

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/main/Night%20Sky%20Wallpapers%20-%20Wallpaper%20Cave.jpeg"

# CSS styles for the app
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('{background_image_url}');
        background-size: cover; /* Cover the area */
        background-attachment: fixed; /* Fixed during scroll */
        background-position: center; /* Center the image */
    }}
    .sidebar .sidebar-content {{
        background: rgba(255, 255, 255, 0.8); /* Semi-transparent sidebar */
    }}
    h1 {{
        color: #f63366;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }}
    h2, h3 {{
        color: #f63366;
        font-size: 24px; /* Consistent font size */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }}
    .stButton > button {{
        background-color: #f63366;
        color: #ffffff;
    }}
    .shadow {{
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        display: flex;
        justify-content: center;
    }}
    .image-container {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .responsive-image {{
        width: 80%;
        max-width: 300px;
        border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 style="text-align: center;">Daryl\'s Bibliography</h1>', unsafe_allow_html=True)

# Image display
image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 
link_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 

st.markdown(
    f"""
    <div class="shadow image-container">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" alt="Daryl's Image" class="responsive-image">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Personal details section
st.markdown("<h3>Personal Details</h3>", unsafe_allow_html=True)
personal_details = (
    "<div class='shadow'>"
    "<p><strong>Age:</strong> 18</p>"
    "<p><strong>Education:</strong> Bachelor of Science in Computer Engineering (BSCpE)</p>"
    "<p><strong>University:</strong> Surigao del Norte State University (SNSU)</p>"
    "<p><strong>High School:</strong> Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)</p>"
    "<p><strong>Location:</strong> Barangay Taft, Surigao City, Surigao del Norte, Philippines</p>"
    "</div>"
)

# Show personal details
st.markdown(personal_details, unsafe_allow_html=True)

# Brief description section
st.markdown("<h2>Brief Description</h2>", unsafe_allow_html=True)
brief_description = (
    "<div class='shadow'>"
    "<p>Daryl enjoys reading and gaming in his free time. He has been in a loving relationship with his girlfriend, KC Aspacio, for three years.</p>"
    "</div>"
)

# Show brief description
st.markdown(brief_description, unsafe_allow_html=True)
