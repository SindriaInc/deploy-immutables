#!/usr/bin/env python3

import os
import subprocess

import helpers

# Pycharm pydevd
PYCHARM_PYDEVD_ENABLED = int(os.getenv('PYCHARM_PYDEVD_ENABLED'))
PYCHARM_PYDEVD_HOST = str(os.getenv('PYCHARM_PYDEVD_HOST'))
PYCHARM_PYDEVD_PORT = int(os.getenv('PYCHARM_PYDEVD_PORT'))

# Enable pydevd debugger
if (PYCHARM_PYDEVD_ENABLED):
    import pydevd_pycharm
    pydevd_pycharm.settrace(PYCHARM_PYDEVD_HOST, port=PYCHARM_PYDEVD_PORT, stdoutToServer=True, stderrToServer=True)

# Sample lightsail
#aws lightsail create-instances-from-snapshot --instance-snapshot-name WordPress-1-1569866208 --instance-names WordPress-2 --availability-zone us-west-2a --bundle-id medium_2_0

# Sample ec2
#aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e



# Main
def main():
    data = helpers.app()

    for k,immutable in data['immutables'].items():
        # Process lightsail deployments
        if (immutable['type'] == "lightsail"):
            subprocess.call(['aws', 'lightsail','create-instances-from-snapshot', '--instance-snapshot-name', immutable['refer'], '--instance-names', immutable['name'], '--availability-zone', immutable['zone'], '--bundle-id', immutable['bundle']])

        # Process ec2 deployments
        if (immutable['type'] == "ec2"):
            subprocess.call(['aws', 'ec2', 'run-instances', '--image-id', immutable['refer'], '--instance-names', immutable['name'], '--availability-zone', immutable['zone'], '--bundle-id', immutable['bundle']])


# Execute
if __name__ == '__main__':
    main()