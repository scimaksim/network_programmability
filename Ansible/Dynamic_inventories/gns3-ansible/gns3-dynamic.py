#!/usr/bin/env python
#
# Created by Maksim Nikiforov (maksim@redhat.com)
# This script retrieves nodes from GNS3 and dynamically populates an Ansible Tower inventory
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GNS3 is a Free and Open Source software under GPL v3 licensing (https://www.gns3.com)
# Red Hat® Ansible Tower® is a registered trademark of Red Hat, Inc. in the United States and other countries.

import json
# Import configparser to parse associated INI file
import configparser
# Import requests library to work with GNS3 API
import requests
import re

# Set location for the INI file on the Ansible Tower server
#config_file = '/etc/ansible/gns3.ini'
config_file = '/home/maksim/Documents/gns3-ansible/gns3.ini'
config = configparser.ConfigParser()

# Retrieve the contents of the INI file
config.read_file(open(config_file))

gns3_server_address = config.get('gns3', 'gns3_server_address')
gns3_server_port = config.get('gns3', 'gns3_server_port')
# gns3_project_uid =

gns3_api_url = "http://"+gns3_server_address+":"+gns3_server_port+"/v2/projects/ae9d8bb9-5280-4038-8ac4-a5708593e0ca" \
                                                                  "/nodes"
response = requests.get(gns3_api_url)
data = response.json()

inventory = {'_meta': {'hostvars': {}}}


if response.status_code == 200:
    for node in data:
        group = node['name']
        host = node['name']
        dict1 = {'hostname': host}
        if group not in inventory:
            inventory[group] = {'hosts': [], 'vars': {}}
        inventory[group]['hosts'].append(host)

    print(json.dumps(inventory, indent=4))

elif response.status_code == 404:
    print('Not Found.')

