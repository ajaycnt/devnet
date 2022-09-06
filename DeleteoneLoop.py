import requests

#Use self signed certs
requests.packages.urllib3.disable_warnings()

#Credentials
USER = 'developer'
PASS = 'C1sco12345'

#Set yang+json as the data formats

payload = {}
headers = {
    'Accept': 'application/yang-data+json'
    }

intname = "Loopback69"
print('Deleting ' + intname)
url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface="+intname
response = requests.request("DELETE",url, auth=(USER, PASS), 
    headers=headers, data = payload, verify=False)
    
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)