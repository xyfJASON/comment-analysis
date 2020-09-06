import csv
import random

import seg_sentence as seg

def trans_for_nltk(input_file_name, fieldname, tagname):
	"""
	input_file_name 是一个 csv 文件，含有 fieldname 的栏位
	功能：将 input_file_name 中 fieldname 一栏提取出来分词处理，然后
	     与 tagname 中的 tag 配对，形成可用于 nltk 的集合
	"""
	with open(input_file_name, newline = "") as infile:
		reader = csv.DictReader(infile)
		res = []
		for row in reader:
			wordlist = seg.segSentence(row[fieldname])
			worddict = dict([word, True] for word in wordlist)
			res.append((worddict, row[tagname]))
	return res

# def reduce(limit, *file_names):
# 	wordcnt = {}
# 	for file_name in file_names:
# 		with open(file_name, "r") as infile:
# 			for row in infile:
# 				i = 9
# 				while row[i] != ' ':
# 					i += 1
# 				for word in row[i+1:].split():
# 					if word not in wordcnt.keys():
# 						wordcnt[word] = 0
# 					wordcnt[word] += 1
# 	for file_name in file_names:
# 		with open(file_name, "r") as infile:
# 			res = []
# 			for row in infile:
# 				i = 9
# 				while row[i] != ' ':
# 					i += 1
# 				res.append(row[:i])
# 				wordList = []
# 				for word in row[i+1:].split():
# 					if wordcnt[word] > limit:
# 						wordList.append(word)
# 				if len(wordList) == 0:
# 					res.pop()
# 					continue
# 				for word in wordList:
# 					res[-1] += " " + word
# 				res[-1] += '\n'
# 		with open(file_name, "w") as outfile:
# 			for row in res:
# 				outfile.write(row)
# 	return wordcnt
