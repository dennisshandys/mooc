import requests
from requests_oauthlib import OAuth2

c_id = 'f816ce9193fbfddba268'
c_secret = '36aabeb2cf646e8f6c918f698f8e66a6f5f3c752'
c_type = 'WebApplicationClient'
token_customer = {'access_token': 'f8ce319fe388ed8342425a429c3d024661978493'}


auth = OAuth2(c_id, c_type, token=token_customer)

api_endpoint = "http://support.satelkom.com:1511/api/courses/v1/courses/"

r = requests.get(api_endpoint, auth=auth)
print (r.json())