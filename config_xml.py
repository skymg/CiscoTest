from ncclient import manager
import xml.dom.minidom

# 创建一个代表NETCONF会话的变量对象
m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

# 定义一个NETCONF过滤器以仅获取所需的数据
# 不使用此过滤器，NETCONF GET操作将尝试
# 返回所有内容并崩溃（又类似于“全部调试”）
# 过滤器定义我们只想获取定义的数据
# 接口状态容器中ietf-interfaces模型中的＃
netconf_filter = """
<filter>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

# 使用NETCONF的get方法，获取数据：
netconf_reply = m.get(filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

input("###### Press Enter to continue to Step 3 ######")
import xmltodict

# 使用xmldict模块解析NETCONF回复（以xml格式）
# 重新调整的对象是Python字典
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

# 遍历Python字典对象并打印有趣的数据
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
    print("====TEST======")
    print("Name: {} MAC: {} Input: {} Output {}".format(
        interface["name"],
        interface["phys-address"],
        interface["statistics"]["in-octets"],
        interface["statistics"]["out-octets"]
    )

    )
    print("====TEST======")