import streamlit as st

st.set_page_config(page_title="Daryl's Biography", page_icon="📚")

text_color = "#ffffff"
highlight_color = "#00bcd4"

background_image_url = "https://github.com/Creamypies69/Bibliography-/blob/48bbce79292518dc98bcca0f071f6890bf4c4b6c/Night%20Sky%20Wallpapers%20-%20Wallpaper%20Cave.jpeg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: 
            linear-gradient(to bottom, rgba(30, 30, 47, 1), rgba(30, 30, 47, 0)), 
            url('{background_image_url}');
        background-size: cover;
        color: {text_color};
    }}
    .sidebar .sidebar-content {{
        background: rgba(30, 30, 47, 0.8);
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {highlight_color};
    }}
    .stButton > button {{
        background-color: {highlight_color};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

person_description = {
    "name": "Daryl Escaño Sagranada",
    "description": "Daryl is an 18-year-old college student currently pursuing a Bachelor of Science in Computer Engineering (BSCpE) at Surigao del Norte State University (SNSU). A proud graduate of Don Ruben Edera Ecleo Sr. Memorial National High School (DREESMNHS), he resides on Narciso Rosales Street in Barangay Taft, Surigao City, Surigao del Norte, Philippines. Daryl enjoys spending his free time immersed in books and visual novels, balancing his intellectual pursuits with casual gaming sessions. For the past three years, he has been in a loving relationship with his girlfriend, KC Aspacio, who shares and supports his laid-back and creative nature."
}

st.title("Daryl's Biography")

st.subheader("Brief Description")
st.write(f"**Name:** {person_description['name']}")
st.write(f"**Description:** {person_description['description']}")
st.write("---")

image_url = "https://github.com/Creamypies69/Bibliography-/blob/48bbce79292518dc98bcca0f071f6890bf4c4b6c/20241121_151401.jpg" 
link_url = "https://github.com/Creamypies69/Bibliography-/blob/48bbce79292518dc98bcca0f071f6890bf4c4b6c/20241121_151401.jpg" 

st.markdown(
    f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" alt="Daryl's Image" width="300">
    </a>
    """,
    unsafe_allow_html=True
)

if st.button("Refresh"):
    st.experimental_rerun()
