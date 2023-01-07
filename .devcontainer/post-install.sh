#!/usr/bin/env bash
#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

set -eux

if [[ "$(poetry --version)" != "" ]]; then
    poetry completions bash >> ~/.bash_completion
    poetry config virtualenvs.in-project true
else
    "(*) Error: Need to install poetry."
fi

if [[ "$(virtualenv --version)" != "" ]]; then
    virtualenv --prompt python-workspace .venv
else
    "(*) Error: Need to install virtualenv."
fi

if [ -f "./pyproject.toml" ]; then
    poetry install --no-root
fi

if [ ! -f "./workspace.code-workspace" ]; then
    cp ./.devcontainer/default-workspace.json ./workspace.code-workspace
fi

echo "Done!"
