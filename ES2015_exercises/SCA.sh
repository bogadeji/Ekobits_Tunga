#!/usr/bin/bash

UNAME=$(uname)

if [[ "$UNAME" = "Linux" ]]; then
    DISTRO="$(lsb_release -i | awk -F"\t" '{print $2}')"
    if [[ "$DISTRO" = "Ubuntu" || "$DISTRO" = "Debian" ]]; then
        echo "Refreshing Package Manager"
        apt update
        echo "Installing WGet & Curl"
        apt install -y wget curl
        echo "Installing: NodeJS 15"
        curl -sL https://deb.nodesource.com/setup_15.x | bash -
        apt install -y nodejs
    fi
fi

if [UNAME == 'MINGW'] then
    echo "Please install and make use of Windows Subsystem for linux"
fi

if [UNAME == 'Darwin'] then
    if [ [ $(command -v brew) == "" ]] then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    echo "Refreshing Package Manager"
    brew update
    echo "Installing WGet & Curl"
    brew install wget curl node
    echo "wget curl and node packages installed successfully"
fi