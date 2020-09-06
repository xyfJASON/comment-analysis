import csv
import random

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")

def cutDataSet(data_set, train_set, test_set, split):
	res1 = []
	res2 = []
	with open(data_set, "r", newline = "") as infile:
		reader = csv.DictReader(infile)
		tot = 0
		for row in reader:
			tot = tot + 1
			if tot <= split:
				res1.append(row)
			else:
				res2.append(row)
	res1 = overSampling(res1, "-1", "0", "1", "2", "3")
	res2 = overSampling(res2, "-1", "0", "1", "2", "3")
	with open(train_set, "w", newline = "") as outfile1, \
	open(test_set, "w", newline = "") as outfile2:
		writer1 = csv.DictWriter(outfile1, fieldnames = fieldnames_with_tag)
		writer2 = csv.DictWriter(outfile2, fieldnames = fieldnames_with_tag)
		writer1.writeheader()
		writer2.writeheader()
		for row in res1:
			writer1.writerow(row)
		for row in res2:
			writer2.writerow(row)

def overSampling(inlist, *tags):
	mx = 0
	tmp = {}
	res = []
	for k in tags:
		tmp.setdefault(k, [])
	for row in inlist:
		res.append(row)
		thisTag = row["tag"]
		tmp[thisTag].append(row)
		mx = max(mx, len(tmp[thisTag]))

	for k in tags:
		if len(tmp[k]) == mx:
			continue
		sz = len(tmp[k])
		tot = sz
		while tot < mx:
			res.append(tmp[k][random.randint(0, sz-1)])
			tot += 1
	random.shuffle(res)
	return res