'''------------------------------------------------------------------
    Filename:   netconf-9800.py
    author:     Haydn Andrews 
    date:       13/07/2020  
    desc:       

    modification history:
    what    when            who     why
    v1.0    13/07/2020      HA      Initial version
-------------------------------------------------------------------'''

#Import Dependencies
from ncclient import manager
from jinja2 import Template

# NETCONF Connection Manager
m = manager.connect(host='10.0.0.10', port=830, username='admin',
                    password='P@ssword1', device_params={'name': 'csr'})

# Create a filter
interface_filter = '''
  <filter>
    <access-point-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-access-point-oper">
        <ap-name-mac-map>
            <eth-mac>70:69:5a:74:8b:5c</eth-mac>
        </ap-name-mac-map>
    </access-point-oper-data>
</filter>
'''

# Execute the netconf get 
result = m.get(interface_filter)
print(result)
