#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%% This script is going to be completed bit by bit
#%%%%% as I am setting up my working env
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


######################################################################
### General Settings
######################################################################
username=reda

######################################################################
### Installing my favorite software
######################################################################
# my go to text editor [more like a lifestyle]
pacman -Sy vim   
# zathura with epub, pdf ... support
pacman -Sy zathura zathura-pdf-mupdf  
# vifm is a cozy file manager for a vim user
pacman -Sy vifm
# dunst as my go-to notification daemon
pacman -Sy dunst

######################################################################
### Creating Symlinks for dotfiles and such
######################################################################
ln -sf /home/$username/dotfiles/.vimrc /home/$username/.vimrc
ln -sf /home/$username/dotfiles/.bashrc /home/$username/.bashrc
ln -sf /home/$username/dotfiles/.config/zathura /home/$username/.config/zathura
ln -sf /home/$username/dotfiles/.config/vifm /home/$username/.config/vifm
ln -sf /home/$username/dotfiles/.config/dunst /home/$username/.config/dunst
ln -sf ~/dotfiles/.config/mimeapps.list ~/.config/mimeapps.list



######################################################################
### setting up .xinitrc, Xsession etc
######################################################################
# dunst should start with the X server
echo "dunst &" >> ~/.xinitrc
# torrenting setup using transmission-cli
# I might want to use a systemd job instead
echo "transmission-daemon &" >> ~/.xinitrc
echo "transmission-rss -f &" >> ~/.xinitrc
