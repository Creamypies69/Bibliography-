import streamlit as st

st.set_page_config(page_title="Daryl's Bibliography ", page_icon="📚")

background_color = "#1e1e2f"
text_color = "#ffffff"
highlight_color = "#00bcd4"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: {background_color};
        color: {text_color};
    }}
    .sidebar .sidebar-content {{
        background: {background_color};
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

st.title("Daryl's Bibliography")

st.subheader("Brief Description")
st.write(f"**Name:** {person_description['name']}")
st.write(f"**Description:** {person_description['description']}")
st.write("---")

if st.button("Refresh"):
    st.experimental_rerun()
