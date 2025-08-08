import os

def get_workspace_dir():
    return f"{os.getcwd()}/workspace"

def get_project_config_dir():
    return f"{get_workspace_dir()}/config/project"