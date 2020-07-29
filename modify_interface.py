# import json
# import requests
# requests.packages.urllib3.disable_warnings()
interface_name = "Loopback8888"
interfacetype = "iana-if-type:softwareLoopback"
interface_ip = "45.56.2.22"
interface_description = "bianjisfsfs"

# api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface"+interface_name
# headers = {"Accept": "application/yang-data+json",
#            "Content-type": "application/yang-data+json"
#            }
# basicauth = ("cisco", "cisco123!")
#
# yangConfig = {
#     "ietf-interfaces:interface": {
#         "name": interface_name,
#         "description": interface_description,
#         "type": interfacetype,
#         "enabled": True,
#         "ietf-ip:ipv4": {
#             "address": [
#                 {
#                     "ip": interface_ip,
#                     "netmask": "255.255.255.0"
#                 }
#             ]
#         },
#         "ietf-ip:ipv6": {}
#     }
# }
# resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
# if (resp.status_code >= 200 and resp.status_code <= 299):
#     print("STATUS OK: {}".format(resp.status_code))
# else:
#     print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface="+interface_name
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": interface_name,
        "description": interface_description,
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [                {
                    "ip": interface_ip,
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}


resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

