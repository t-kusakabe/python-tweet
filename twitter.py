from requests_oauthlib import OAuth1Session
import json

token = open('token.json', 'r')
to_json = json.load(token)

CK = to_json['CK']
CS = to_json['CS']
AT = to_json['AT']
AS = to_json['AS']

url = 'https://api.twitter.com/1.1/statuses/update.json'

params = { 'status': 'docker with python' }

twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

if req.status_code == 200:
    print ('ok')
else:
    print ('Error: %d' % req.status_code)
