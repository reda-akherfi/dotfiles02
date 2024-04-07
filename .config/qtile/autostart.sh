#!/usr/bin/env bash

clipcatd --replace
kill $(pgrep sxhkd)
sxhkd &
redshift -x
redshift -O 4000
nm-applet &
killall cbatticon
cbatticon &
killall volumeicon
volumeicon &


