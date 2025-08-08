import os
import core.config.config as config

def git_clone(repo_url, target_dir):
    # 确保目标目录不存在
    if os.path.exists(target_dir):
        print(f"Directory {target_dir} already exists. Skipping cloning.")
        return

    # 执行 git clone 命令
    command = f"git clone {repo_url} {target_dir}"
    os.system(command)

def init_project(project_data):
    git_clone("https://github.com/open-mmlab/mmdetection3d.git", f"{config.get_project_save_dir()}/mmdetection3d")
    return