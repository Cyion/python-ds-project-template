import os
from pathlib import Path
from argparse import ArgumentParser

_dir_list = [
    "data",
    "docs",
    "models",
    "notebooks",
    "reports",
    "src/projectname/data",
    "src/projectname/model",
    "src/projectname/trainer",
    "src/projectname/visualization",
]

_file_list = [
    "README.md",
    "requirements.txt",
    "src/projectname/__init__.py",
    "src/projectname/data/__init__.py",
    "src/projectname/model/__init__.py",
    "src/projectname/trainer/__init__.py",
    "src/projectname/visualization/__init__.py",
]

def _create_project_structure(args):
    root = f"{args.projectname}/"
    for dir in _dir_list:
        os.makedirs(root + dir.replace("projectname", args.projectname), exist_ok=True)

    for file in _file_list:
        filepath = root + file.replace("projectname", args.projectname)
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            open(filepath,'a')

def _parse_args():
    parser = ArgumentParser(
        description="Make data science projects",
    )
    parser.add_argument(
        "projectname",
        type=str,
        help="Name of the project",
    )
    return parser.parse_args()

if __name__ =="__main__":
    args = _parse_args()
    _create_project_structure(args)
