# Playbooks for Cisco ACI
This is a set of playbooks for managing resources in Cisco ACI. Hank Preston authored the [original playbooks](https://github.com/hpreston/netdevops_demos).

The "hosts" file points to [Cisco's ACI sandbox](https://developer.cisco.com/site/sandbox/). 

To import these playbooks into Ansible Tower, let's create a new project.
1. Under "Projects", click the "+" icon to create a new project
2. Select "Git" as the SCM type and enter the URL of the GitHub repository 
(e.g. https://github.com/scimaksim/network_programmability.git)
3. Save and synchronize the new project to retrieve its playbooks from GitHub

Now, it's time to create a new inventory.

1. Under "Inventories", click the "+" icon to create a new inventory. Provide a unique title and click "Save".  
2. Within the new inventory, click on "Sources" and "+" to create a new inventory source.
4. Enter a unique name for the source. Under the "Source" dropdown, select "Sourced from a Project" and find the "hosts" file (e.g. Ansible/ACI/hosts). 
Optionally, you may select the "Update on Launch" checkbox to update the inventory each time you launch a job in Ansible Tower.
5. Save and synchronize the inventory source. You should now be able to see the ACI controller under "Hosts" within the inventory.  

Let's create a job template and run our first job.

1. Under "Templates", click the "+" icon and specify a custom name.
2. Select the inventory and the project you created earlier. 
3. Select one of the playbooks from the project (e.g. Ansible/ACI/create_tenants.yaml). CLick "Save".
4. Create a survey to prompt a user for initials. Under "Answer variable name", enter *prefix*. This corresponds to the {{ prefix }} variable in the playbooks.

