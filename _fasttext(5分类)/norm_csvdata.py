import csv

def normalization(input_file_name, output_file_name, fieldnames):
	"""
	input_file_name 是一个 csv 文件，以 fieldnames 为其栏位名字
	output_file_name 也是以 fieldnames 为栏位名字的 csv 文件

	功能：去除不符合格式的内容
	"""

	res = []
	with open(input_file_name, newline = "") as infile, \
	open(output_file_name, "w", newline = "") as outfile:
		reader = csv.DictReader(infile)
		writer = csv.DictWriter(outfile, fieldnames = fieldnames, extrasaction = "ignore")
		writer.writeheader()
		for row in reader:
			if row['_id'][:8] != 'ObjectId':
				continue
			ok = True
			for fieldname in fieldnames:
				if row.get(fieldname) == None or row.get(fieldname) == "":
					ok = False
					break
			if ok == False:
				continue
			if row.get("tag") != None:
				if not(row["tag"] == "-1" or row["tag"] == "0" or \
					row["tag"] == "1" or row["tag"] == "2" or row["tag"] == "3"):
					continue
			writer.writerow(row)