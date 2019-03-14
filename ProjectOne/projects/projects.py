import urllib.request
import json
from datetime import datetime
namegit = "devanob"

contents = urllib.request.urlopen("https://api.github.com/users/devanob/repos").read()
jsonContent =  json.loads(contents)[0]
oodict = {key: value
            for key, value in jsonContent.items()
            if key in ['id', 'html_url', 'created_at', 'updated_at', 'name']
            }
temp_date = datetime.strptime("2007-03-04T21:08:12Z", "%Y-%m-%dT%H:%M:%SZ")
print(temp_date)
