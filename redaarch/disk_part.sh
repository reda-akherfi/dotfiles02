#!/bin/bash


############################################################
###  Disk Partitionning 
############################################################

# $ parted [options] [device [command [options...]...]]
echo "partitionning the disk"
sleep 3
lsblk
DISK="here goes the disk"
read -p "enter the disk name in here, pay attention to typos" DISK
# use parted
parted $DISK --script mklabel gpt
parted $DISK --script mkpart fat32 1MiB 301MiB
parted $DISK --script set 1 esp on
parted $DISK --script mkpart ext4 301MiB 100%
# making the file system -- formatting
mkfs.fat -F 32 ${DISK}1
mkfs.ext4 ${DISK}2
# mounting the partitions
mount ${DISK}2 /mnt
mount --mkdir ${DISK}1 /mnt/boot
