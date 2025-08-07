import streamlit as st

def show_header():
    # Set page config
    st.set_page_config(
        page_title="Project",
        page_icon="💫",
    )

    # Show all projects
    st.subheader("💫 Project", divider=True)


show_header()