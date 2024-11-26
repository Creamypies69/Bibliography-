import streamlit as st
import pandas as pd

# Title of the application
st.title("Quick Bibliography Manager")

# Subtitle
st.subheader("Add your bibliography entries below:")

# Create a form for inputting bibliography entries
with st.form(key='bibliography_form'):
    entry_type = st.selectbox("Entry Type", ["Book", "Article", "Website"])
    author = st.text_input("Author(s)")
    title = st.text_input("Title")
    year = st.number_input("Year", min_value=1900, max_value=2023, step=1)
    publisher = st.text_input("Publisher (if applicable)")
    url = st.text_input("URL (if applicable)")
    
    # Submit button
    submit_button = st.form_submit_button("Add Entry")

# Initialize or load bibliography
if 'bibliography' not in st.session_state:
    st.session_state.bibliography = []

# Add entry to bibliography if the form is submitted
if submit_button:
    entry = {
        "Entry Type": entry_type,
        "Author": author,
        "Title": title,
        "Year": year,
        "Publisher": publisher,
        "URL": url
    }
    st.session_state.bibliography.append(entry)
    st.success("Entry added successfully!")

# Display the bibliography
st.subheader("Your Bibliography Entries:")
if st.session_state.bibliography:
    # Create a DataFrame from the bibliography entries
    bibliography_df = pd.DataFrame(st.session_state.bibliography)
    st.dataframe(bibliography_df)
else:
    st.write("No entries yet. Add some above!")

# Option to clear the bibliography
if st.button("Clear All Entries"):
    st.session_state.bibliography.clear()
    st.success("All entries cleared!")