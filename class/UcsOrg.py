import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\r\ncookie=\"1540572435/10582da0-e81f-4440-ae95-d1459892201f\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/org-PythonMaster\">\r\n    <orgOrg\r\n    name=\"PythonMaster\"\r\n    dn=\"org-root/org-PythonMaster\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </orgOrg>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "application/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
