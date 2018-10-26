import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\r\ncookie=\"1540573065/362b4a8e-3b4c-4961-a03e-2988a76ea0fb\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Linux\">\r\n    <lsServer\r\n    name=\"Linux\"\r\n    dn=\"org-root/ls-Linux\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth0\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"ether-eth0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"finance\"\r\n            \r\n            rn=\"if-finance\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth1\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"ether-eth1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"finance\"\r\n            \r\n            rn=\"if-finance\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc0\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"fc-fc0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc1\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"fc-fc1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <lsbootDef\r\n        \r\n        rn=\"boot-policy\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <lsbootStorage\r\n            order=\"1\"\r\n            \r\n            rn=\"storage\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n                <lsbootLocalStorage\r\n                \r\n                rn=\"local-storage\"\r\n                \r\n                \r\n                sacl=\"addchild,del,mod\">\r\n                    <lsbootDefaultLocalImage\r\n                    order=\"1\"\r\n                    \r\n                    rn=\"local-any\"\r\n                    \r\n                    \r\n                    sacl=\"addchild,del,mod\">\r\n                    </lsbootDefaultLocalImage>\r\n                </lsbootLocalStorage>\r\n            </lsbootStorage>\r\n        </lsbootDef>\r\n        <vnicFcNode\r\n        addr=\"pool-derived\"\r\n        identPoolName=\"\"\r\n        \r\n        rn=\"fc-node\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFcNode>\r\n    </lsServer>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>\r\n"
headers = {
    'Content-Type': "application/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

payload = "<configConfMos\r\ncookie=\"1540573065/362b4a8e-3b4c-4961-a03e-2988a76ea0fb\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Exchange\">\r\n    <lsServer\r\n    name=\"Exchange\"\r\n    dn=\"org-root/ls-Exchange\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth0\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"ether-eth0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"human-resource\"\r\n            \r\n            rn=\"if-human-resource\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth1\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"ether-eth1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"human-resource\"\r\n            \r\n            rn=\"if-human-resource\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc0\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"fc-fc0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc1\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"fc-fc1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <lsbootDef\r\n        \r\n        rn=\"boot-policy\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <lsbootStorage\r\n            order=\"1\"\r\n            \r\n            rn=\"storage\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n                <lsbootLocalStorage\r\n                \r\n                rn=\"local-storage\"\r\n                \r\n                \r\n                sacl=\"addchild,del,mod\">\r\n                    <lsbootDefaultLocalImage\r\n                    order=\"1\"\r\n                    \r\n                    rn=\"local-any\"\r\n                    \r\n                    \r\n                    sacl=\"addchild,del,mod\">\r\n                    </lsbootDefaultLocalImage>\r\n                </lsbootLocalStorage>\r\n            </lsbootStorage>\r\n        </lsbootDef>\r\n        <vnicFcNode\r\n        addr=\"pool-derived\"\r\n        identPoolName=\"\"\r\n        \r\n        rn=\"fc-node\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFcNode>\r\n    </lsServer>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>\r\n"

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

