import sys
import json
import base64
import time
import json

import requests

ak = ''
sk=''
service_main_url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/depparser'

def get_token(ak, sk):
  host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak+'&'+'client_secret='+sk
  response = requests.get(host)
  return response.json()['access_token']


def make_request(url, sentence):
  data=json.dumps({"text": sentence, "mode": 0}).encode('GBK')
  response = requests.post(url, headers={"Content-Type": "application/json"}, data=data)
  return response.json()


if __name__=='__main__':
  token = get_token(ak, sk)
  url = service_main_url + '?charset=UTF-8&access_token=' + token
  result = make_request(url, "今天天气怎么样")
  print(result)
