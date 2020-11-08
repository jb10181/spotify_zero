#!/bin/bash

echo "Starting installation script"

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python-rpi.gpio python-spidev python-pip python-pil python-numpy
sudo pip install st7789

pip install spotipy 

curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

sudo raspi-config