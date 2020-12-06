#!/bin/bash

echo "Starting installation script"

echo "Set a new password"
passwd

echo "Install latest updates"
sudo apt-get update
sudo apt-get upgrade

echo "Install required apt packages"
sudo apt-get install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy
sudo apt install libopenjp2-7 libopenjp2-7-dev libopenjp2-tools libatlas-base-dev

echo "Install required python packages"
pip install st7789 numpy Pillow spotipy os time requests io

echo "Set the following parameters
# dtparam=audio=off
#
# dtoverlay=hifiberry-dac
# gpio=25=op,dh"
sudo vi /boot/config.txt

echo "Install raspotify"
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

echo "Install spotify_zero, set up systemd service"
git clone https://github.com/jb10181/spotify_zero
cd spotify_zero
sudo cp spotify_pirate.service /lib/systemd/system/spotify_pirate.service
sudo systemctl daemon-reload
sudo systemctl enable spotify_pirate.service
