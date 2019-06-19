# README

This playbook allows you to automatically post notifications to one or more rooms within Webex Teams.

To start, add room IDs and an authorization token to the "keys.yaml" file. For testing, you may obtain a developer token at https://developer.webex.com/docs/api/v1/rooms/list-rooms

[![Token](https://github.com/scimaksim/network_programmability/blob/master/Ansible/Cisco_Webex/personal_access_token.png)](https://github.com/scimaksim/network_programmability/blob/master/Ansible/Cisco_Webex/personal_access_token.png)

To run the playbook from the command line, install Ansible and run

```sh
$ ansible-playbook webex_teams.yaml
```

[![Post](https://github.com/scimaksim/network_programmability/blob/master/Ansible/Cisco_Webex/notification_posted.png)](https://github.com/scimaksim/network_programmability/blob/master/Ansible/Cisco_Webex/notification_posted.png)