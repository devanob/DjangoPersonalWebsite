import urllib.request
import json
from datetime import datetime
namegit = "devanob"

import urllib.request
from urllib.request import Request, urlopen

url_request = Request("https://api.github.com/users/devanob/repos", 
                      headers = {"User-Agent": "Mozilla/5.0"})
contents = urlopen(url_request).read()

currentUserRepos= [] # // intially empty 
jsonContentRepos =  json.loads(contents)
for reposInfo in jsonContentRepos: 
	oodict = {key: value
		    for key, value in reposInfo.items()
		    if key in ['id', 'html_url', 'created_at', 'updated_at', 'name']
		  }
	currentUserRepos.append(oodict)
for repos in currentUserRepos:
	repos["created_at"] = datetime.strptime(repos["created_at"], "%Y-%m-%dT%H:%M:%SZ")
	repos["updated_at"] = datetime.strptime(repos["updated_at"], "%Y-%m-%dT%H:%M:%SZ")

print(currentUserRepos)
