import json
import pprint

codes = {}
out = ""
with open('source.txt', 'r') as f:
	out = f.readlines()


for lineno, line in enumerate(out):
    parts = line.replace('\n','').split(';')
    if len(parts) != 2:
            print("Error parsing line " + str(lineno) + ": "),
            print(line)
    else:
            codes[parts[1]] = parts[0]

a = json.dumps(codes, sort_keys=True, indent=4)
with open('barcodes.json', 'w') as f:
	f.write(a+'\n')
