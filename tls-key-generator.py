############################################################################
## Author: Dimitri De Schuyter                                            ##
## Mail: dimitri.deschuyter@gmail.com                                     ##
############################################################################
import sys
import os
path = os.popen("cd /usr/local/lib/python3.?/dist-packages/ && pwd").read().rstrip()
sys.path.append(path + "/depuydt/src/")
from depuydt import command,environment,echo

echo.notice("install libnss3 and golang");
command.exec("sudo apt-get install libnss3-tools");
command.exec("sudo apt-get install golang");

echo.notice("install mkcert");
command.exec("git clone https://github.com/FiloSottile/mkcert && cd mkcert");
command.exec("go build -ldflags '-X main.Version=$(git describe --tags)'");
command.exec("mkcert -install");

echo.notice("Create certificate for domain name");
env = environment.Environment("~/.env");
domainName=env.get("DOMAINNAME");
command.exec("mkcert -key-file key.pem -cert-file cert.pem " + domainName + " *." + domainName)
command.exec("mkdir /mnt/usb/certs")
command.exec("mv key.pem /mnt/usb/certs/")
command.exec("mv cert.pem /mnt/usb/certs/")