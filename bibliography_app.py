import streamlit as st

st.set_page_config(page_title="Single Person Description", page_icon="📚")

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
    "name": "Alice Smith",
    "description": "Alice Smith is a dedicated environmental scientist focused on climate change research and sustainable practices."
}

st.title("Person Description")

st.subheader("Brief Description")
st.write(f"**Name:** {person_description['name']}")
st.write(f"**Description:** {person_description['description']}")
st.write("---")

if st.button("Refresh"):
    st.experimental_rerun()
