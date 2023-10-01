<<<<<<< HEAD
import requests
import json
import base64

url = 'http://127.0.0.1:5000/'
files = {'image': open('1.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.json())
=======
import requests
import json
import base64

url = 'http://127.0.0.1:5000/'
files = {'image': open('1.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.json())
>>>>>>> 48cb49affcd9dfa81c636b50a239f7893ad417c1
