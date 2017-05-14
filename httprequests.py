import requests;
import json;


r = requests.get('https://api.github.com/user', auth=('usrname', 'pass'))
print(r.json());

jsonString = r.json();
data = json.loads(jsonString);
