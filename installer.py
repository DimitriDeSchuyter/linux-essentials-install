#!/usr/bin/env python3

############################################################################
## Linux installation script (MANDATORY)                                  ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing part X requires all previous mandatory parts to be installed ##
############################################################################

exec(open("lib-bin-share.py").read())

from depuydt import echo

echo.section("Linux essentials - INSTALL", "Installing Docker and Docker-Compose")
exec(open("docker/docker-install.py").read())
exec(open("docker/docker-group.py").read())
exec(open("docker/docker-compose-install.py").read())