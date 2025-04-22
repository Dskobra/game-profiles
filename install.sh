#!/usr/bin/bash

mkdir "$HOME"/.config/MangoHud/
python config_pci.py
chown "$USER":"$USER" *.conf
cp *.conf "$HOME"/.config/MangoHud/
git stash       # reset profiles after copying
