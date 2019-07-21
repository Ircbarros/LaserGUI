# -*- coding: utf-8 -*-
import os
import pexpect
from pexpect import pxssh
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


# Reads the XML File
xmlFile = et.parse('environment.xml')
# Find the root element from the file (in this case "environment")
root = xmlFile.getroot()


address = root.findtext('TURTLEBOT_IP')
usernameClient = root.findtext('USERNAME')
passwordClient = root.findtext('PASSWORD')
portClient = root.findtext('PORT')

myIP = root.findtext('MY_IP')
masterIP = root.findtext('MASTER_IP')
rosMasterURI = root.findtext('ROS_MASTER_URI')
rosHostname = root.findtext('ROS_HOSTNAME')
rosNamespace = root.findtext('ROS_NAMESPACE')
address = root.findtext('TURTLEBOT_IP')
usernameClient = root.findtext('USERNAME')
passwordClient = root.findtext('PASSWORD')
portClient = root.findtext('PORT')
perspectiveLocation = root.findtext('PERSPECTIVE_LOCATION')
rosSource = root.findtext("ROS_SOURCE")
rosEtc = root.findtext('ROS_ETC_DIRECTORY')
rosRoot = root.findtext('ROS_ROOT')

exportIP = str('ROS_IP='+myIP)
exportMasterIP = str('MASTER_IP='+myIP)
exportMasterIPURI = str('export ROS_MASTER_URI=http://'+myIP+':11311/')
exportRosIP = str('export ROS_IP='+myIP)
exportHostname = str('export ROS_HOSTNAME_IP='+myIP)
exportNamespace = str('export ROS_NAMESPACE='+rosNamespace)
print(exportMasterIP)
print(exportRosIP)
print(exportHostname)
print(exportNamespace)
print(address)


class sshTeleopLaunch():
    def __init__(self, parent=None):
        try:

            client = pxssh.pxssh()
            hostname = address
            username = usernameClient
            password = passwordClient
            client.login(hostname, username, password)
            client.sendline(exportMasterIPURI)
            client.prompt()
            print(client.before)
            client.sendline(exportRosIP)
            client.prompt()
            print(client.before)
            client.sendline('roslaunch turtlebot_teleop keyboard_teleop.launch')
            client.prompt()
            print(client.before)
            client.interact()
            # client.logout()

        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)


if __name__ == "__main__":
    sshTeleopLaunch()
