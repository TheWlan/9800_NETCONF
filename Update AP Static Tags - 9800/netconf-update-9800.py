'''------------------------------------------------------------------
    Filename:   netconf-update-9800.py
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
