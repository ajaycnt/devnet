import requests

#Use self signed certs
requests.packages.urllib3.disable_warnings()

#Credentials
USER = 'developer'
PASS = 'C1sco12345'

#URL to reach the router
url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

#Set header to send
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'}

payload = '\
{\
        "ietf-interfaces:interface": {\
        "name": "Loopback69",\
        "description": "Added with RESTCONF by AS",\
        "type": "iana-if-type:softwareLoopback",\
        "enabled": true,\
        "ietf-ip:ipv4": {\
            "address": [\
                {\
                    "ip": "69.69.69.69",\
                    "netmask": "255.255.255.255"\
                }\
            ]\
        }\
    }\
}'

print(payload)
response = requests.request('POST', url, auth=(USER, PASS),
                        headers=headers, data = payload, verify=False)

#Print Results    
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)
    