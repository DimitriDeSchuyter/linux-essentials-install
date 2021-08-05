#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

from depuydt import command, echo, environment
from depuydt.file import File

echo.section("Linux essentials - INSTALL", "Setting environment variables")
f = File("~/.env", "w") 
f.close()

env = environment.Environment("~/.env")
hostname = env.require("HOSTNAME")
domainname = env.require("DOMAINNAME")
env.save()

os.environ["HOSTNAME"] =hostname;
echo.notice(os.environ["HOSTNAME"] )

os.environ["DOMAINNAME"] =domainname;
echo.notice(os.environ["DOMAINNAME"] )

# Writing hostname to /etc/hostname and /etc/hosts file
command.exec("sudo chmod 666 /etc/hostname /etc/hosts")
f = File("/etc/hostname", "w")
f.write(str(hostname))
f.close()
f = File("/etc/hosts", "a")
f.write("127.0.0.1    " + str(hostname))
f.close()
command.exec("sudo chmod 644 /etc/hostname /etc/hosts")