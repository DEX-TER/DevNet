from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint

from router_info import router #The router information are inside the router_info.py file

netconf_filter = open("netconf-filter.xml").read() #we open the xml filer code which is in the netconf-filter file

# we connect to the router and apply the filter while using get

with manager.connect(host=router["host"],port=router["port"],username=router["username"],password=router["password"],hostkey_verify=False) as m:
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running config')

# The next line we convert the xml response inside the data into a dictionnary
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

#pprint(interface_python)

config = interface_python["interfaces"]["interface"]

op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"IP: {config['ipv4']['address']['ip']}")
print(f"Netmask: {config['ipv4']['address']['netmask']}")
print(f"Packets In: {op_state['statistics']['in-unicast-pkts']}")