import requests
import json

## part 1 ASA


asaurl = "https://192.168.10.100/api/objects/networkobjects"

asapayload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"ASA_Demo_NObj_1190\"\r\n}"
asaheaders = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

asaresponse = requests.request("POST", asaurl, data=asapayload, verify=False, headers=asaheaders)




## part 2 NXOS
nxurl='http://192.168.10.60/ins'
nxswitchuser='admin'
nxswitchpassword='Passw0rd1'

nxheaders={'content-type':'application/json'}
nxpayload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vlan 600 ;name Construction ;vlan 700 ;name Analysis",
    "output_format": "json"
  }
}
nxresponse = requests.post(nxurl,data=json.dumps(nxpayload), headers=nxheaders,auth=(nxswitchuser,nxswitchpassword)).json()


## part 3 IOS XE

iosurl = "http://192.168.10.80/restconf/api/config/native/ip/route"

iospayload = "{\r\n    \"ned:route\": {\r\n        \"ip-route-interface-forwarding-list\": [\r\n            {\r\n                \"prefix\": \"216.48.1.0\",\r\n                \"mask\": \"255.255.255.0\",\r\n                \"fwd-list\": [\r\n                    {\r\n                        \"fwd\": \"10.1.1.1\"\r\n                    }\r\n                ]\r\n            }\r\n        ]\r\n    }\r\n}"
iosheaders = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

iosresponse = requests.request("PATCH", iosurl, data=iospayload, headers=iosheaders)


#Response codes
print('ASA response: %s' % (asaresponse.text))
print('Nexus response: %s' % (nxresponse))
print('IOS XE response: %s' % (iosresponse.text))
