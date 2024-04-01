#!/usr/bin/env bash

# get all the ssids and list them by name, security...
#
# when i click on an ssid : it needs to check if that connection exists or not 
# if it exists, it should try and connect
# and if it doesn't, it should prompt me for a password
#
# a wifi that i am connected to needs to have  an indication nex to it
# the script needs to keep checking if I am connected to a network every 5 secs while i am using it 
# and change the indication accordingly
#

# listing all the ssids 
SSID_LIST=$(nmcli --fields "SSID" device wifi list| sed '/^--/d')
for el in $SSID_LIST;
    do
        echo "$el"
    done
echo $SSID_LIST
