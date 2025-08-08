import os
import yaml
import core.config.config as config
import streamlit as st

def show_projects():
    project_config_dir = config.get_project_config_dir()

    projects = []
    for root, dirs, files in os.walk(project_config_dir):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        project_data = yaml.safe_load(f)
                        projects.append(project_data)
                        st.write(file)
                        st.write(project_data)

                except Exception as e:
                    st.error(f"Parse project file: {file_path} failed: {str(e)}")

    return projects
    return

def show_header():
    # Set page config
    st.set_page_config(
        page_title="Project",
        page_icon="💫",
    )

    # Show all projects
    st.subheader("💫 Project", divider=True)


show_header()
show_projects()