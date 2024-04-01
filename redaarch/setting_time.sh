#!/bin/bash

# set up the time
echo "configuring the time has begun"
sleep 3
timedatectl
timedatectl set-ntp true
timedatectl set-timezone Africa/Casablanca
echo "setting up the time has finished"
sleep 3
clear

# updating keyrings
echo "updating the keyrings "
sleep 3
pacman -Sy --needed --noconfirm archlinux-keyring
echo "just updated the keyring for arch \nwhatever that means!"
sleep 3
clear
