import requests

ak = ''
sk=''
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak+'&'+'client_secret='+sk
response = requests.get(host)
if response:
    with open('acctess_token.txt', 'w+') as f:
      f.write(response.json()['access_token'])