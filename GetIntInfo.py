import requests

#Allow self signed certs
requests.packages.urllib3.disable_warnings()

#Credentials
USER = 'developer'
PASS = 'C1sco12345'

#URL for GET request
url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

#Set yang+json as the data formats
headers = {'Content-Type': 'application/yang-data+json',
			'Accept': 'application/yang-data+json'}
#Run GET
response = requests.get(url, auth=(USER, PASS), 
                        headers=headers, verify=False)
			
#print results		
print('Status Code:' + str(response.status_code))	
print('Response Text:' + response.text)

#end of the script