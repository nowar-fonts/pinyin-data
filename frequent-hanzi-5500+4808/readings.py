rawdata = { k: [] for k in range(0x4E00, 0xA000) }

for line in open("Unihan_Readings.txt"):
	if line[0] in ('#', '\n'):
		continue
	cp, ktype, data = line.rstrip().split('\t')
	if ktype in ("kXHC1983", "kTGHZ2013"):
		cp = int(cp[2:], base = 16)
		if cp in rawdata:
			rawdata[cp].append(data)

result = {}

from charlist import charlist
for cp, v in rawdata.items():
	ch = chr(cp)
	if ch in charlist:
		readings = set(reading.split(':')[1] for data in v for reading in data.split())
		result[ch] = readings.pop() if len(readings) == 1 else list(sorted(readings))

import pprint
pprint.pprint(result)
