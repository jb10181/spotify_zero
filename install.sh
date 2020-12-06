#!/bin/bash

echo "Starting installation script"

passwd

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy
sudo apt install libopenjp2-7 libopenjp2-7-dev libopenjp2-tools libatlas-base-dev
sudo pip install st7789

pip install numpy Pillow spotipy

sudo vi /boot/config.txt

# dtparam=audio=off
#
# dtoverlay=hifiberry-dac
# gpio=25=op,dh

curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

git clone https://github.com/jb10181/spotify_zero
cd spotify_zero
sudo cp spotify_pirate.service /lib/systemd/system/spotify_pirate.service
sudo systemctl daemon-reload
sudo systemctl enable spotify_pirate.service
