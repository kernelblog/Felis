# Check for root privileges
if [ $(echo $PREFIX | wc -c) -lt 2 ] && [ $(id -g) -ne 0 ]; then
    echo "This command can only be run with root access."
    exit 1
fi

# Install packages using the appropriate package manager
install_packages() {
    if [ -f /usr/bin/apt ]; then
        apt update
        apt install ffmpeg python3-pip
    elif [ -f "$PREFIX"/bin/apt ]; then
        pkg install ffmpeg python3-pip
        pgk install
    elif [ -f /usr/bin/pacman ]; then
        pacman -S --needed ffmpeg python3-pip
    fi
}

# Find the pip command
determine_pip_cmd() {
    if [ -f /usr/bin/pip3 ]; then
        PIP_CMD="/usr/bin/pip3"
    elif [ -f "$PREFIX/bin/pip" ]; then
        PIP_CMD="$PREFIX/bin/pip"
    else
        PIP_CMD="pip3"
    fi
    echo $PIP_CMD
}

# Install required Python packages
install_python_packages() {
    local pip_cmd=$(determine_pip_cmd)
    $pip_cmd install -r requirements.txt
}

# Main installation function
main_install() {
    install_packages
    install_python_packages

    SETUP_ROOT="/usr"
    if [ $(echo $PREFIX | wc -c) -gt 2 ]; then
        SETUP_ROOT=$PREFIX
    fi

    mkdir -p "$SETUP_ROOT/share/felis" 2>&1
    cp felis "$SETUP_ROOT/bin/"
    cp -r * "$SETUP_ROOT/share/felis/"
    chmod 755 "$SETUP_ROOT/bin/felis"
    chmod 755 "$SETUP_ROOT/share/felis/"*

    echo "Installation completed successfully. You can use it by typing 'felis' in the terminal."
}

main_install
