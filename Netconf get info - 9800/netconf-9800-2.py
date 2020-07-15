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

#Mac Address Variable / Static for the demo but could be called from CSV/ JSON or something else
MACAddress = '70:69:5a:74:8b:5c'

# Render Jinja Template
Ethernetmac_template = Template(open('EthernetMacfilter.xml').read())
Ethernetmac_rendered = Ethernetmac_template.render(
        MAC_ADDRESS= MACAddress, 
)

# Execute the netconf get
result = m.get(Ethernetmac_rendered)
print(result)