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
config_file = '/etc/ansible/gns3.ini'

# Retrieve the contents of the INI file
config = configparser.ConfigParser()
config.read_file(open(config_file))

gns3_server_address = config.get('gns3', 'gns3_server_address')
gns3_server_port = config.get('gns3', 'gns3_server_port')

# URL for the GNS3 projects API (documentation available at https://gns3-server.readthedocs.io)
projects_api_link = "http://"+gns3_server_address+":"+gns3_server_port+"/v2/projects"


# Query the projects API for existing GNS3 projects
def retrieve_projects():
    global open_id
    projects_request = requests.get(projects_api_link)
    projects_response = projects_request.json()

    if projects_request.status_code == 200:
        for project in projects_response:
            if project['status'] == "opened":
                open_id = str(project['project_id'])
    elif projects_response.status_code == 404:
        open_id = str('Server cannot reach the GNS3 API.')

    return open_id


# Form the URL for the nodes API
project_id = retrieve_projects()
nodes_api_link = "http://"+gns3_server_address+":"+gns3_server_port+"/v2/projects/"+project_id+"/nodes"

def retrieve_nodes():
    nodes_request = requests.get(nodes_api_link)
    nodes_response = nodes_request.json()

    inventory = {'_meta': {'hostvars': {}}}

    if nodes_request.status_code == 200:
        for node in nodes_response:
            group = node['name']
            host = node['name']
            if group not in inventory:
                inventory[group] = {'hosts': [], 'vars': {}}
                inventory[group]['hosts'].append(host)

    print(json.dumps(inventory, indent=4))


retrieve_nodes()

