import random
import csv
import norm_csvdata as norm

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")

def cutDataSet_general(file_data, file_data_norm, test_set, split):
	norm.normalization(file_data, file_data_norm, fieldnames_with_tag)
	res = []
	with open(file_data_norm, newline = "") as infile, \
	open(test_set, "w", newline = "") as outfile:
		reader = csv.DictReader(infile)
		writer = csv.DictWriter(outfile, fieldnames = fieldnames_with_tag)
		writer.writeheader()
		tot = 0
		for row in reader:
			tot += 1
			if tot <= split:
				writer.writerow(row)
			else:
				res.append(row)
	with open(file_data_norm, "w", newline = "") as outfile:
		writer = csv.DictWriter(outfile, fieldnames = fieldnames_with_tag)
		writer.writeheader()
		for row in res:
			writer.writerow(row)

def cutDataSet_stage(file_data_norm, train_set, valid_set, test_set, split1, split2, stage):
	"""
	cut the data set into train set, valid set and test set
	"""
	with open(file_data_norm, "r", newline = "") as infile, \
	open(train_set, "w", newline = "") as outfile1, \
	open(valid_set, "w", newline = "") as outfile2, \
	open(test_set, "w", newline = "") as outfile3:
		reader = csv.DictReader(infile)
		writer1 = csv.DictWriter(outfile1, fieldnames = fieldnames_with_tag)
		writer2 = csv.DictWriter(outfile2, fieldnames = fieldnames_with_tag)
		writer3 = csv.DictWriter(outfile3, fieldnames = fieldnames_with_tag)
		writer1.writeheader()
		writer2.writeheader()
		writer3.writeheader()
		tot = 0
		if stage == 1: # quality theme
			for row in reader:
				tmp = row
				if row["tag"] != "0":
					tmp["tag"] = "1"
				tot = tot + 1
				if tot <= split1:
					writer1.writerow(tmp)
				elif tot <= split2:
					writer2.writerow(tmp)
				else:
					writer3.writerow(tmp)
		elif stage == 2: # shuijun theme
			for row in reader:
				tmp = row
				if row["tag"] == "-1":
					tmp["tag"] = "0"
				else:
					tmp["tag"] = "1"
				tot = tot + 1
				if tot <= split1:
					writer1.writerow(tmp)
				elif tot <= split2:
					writer2.writerow(tmp)
				else:
					writer3.writerow(tmp)
		elif stage == 3: # emotion theme
			for row in reader:
				tmp = row
				if row["tag"] == "0" or row["tag"] == "-1":
					continue
				tot = tot + 1
				if tot <= split1:
					writer1.writerow(tmp)
				elif tot <= split2:
					writer2.writerow(tmp)
				else:
					writer3.writerow(tmp)
