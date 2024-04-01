#!/bin/bash

############################################################
### Setting up users
############################################################
# setting the password for the root user
echo root:Tzbg5340 | chpasswd
# adding a new user
useradd -m reda --shell /bin/bash
echo reda:1966 | chpasswd

############################################################
### Performing menial tasks 
############################################################
# setting up the timezone
echo "setting up the timezone"
sleep 3
ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime
# syncing the system to hardware clock
echo "syncing the system to hardware clock"
sleep 3
hwclock --systohc
# setting up the locale
echo "setting up the locale"
sleep 3
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
# setting up the language
echo "setting up the language"
sleep 3
echo "LANG=en_US.UTF-8" > /etc/locale.conf
# host name stuff
echo "host name stuff"
sleep 3
echo homeworld16 > /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1       localhost" >> /etc/hosts
echo "127.0.1.1 archmc.localdomain archmc" >> /etc/hosts


############################################################
###  Systemd-boot setup
############################################################
bootctl --path=/boot install
uuid=blkid  $DISK | awk '{print $2}'
touch /boot/loader/entries/arch.conf
echo "title Arch Linux" >> /boot/loader/entries/arch.conf
echo "linux /vmlinuz-linux" >> /boot/loader/entries/arch.conf
echo "initrd  /intel-ucode.img" >> /boot/loader/entries/arch.conf
echo "initrd /initramfs-linux.img" >> /boot/loader/entries/arch.conf
echo "options root=$uuid rw" >> /boot/loader/entries/arch.conf

echo "default arch" >  /boot/loader/loader.conf
echo "timeout 4" >>  /boot/loader/loader.conf
echo "console-mode max" >>  /boot/loader/loader.conf
echo "editor no" >>  /boot/loader/loader.conf

bootctl --path=/boot update

exit
