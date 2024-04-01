#!/bin/bash
#
# selected=$(echo -e "Option 1\nOption 2\nOption 3" | dmenu -p "Choose an option:")

word=$(echo "" | dmenu -p "Enter a word"   -fn 'JetBrainsMono Nerd Font Mono,JetBrainsMono NFM Light:style=Bold,Regular:size=18' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#ffd700' -sb '#333333')

qutebrowser --set zoom.default 125  --target window https://www.merriam-webster.com/dictionary/$word


