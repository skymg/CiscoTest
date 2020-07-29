import json
import requests
requests.packages.urllib3.disable_warnings()

# api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=Loopback8888"
api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=Loopback778"
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))