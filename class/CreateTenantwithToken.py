import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)

#print type(json_response['imdata'][0]['aaaLogin']['attributes']['token'])
#print len(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

tokenfromlogin = json_response['imdata'][0]['aaaLogin']['attributes']['token']
print (tokenfromlogin)

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY28='}
cookie = {"APIC-Cookie":tokenfromlogin}
response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)
