
import base64
import requests

# EDIT THIS ↓ 
lockfile_path = "C:/Program Files (x86)/League Of Legend/32775/LeagueClient/lockfile"

with open(lockfile_path,'r') as f:
    lockfile_data = f.read()
    lockfile_data = lockfile_data.split(":")
    
    host = "127.0.0.1"
    port = lockfile_data[2]
    connection_method = lockfile_data[4]
    autho = 'Basic ' + base64.b64encode(('riot:' + lockfile_data[3]).encode(encoding = 'utf-8')).decode('utf-8')
    
    url_prefix = connection_method + '://' + host + ':' + port
    headers    = {'Accept' : 'application/json', 'Authorization' : autho}

    resp = requests.post(url= url_prefix+"/lol-challenges/v1/update-player-preferences/", headers=headers, json={"challengeIds": []},verify = False)