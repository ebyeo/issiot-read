import time
from random import randrange
import base64
import requests

url = 'http://52.163.89.207/api/authorize/access_token'
layoutsurl = 'http://52.163.89.207/api/layout?layout=&embed=regions,playlists'
displayurl = 'http://52.163.89.207/api/display'
changedisplayurl = 'http://13.84.54.83/api/displaygroup/2/action/changeLayout'
overlaydisplayurl = 'http://13.84.54.83/api/displaygroup/2/action/overlayLayout'
changebgurl = 'http://52.163.89.207/api/layout/9'
consumer_key = 'wQuB9wwHSbSQaSVGKuAJIECYVbSjJAbW1YgKfdnV'
consumer_secret = '1z4BoP81BchiYrl670Me81KlCFySnFlEJQhXL5oTTGmprAaRRXdcU9Wdqq3pZhq9lJzB44ai1uwoBQjqc2H2sOWmd1GFJAUIJZtxtIqIsTPDIPsK5M1ql2pPfN3JKixwyhlwttWFqTKFhb2FGF8E2nKREDcq0FYN67lRojhwAY69hEbwzSDOHDXUTIFdm5ebYRqZ2Csf01hZLBy3Tc1D3wcnF64f23ZTGW7uCxMM2pxL8tZp1xoYtGQWt90smR'
token = ''

bearer_token_credentials = base64.urlsafe_b64encode(
    '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')).decode('ascii')
headers = {
    'Authorization': 'Basic {}'.format(bearer_token_credentials),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
}
data = 'grant_type=client_credentials'
response = requests.post(url, headers=headers, data=data)
response_data = response.json()
print(response_data)
if response_data['token_type'] == 'Bearer':
    bearer_token = response_data['access_token']
    headers = {
        'Authorization': 'Bearer {}'.format(bearer_token),
        'Accept-Encoding': 'gzip',
    }
    response = requests.get(displayurl, headers=headers)
    response_data = response.json()
    print(response_data)

    color = randrange(25, 30)
    data = {
       "name": "SMRT Demo",
       "backgroundColor": "#FFFFFF",
       "backgroundzIndex": "3",
       "backgroundImageId": "25"
    }
    response = requests.put(changebgurl, data=data, headers=headers)
    print(response, response.status_code, response.reason)

    time.sleep(10)

    data = {
       "name": "SMRT Demo",
       "backgroundColor": "#FFFFFF",
       "backgroundzIndex": "3",
       "backgroundImageId": "67"
    }
    response = requests.put(changebgurl, data=data, headers=headers)
else:
    raise RuntimeError('unexpected token type: {}'.format(response_data['token_type']))

