#!/usr/bin/env bash

choice="$(echo -e "start win10\nstop win10\nssh to win10" | fzf --header="I fucking hate Windows!" --header-first --border=rounded)"
windows_line="$(virsh list --all | grep -i win10)"
if [ "$choice" = "start win10" ];then
    if echo "$windows_line" | grep -q "shut off";then
        virsh start fucking-win10
        sleep 20
        ssh reda@192.168.122.167
    fi
elif [ "$choice" = "stop win10" ];then
    virsh shutdown fucking-win10
elif [ "$choice" = "ssh to win10" ];then
    ssh reda@192.168.122.167
fi

