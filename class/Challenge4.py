import requests
import json

# Get the cookie from the login
url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n\t\t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)

# print type(json_response['imdata'][0]['aaaLogin']['attributes']['token'])
# print len(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

tokenfromlogin = json_response['imdata'][0]['aaaLogin']['attributes']['token']
# print (tokenfromlogin)

# Create the tenant acme
url = "http://192.168.10.1/api/node/mo/uni/tn-acme.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme\",\r\n\t\t\t\"name\": \"acme\",\r\n\t\t\t\"rn\": \"tn-acme\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY28='}
cookie = {"APIC-Cookie":tokenfromlogin}
response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)

# create the application profile accounting

# output from APIC API Inspector
# url: https://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting.json
# payload: {"fvAp":{"attributes":{"dn":"uni/tn-acme/ap-Accounting","name":"Accounting","rn":"ap-Accounting","status":"created"},"children":[]}}

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting.json"
payload = "{\"fvAp\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting\",\"name\":\"Accounting\",\"rn\":\"ap-Accounting\",\"status\":\"created\"},\"children\":[]}}"
cookie = {"APIC-Cookie":tokenfromlogin}
response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)

# create the EPG Bills

# output from APIC API Inspector
# url: https://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json
# payload: {"fvAEPg":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Bills","name":"Bills","rn":"epg-Bills","status":"created"},"children":[{"fvCrtrn":{"attributes":{"dn":"uni/tn-acme/ap-Accounting/epg-Bills/crtrn","name":"default","rn":"crtrn","status":"created,modified"},"children":[]}}]}}

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json"
payload = "{\r\n\t\"fvAEPg\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Bills\",\r\n\t\t\t\"name\": \"Bills\",\r\n\t\t\t\"rn\": \"epg-Bills\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": [{\r\n\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Bills/crtrn\",\r\n\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\"rn\": \"crtrn\",\r\n\t\t\t\t\t\"status\": \"created,modified\"\r\n\t\t\t\t},\r\n\t\t\t\t\"children\": []\r\n\t\t\t}\r\n\t\t}]\r\n\t}\r\n}"
cookie = {"APIC-Cookie":tokenfromlogin}
response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)

# create the EPG Payroll

# no output from APIC API Inspector
# modified previous

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Payroll.json"
payload = "{\r\n\t\"fvAEPg\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Payroll\",\r\n\t\t\t\"name\": \"Payroll\",\r\n\t\t\t\"rn\": \"epg-Payroll\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": [{\r\n\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting/epg-Payroll/crtrn\",\r\n\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\"rn\": \"crtrn\",\r\n\t\t\t\t\t\"status\": \"created,modified\"\r\n\t\t\t\t},\r\n\t\t\t\t\"children\": []\r\n\t\t\t}\r\n\t\t}]\r\n\t}\r\n}"
cookie = {"APIC-Cookie":tokenfromlogin}
response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)
