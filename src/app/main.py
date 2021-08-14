#!/usr/bin/env python3

import subprocess
import helpers

# Sample lightsail
#aws lightsail create-instances-from-snapshot --instance-snapshot-name WordPress-1-1569866208 --instance-names WordPress-2 --availability-zone us-west-2a --bundle-id medium_2_0

# Main
def main():
    data = helpers.app()

    for k,immutable in data['immutables'].items():
        if (immutable['type'] == "lightsail"):
            subprocess.call(['aws', 'lightsail','create-instances-from-snapshot', '--instance-snapshot-name', immutable['refer'], '--instance-names', immutable['name'], '--availability-zone', 'eu-central-1a', '--bundle-id', 'medium_2_0'])

# Execute
if __name__ == '__main__':
    main()