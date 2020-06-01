import requests
import json

cookies = {}
data = '{"username":"admin","password":"eve","html5":"-1"}'
headers = {"Content-type": "application/json"}

with requests.Session() as s:
    login = s.post("http://192.168.43.131/api/auth/login", cookies=cookies, data=data)
    login.json()
    print(login.json())
    print(s.cookies)

    user = s.get("http://192.168.43.131/api/auth", headers=headers, cookies=cookies)
    user.json()
    print(user.json())

    status = s.get("http://192.168.43.131/api/status", headers=headers, cookies=cookies)
    status.json()
    print(status.json())

    list_nodes = s.get(
        "http://192.168.43.131/api/list/templates/", headers=headers, cookies=cookies
    )
    list_nodes.json()
    print(list_nodes.json())

    data_node = '{"type":"qemu","template":"vios","config":"Unconfigured","delay":0,"icon":"Router.png","image":"vios-adventerprisek9-m-15.5.3M","name":"Core Router 1","left":"35%","top":"25%","ram":"1024","console":"telnet","cpu":1,"ethernet":2,"uuid":"e967819b-626c-4e5c-afa6-ebb4476bc19e"}'
    add_node = s.post("http://192.168.43.131/api/labs/Autobot.unl/nodes",
        cookies=cookies,
        data=data_node,
        )
    add_node.json()
    print(add_node.json())
