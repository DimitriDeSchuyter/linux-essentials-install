############################################################################
## Install file for local MariaDB                                         ##
## Author: Dimitri De Schuyter                                            ##
## Mail: dimitri.deschuyter@gmail.com                                     ##
############################################################################
import sys
import os
path = os.popen("cd /usr/local/lib/python3.?/dist-packages/ && pwd").read().rstrip()
sys.path.append(path + "/depuydt/src/")

from depuydt import command,environment,echo
command.exec("sudo apt update && sudo apt upgrade -y");
command.exec("sudo apt-get install -y mariadb-server");
command.exec("sudo chmod 0444 /etc/mysql/my.cnf")
os.system("cd && sudo mysql_secure_installation && cd /mnt/usb/linuxEssentials");