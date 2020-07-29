import xmltodict;
import json;

#定义函数
def pythonXmlToJson():
    with  open('save.xml', 'r') as f:
        xmlStr = f.read()

    convertedDict = xmltodict.parse(xmlStr);
    jsonStr = json.dumps(convertedDict, indent=1);
    print (jsonStr)
#执行函数
if __name__=="__main__":
    pythonXmlToJson();