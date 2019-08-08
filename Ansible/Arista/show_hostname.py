# start by importing the library
import pyeapi

# create a node object by specifying the node to work with
node = pyeapi.connect_to('veos02')

# send one or more commands to the node
node.enable('show hostname')
[{'command': 'show hostname',
  'encoding': 'json',
  'result': {u'hostname': u'veos01',
             u'fqdn': u'veos01.arista.com'}}]

# Request a specific revision of a command that has been updated
node.enable({'cmd': 'show cvx', 'revision': 2})
[{'command': {'cmd': 'show cvx', 'revision': 2},
  'encoding': 'json',
  'result': {u'clusterMode': False,
             u'controllerUUID': u'',
             u'enabled': False,
             u'heartbeatInterval': 20.0,
             u'heartbeatTimeout': 60.0}}]

# use the config method to send configuration commands
node.config('hostname veos01')
[{}]

# multiple commands can be sent by using a list
# (works for both enable or config)
node.config(['interface Ethernet1', 'description foo'])
[{}, {}]

# return the running or startup configuration from the
# node (output omitted for brevity)
node.running_config

node.startup_config
