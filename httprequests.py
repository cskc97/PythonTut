import requests;
import json;


r = requests.get('https://api.github.com/user', auth=('username', 'password'))
print(r.json());

jsonString = r.text;
data = json.loads(jsonString);
print data['public_repos'];
