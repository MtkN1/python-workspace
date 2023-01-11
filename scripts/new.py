import json
import subprocess
from pathlib import Path

from names_generator import generate_name

WORKSPACES_PATH = Path("src")
CODE_WORKSPACE_PATH = Path("python-workspaces.code-workspace")


def main():
    # Generate a random name
    random_name = generate_name()

    # Create a new project and virtualenv
    new_workspace_path = WORKSPACES_PATH.joinpath(random_name)
    venv_dest = new_workspace_path.joinpath(".venv")
    subprocess.run(["poetry", "new", "--src", new_workspace_path], check=True)
    subprocess.run(["virtualenv", "--prompt", random_name, venv_dest], check=True)

    # Edit .code-workspace
    with open(CODE_WORKSPACE_PATH) as fp:
        code_workspace = json.load(fp)

    code_workspace["folders"] += [{"path": str(new_workspace_path)}]

    with open(CODE_WORKSPACE_PATH, "w") as fp:
        code_workspace = json.dump(code_workspace, fp, indent="\t")

    # Open main.py
    package_root_path = new_workspace_path.joinpath("src", random_name, "__init__.py")
    subprocess.run(["code", package_root_path], check=True)

    print("Done!")


if __name__ == "__main__":
    main()
