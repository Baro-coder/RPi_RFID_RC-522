#!/bin/bash

GITHUB_URL="https://github.com/Baro-coder/RPi_RFID_RC-522"
WORKDIR="RPi_RFID_RC-522"

echo " > sudo apt update"
sudo apt update

echo " > sudo apt upgrade"
sudo apt upgrade

echo " > sudo apt install python3-dev python3-pip"
sudo apt install python3-dev python3-pip

echo " > sudo pip3 install spidev mfrc522"
sudo pip3 install spidev mfrc522
