#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import echo, command

import os, pwd
user = pwd.getpwuid(os.getuid())[0]

echo.title("Adding current user to the docker group")
command.exec("groupadd docker")
command.exec("sudo usermod -aG docker " + str(user))
command.exec("grep 'docker' /etc/group")