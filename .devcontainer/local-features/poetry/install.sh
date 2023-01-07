#!/usr/bin/env bash
#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

USERNAME=${USERNAME:-"vscode"}

set -eux

if [ "$(id -u)" -ne 0 ]; then
    echo -e 'Script must be run as root. Use sudo, su, or add "USER root" to your Dockerfile before running this script.'
    exit 1
fi

sudo_if() {
    COMMAND="$*"
    if [ "$(id -u)" -eq 0 ] && [ "$USERNAME" != "root" ]; then
        su - "$USERNAME" -c "$COMMAND"
    else
        "$COMMAND"
    fi
}

export DEBIAN_FRONTEND=noninteractive

install_python_package() {
    PACKAGE=${1:-""}

    echo "Installing $PACKAGE..."
    sudo_if pipx install --pip-args="--no-cache-dir" $PACKAGE
}

if [[ "$(pipx --version)" != "" ]]; then
    install_python_package "poetry~=1.3.0"
else
    "(*) Error: Need to install pipx."
fi

echo "Done!"
