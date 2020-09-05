import csv
import norm_csvdata as norm

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")

def cutDataSet(file_data, file_data_norm, train_set, valid_set, test_set, split1, split2):
	norm.normalization(file_data, file_data_norm, fieldnames_with_tag)

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
		for row in reader:
			if row["tag"] == "0":
				continue
			if row["tag"] == "-1":
				continue
			tot = tot + 1
			if tot <= split1:
				writer1.writerow(row)
			elif tot <= split2:
				writer2.writerow(row)
			else:
				writer3.writerow(row)
