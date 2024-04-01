#!/usr/bin/env bash

# this script runs the command systemctl --failed and notify me for failed services
# it will run as a cron job everyday at 9pm
#

export DISPLAY=:0

run_command() {
    systemctl --failed | grep -qi "0 loaded units listed."
}

if [ run_command ];then
    notify-send  -t 0 "system maintenance" "all systemd units are green"
else
    notify-send -u critical -t 0 "system maintenance" "RED ALERT : failed sysd units "
fi
