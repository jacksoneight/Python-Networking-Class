#!/usr/bin/env python
##############################################################################
# netmiko_example.py
#
# Tries out some Netmiko commands to connect to the Cisco XE router
#
# 06/20/18 - Original code
##############################################################################
from netmiko import ConnectHandler

def main():
    # Use Netmiko to create the connection
    connection = ConnectHandler(device_type="cisco_ios", ip="192.168.10.80", username="admin", password="cisco")
    # Grab the running config
    output = connection.send_command("show run")
    # Print the current config
    print ("Current running config: \n")
    print output


if __name__ == "__main__":
    main()
