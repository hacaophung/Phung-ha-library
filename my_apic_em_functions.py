import json
import requests
from tabulate import *

def get_ticket():
    
    requests.packages.urllib3.disable_warnings()
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }
    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    print("Ticket request status: ", resp.status_code)
    response_json = resp.json()
    print(response_json)
    serviceTicket = response_json["response"]["serviceTicket"]
    print("The service ticket number is: ", serviceTicket)
    return serviceTicket
def print_hosts():
    api_url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()

    headers = {
    "content-type": "application/json",
    "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    host_list = []
    i = 0

    for item in response_json["response"]:
        i+=1
        host = [
        i,
        item["hostType"],
        item["hostIp"]
        ]
        host_list.append( host )
        table_header = ["Number", "Type", "IP"]
        print( tabulate(host_list, table_header) )
        
