import json
import subprocess
from pathlib import Path

from names_generator import generate_name

WORKSPACES_PATH = Path.cwd().parent
CODE_WORKSPACE_PATH = Path("workspaces.code-workspace")


def main():
    # Generate a random name
    random_name = generate_name()

    # Create a virtual environment and pyproject.toml file
    new_workspace_path = WORKSPACES_PATH.joinpath(random_name)
    venv_dest = new_workspace_path.joinpath(".venv")
    subprocess.run(["virtualenv", "--prompt", random_name, venv_dest], check=True)
    subprocess.run(["poetry", "init", "-n"], cwd=new_workspace_path, check=True)

    # Edit .code-workspace
    with open(CODE_WORKSPACE_PATH) as fp:
        code_workspace = json.load(fp)

    code_workspace["folders"] += [{"path": str(new_workspace_path)}]

    with open(CODE_WORKSPACE_PATH, "w") as fp:
        code_workspace = json.dump(code_workspace, fp, indent="\t")

    print("Done!")


if __name__ == "__main__":
    main()
