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


class GNS3Inventory:
    def __init__(self, gns3_address, gns3_port):
        self.gns3_address = gns3_address
        self.gns3_port = gns3_port
        self.inventory = {'_meta': {'hostvars': {}}}
        self.api_link = ("http://"+self.gns3_address+":"+self.gns3_port+"/v2/projects")
        self.retrieve_projects()

    def retrieve_projects(self):
        """Identify the ID of the open GNS3 project"""
        projects_query = requests.get(self.api_link)
        projects_response = projects_query.json()

        if projects_query.status_code == 200:
            for project in projects_response:
                if project['status'] == "opened":
                    self.retrieve_nodes(project['project_id'])
        elif projects_query.status_code == 404:
            print('Server cannot reach the GNS3 projects API.')

    def retrieve_nodes(self, project_id):
        """Retrieve nodes from the open project"""
        nodes_request = requests.get(self.api_link + "/"+project_id+"/nodes")
        nodes_response = nodes_request.json()

        if nodes_request.status_code == 200:
            for node in nodes_response:
                group = node['name']
                host = node['name']
                if group not in self.inventory:
                    self.inventory[group] = {'hosts': [], 'vars': {}}
                    self.inventory[group]['hosts'].append(host)
            print(json.dumps(self.inventory, indent=4))
        elif nodes_request.status_code == 404:
            print('Server cannot reach the GNS3 nodes API.')


GNS3Inventory(gns3_server_address, gns3_server_port)


