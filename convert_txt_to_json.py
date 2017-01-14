import json
import pprint

codes = {}
out = ""
with open('source.txt', 'r') as f:
	out = f.readlines()

for line in out:
    if line.find(';') != -1:
        parts = line.replace('\n','').split(';')
        codes[parts[1]] = parts[0]

a = json.dumps(codes, sort_keys=True, indent=4)
with open('barcodes.json', 'w') as f:
	f.write(a+'\n')
