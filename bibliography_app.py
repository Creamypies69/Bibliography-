import streamlit as st

# Define the new color theme
text_color = "#000000"  # Black text for better contrast
highlight_color = "#87CEEB"  # Light sky blue

image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 
link_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/9c00f063fcdf27e3dc87b1793304ddacbe4f634c/20241121_151401.jpg" 

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Creamypies69/Bibliography-/main/Night%20Sky%20Wallpapers%20-%20Wallpaper%20Cave.jpeg?raw=true"

# Set background and text styles
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: 
            url('{background_image_url}');
        background-size: cover;
        background-attachment: fixed; /* Keeps the background fixed on scroll */
        color: {text_color};
    }}
    .sidebar .sidebar-content {{
        background: rgba(255, 255, 255, 0.8); /* Light background for sidebar */
    }}
    h1 {{
        color: {highlight_color};
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7); /* Light shadow effect for title */
    }}
    h2, h3, h4, h5, h6 {{
        color: {highlight_color};
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7); /* Light shadow effect for subtitles */
    }}
    .stButton > button {{
        background-color: {highlight_color};
        color: {text_color};
    }}
    .shadow {{
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Lighter shadow effect for elements */
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        display: flex;
        justify-content: center; /* Center the content */
    }}
    .image-container {{
        display: flex;
        justify-content: center; /* Center the image */
        align-items: center; /* Center vertically if needed */
    }}
    .responsive-image {{
        width: 80%; /* Adjust this percentage for responsiveness */
        max-width: 300px; /* Maximum width for larger screens */
        border-radius: 5px; /* Optional: rounded corners for the image */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title with shadow
st.markdown('<h1 style="text-align: center;">Daryl\'s Bibliography</h1>', unsafe_allow_html=True)

# Display picture with shadow and responsive design
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

# Personal details section with shadow
personal_details = (
    "<div class='shadow'>"
    "<h3>Personal Details</h3>"
    "<p><strong>Age:</strong> 18</p>"
    "<p><strong>Education:</strong> Bachelor of Science in Computer Engineering (BSCpE)</p>"
    "<p><strong>University:</strong> Surigao del Norte State University (SNSU)</p>"
    "<p><strong>High School:</strong> Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS)</p>"
    "<p><strong>Location:</strong> Barangay Taft, Surigao City, Surigao del Norte, Philippines</p>"
    "</div>"
)

# Show personal details with shadow
st.markdown(personal_details, unsafe_allow_html=True)

# Brief description section with shadow
brief_description = (
    "<div class='shadow'>"
    "<h2>Brief Description</h2>"
    "<p>Daryl enjoys spending his free time immersed in books and visual novels, balancing his intellectual pursuits with casual gaming sessions. "
    "For the past three years, he has been in a loving relationship with his girlfriend, KC Aspacio, who shares and supports his laid-back and creative nature.</p>"
    "</div>"
)

# Show brief description
