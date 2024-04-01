#!/bin/bash

virsh list --all > /dev/null 2>&1

virsh start win10 > /dev/null 2>&1


virt-viewer --attach win10

