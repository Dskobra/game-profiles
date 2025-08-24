#!/usr/bin/bash

python config_pci.py "0:03:00.0"    # insert pci device number
chown "$USER":"$USER" *.conf
mkdir "$HOME"/.config/MangoHud/
cp *.conf "$HOME"/.config/MangoHud/
git stash       # reset profiles after copying

