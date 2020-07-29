from ncclient import manager
import xml.dom.minidom
import xmltodict,json
# create a variable object that represents the NETCONF session
m = manager.connect(
         host="192.168.56.101",
         port=830,
         username="cisco",
         password="cisco123!",
         hostkey_verify=False
         )

# define a NETCONF filter to get only the required data
# w/o this filter the NETCONF GET operation will try to
# return everything and will crash (aka. similar to 'debug all')
# the filter defines that we want to get only data defined
# in the ietf-interfaces model in the interfaces-state container
netconf_filter = """
<filter>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

# using the NETCONF get method, get data:
netconf_reply = m.get(filter = netconf_filter)
# print("=========")
# print(netconf_reply)
# print("-----------")
# converteJson = xmltodict.parse(netconf_reply,encoding='utf-8')
# json_str = json.dumps(converteJson)
xml_data = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
fo = open("save.xml", "w")
fo.write(xml_data)
fo.close()
print(xml_data)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
