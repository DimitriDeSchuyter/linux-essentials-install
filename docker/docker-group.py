#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import echo, command

import os
user = os.getlogin()

echo.title("Adding current user to the docker group")
command.exec("groupadd docker")
command.exec("sudo usermod -aG docker " + str(user))
command.exec("grep 'docker' /etc/group")