import pyeapi

node = pyeapi.connect_to('veos01')

show_version = node.enable('show version')
print(show_version[0]['result']['version'])