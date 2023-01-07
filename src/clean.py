import json
import os
import subprocess
from pathlib import Path

WORKSPACES_PATH = Path(".workspaces")
CODE_WORKSPACE_PATH = Path("workspace.code-workspace")


def main():
    if not WORKSPACES_PATH.exists():
        return

    with open(CODE_WORKSPACE_PATH) as fp:
        code_workspace = json.load(fp)

    workspace_paths = {x["path"] for x in code_workspace["folders"]}

    with os.scandir(WORKSPACES_PATH) as it:
        for entry in it:
            if entry.is_dir():
                if entry.path not in workspace_paths:
                    subprocess.run(["rm", "-rf", entry.path])
                    print(f"Removed {entry.path}")

    print("Done!")


if __name__ == "__main__":
    main()
