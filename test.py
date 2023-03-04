
import urllib.request
import re

url = 'https://coderbyte.com/api/challenges/logs/web-logs-raw'

response = urllib.request.urlopen(url)
raw_logs = response.read().decode('utf-8')


pattern = re.compile(r' .*coderbyte heroku/router. *')


for line in raw_logs.split:
  if pattern.match(line):
   request_id line.split('request_id=')[1].split()[0]
   
 output = request_id
 
print(output)
