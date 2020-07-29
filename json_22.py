import json
ss = ' {"ietf-ip:ipv4": {}, "ietf-ip:ipv6": {}, "name": "GigabitEthernet1", "enabled": true, "type": "iana-if-type:ethernetCsmacd", "description": "VBox"}'
ss2 = '{"Name":"李念", "Stature":"163cm","Birthday":"1985年5月30日","Birthplace":"湖北省荆门市京山县"}'

ss3 = '{"ietf-interfaces:interfaces": {"interface": [{"ietf-ip:ipv4": {}, "enabled": true, "ietf-ip:ipv6": {}, "description": "VBox", "type": "iana-if-type:ethernetCsmacd", "name": "GigabitEthernet1"}]}}'

# print(type(ss))
json_string = json.loads(ss)
json_string3 = json.loads(ss3)
print(type(json_string3))
print(json_string3['ietf-interfaces:interfaces']['interface'][0]['enabled'])
# print(json_string["name"])
# print(type(json_string))