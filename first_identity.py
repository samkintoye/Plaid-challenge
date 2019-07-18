#!/usr/bin/python
import requests
headers = {
    'Content-type': 'application/json',
}
data = '{"query":"first", "products":["identity"], "public_key":"3d22185375faf9e074b43c76dd0827" }'
response = requests.post('https://sandbox.plaid.com/institutions/search', headers=headers, data=data)
response_txt=response.text
print(response_txt)
count = response_txt.count("institution_id")
print("The total number of institutions that has the word 'first' in the name and support Plaid's identity product is" , count)




