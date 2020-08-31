#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from pprint import pprint

## TITLE
print("Installation Part 01", "Installing libraries, binaries and shares")

## Installing python libraries and binaries
import os
path = os.popen("cd /usr/local/lib/python3.?/dist-packages/ && pwd").read().rstrip()
os.system("sudo git clone https://github.com/fredericdepuydt/python-libraries.git " + path + "/depuydt")

## INCLUDES
from depuydt import command

## Installing python binaries
command.exec("sudo git clone https://github.com/fredericdepuydt/python-binaries.git /usr/local/bin/python3")
command.exec("sudo chmod +x /usr/local/bin/python3/*")

## Installing shares
command.exec("sudo cp -a share/. /usr/local/share/")