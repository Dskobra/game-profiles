#!/usr/bin/bash

mkdir "$HOME"/.config/MangoHud/
python pci.py
chown "$USER":"$USER" *.conf
cp *.conf "$HOME"/.config/MangoHud/