#!/usr/bin/env python3
# author sasidhar

import os,platform
kernel = platform.platform().split("-")[0]
kernel_version = platform.platform().split("-")[1]
architecture = platform.architecture()[0]
desktop = os.getenv("XDG_CURRENT_DESKTOP")
shell = os.getenv("SHELL").split("/")[-1].upper()
user_name = os.getlogin()
uptime = os.popen("uptime -p").read()[3:]
os_name = os.popen("lsb_release -d").read().split(":")[1].strip()
#print(os_name)
pacman = os.popen("pacman -Qq | wc -l ").read()
aur = os.popen("pacman -Qm | wc -l ").read()
try:
	guix_packages = os.popen("guix package --list-installed | wc -l").read()
except Exception as e:
	guix_packages = e

hostname = os.popen("cat /etc/hostname").read().strip()


def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

print("USER AND HOST_NAME",end="		")
prRed(f': {user_name}@{hostname}')

print("OS                              ",end="")
prRed(f': {os_name}')

print("KERNEL                          ",end="")
prRed(f': {kernel} {kernel_version}')

print("ARCHITECTURE                    ",end="")
prRed(f': {architecture}')

print("DESKTOP                         ",end="")
prRed(f': {desktop}')

print("SHELL                           ",end="")
prRed(f': {shell}')

print("UPTIME                          ",end="")
prRed(f': {uptime}')

print("PACKAGES                        ",end="")
prRed(f': pacman {pacman}\t\t\t\t aur {aur}\t\t\t\t guix-packages {guix_packages}')

















