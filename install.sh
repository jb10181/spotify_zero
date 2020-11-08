#!/bin/bash

echo "Starting installation script"

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy libatlas-base-dev
sudo pip install st7789

pip install numpy Pillow spotipy

curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

sudo raspi-config
