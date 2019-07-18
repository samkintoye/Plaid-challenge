#!/usr/bin/python
import requests
headers = {
    'Content-type': 'application/json',
}
data = '{"client_id":"5d2df3989085b90018e6694b", "secret":"b511404243e8d623ff4da095f8d2bf", "count":200,"offset":0  }'
response = requests.post('https://sandbox.plaid.com/institutions/get', headers=headers, data=data)
response_txt=response.text
count = response_txt.count("identity")
print("The total number of institutions that support Plaid's identity product is" , count)




       
        





