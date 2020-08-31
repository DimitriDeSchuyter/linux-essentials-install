#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import echo, command

echo.title("Adding current user to the docker group")
command.exec("groupadd docker")
command.exec("usermod -aG docker $SUDO_USER")
command.exec("printf \" \" && grep 'docker' /etc/group")