#!/usr/bin/env python
##############################################################################
# paramiko_example.py
#
# Tries out some Paramiko commands to connect to the Cisco XE router
#
# 06/20/18 - Original code
##############################################################################
import paramiko
import time


def send_command(connection, command):
    connection.send(command+'\n')
    time.sleep(.5)
    output = connection.recv(65535)
    print output


def main():

    # Use Paramiko to create the connection
    pre_connection = paramiko.SSHClient()
    pre_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_connection.connect("192.168.10.80", port=22, username='admin', password='cisco', look_for_keys=False, allow_agent=False)
    connection = pre_connection.invoke_shell()
    output = connection.recv(65535)
    print output

    # send_command(connection,'show ip int brief')
    # send_command(connection,'show ver')

    # configure ospf
    send_command(connection,'config t')
    send_command(connection,'router ospf 1')
    send_command(connection,'network 10.0.0.0 0.255.255.255 area 0')
    send_command(connection,'end')
    send_command(connection,'wr')


if __name__ == "__main__":
    main()
