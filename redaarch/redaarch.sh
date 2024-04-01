############################################################
## This is my own arch install script 
## It is a minimal one since all customization is done
## through my dotfiles' install.sh
############################################################


# making the font get bigger
# echo "this is the font before:"
# sleep 3
# setfont ter-132b
# echo "this is the font after"
# sleep 3
# clear







	


############################################################
## Last thing to do is a bit of mounting cleanup
############################################################
umount -R /mnt/boot
umount -R /mnt
reboot
