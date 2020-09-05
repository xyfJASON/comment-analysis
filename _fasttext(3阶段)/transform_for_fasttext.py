import csv
import random

import seg_sentence as seg

def trans_for_fasttext(input_file_name, output_file_name, fieldname, tagname):
	"""
	input_file_name 是一个 csv 文件，含有 fieldname 的栏位
	output_file_name 是一个文本文件，存储分词后的结果
	功能：将 input_file_name 中 fieldname 一栏提取出来与 tagname 中的 tag 配对，形成可用于 fasttext 的集合
	"""

	with open(input_file_name, newline = "") as infile, \
	open(output_file_name, "w", newline = "") as outfile:
		reader = csv.DictReader(infile)
		for row in reader:
			row_res = "__label__" + row[tagname] + " " + row[fieldname]
			outfile.write(row_res)
			outfile.write('\n')

def segSentence(file_name):
	res = []
	with open(file_name, "r") as infile:
		for row in infile:
			i = 9
			while row[i] != ' ':
				i += 1
			segList = seg.segSentence(row[i+1:])
			if len(segList) == 0:
				continue
			res.append(row[:i])
			for k in segList:
				res[-1] += " " + k
			res[-1] += '\n'
	with open(file_name, "w") as outfile:
		for row in res:
			outfile.write(row)

def reduce(limit, *file_names):
	wordcnt = {}
	for file_name in file_names:
		with open(file_name, "r") as infile:
			for row in infile:
				i = 9
				while row[i] != ' ':
					i += 1
				for word in row[i+1:].split():
					if word not in wordcnt.keys():
						wordcnt[word] = 0
					wordcnt[word] += 1
	for file_name in file_names:
		with open(file_name, "r") as infile:
			res = []
			for row in infile:
				i = 9
				while row[i] != ' ':
					i += 1
				res.append(row[:i])
				wordList = []
				for word in row[i+1:].split():
					if wordcnt[word] > limit:
						wordList.append(word)
				if len(wordList) == 0:
					res.pop()
					continue
				for word in wordList:
					res[-1] += " " + word
				res[-1] += '\n'
		with open(file_name, "w") as outfile:
			for row in res:
				outfile.write(row)
	return wordcnt

def overSampling(file_name, *tags):
	mx = 0
	tmp = {}
	res = []
	for k in tags:
		tmp.setdefault(k, [])
	with open(file_name, "r") as infile:
		for row in infile:
			res.append(row)
			i = 9
			thisTag = ""
			while row[i] != ' ':
				thisTag += row[i]
				i = i + 1
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
	with open(file_name, "w") as outfile:
		for row in res:
			outfile.write(row)