#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import echo, file

echo.section("Linux essentials - INSTALL", "Appending bash files contents")

file.append(".bash_aliases","~/.bash_aliases")
file.append(".bash_env","~/.bash_env")
file.append(".bash_logout","~/.bash_logout")
file.append(".bashrc","~/.bashrc")