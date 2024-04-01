#!/bin/bash

############################################################
### Setting up users
############################################################
# setting the password for the root user
echo "setting the password for the root user\n"
echo root:Tzbg5340 | chpasswd
sleep 3
# adding a new user
echo "adding a new user\n"
useradd -m reda --shell /bin/bash
sleep 3
# setting up the password for reda
echo "setting up the password for reda\n"
echo reda:1966 | chpasswd
sleep 3
# adding reda to certain groups
echo "adding reda to certain groups\n"
sed -i 's/^# %wheel ALL=(ALL:ALL) ALL/%wheel ALL=(ALL:ALL) ALL/' /etc/sudoers
usermod -a -G wheel,storage,power,audio reda
sleep 3

############################################################
### Performing menial tasks 
############################################################
# setting up the timezone
echo "setting up the timezone"
ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime
sleep 3
# syncing the system to hardware clock
echo "syncing the system to hardware clock"
hwclock --systohc
sleep 3
# setting up the locale
echo "setting up the locale"
sed -i 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
sleep 3
locale-gen
sleep 3
# setting up the language
echo "setting up the language"
echo "LANG=en_US.UTF-8" > /etc/locale.conf
sleep 3
# host name stuff
echo "host name stuff"
sleep 3
#setting up the host name
echo "setting up the host name\n"
echo homeworld16 > /etc/hostname
sleep 2
# setting  up the /etc/hosts file
echo "setting  up the /etc/hosts file\n"
cat <<EOF > /etc/hosts
127.0.0.1 localhost
::1       localhost
127.0.1.1 archmc.localdomain archmc
EOF
sleep 2


############################################################
### misc
############################################################
# enabling the NetworkManager service
echo "enabling the NetworkManager service\n"
systemctl enable NetworkManager.service


