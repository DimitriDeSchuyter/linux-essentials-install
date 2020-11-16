#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import echo, command

echo.title("Installing Docker")
command.exec("curl -fsSL https://get.docker.com | sudo sh")

## Creating config.json
command.exec("mkdir ~/.docker")
command.exec("cp docker/config.json ~/.docker/config.json")