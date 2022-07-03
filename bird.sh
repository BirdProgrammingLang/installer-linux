sudo ./bdins $(getent passwd $SUDO_USER | cut -d: -f6)
