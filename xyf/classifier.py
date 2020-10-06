import json
import jieba
import pickle
import fasttext
from math import floor

models = {}
# models["NaiveBayes"] = ("models/model_NaiveBayes.pickle", 0.5400, None)
models["MNB"] = ["models/model_MNB.pickle", 0.7099, None]
models["BNB"] = ["models/model_BNB.pickle", 0.7045, None]
models["LR"] = ["models/model_LR.pickle", 0.7199, None]
models["SGD"] = ["models/model_SGD.pickle", 0.7153, None]
models["SVC"] = ["models/model_SVC.pickle", 0.6645, None]
models["LinearSVC"] = ["models/model_LinearSVC.pickle", 0.6745, None]
models["NuSVC"] = ["models/model_NuSVC.pickle", 0.6886, None]
models["FastText"] = ["models/model_FastText.bin", 0.7226, None]

def get_stopwords_list():
	""" 获取停用词表，返回包含停用词的列表 """
	stopwords = [line.strip() for line in open("my_stopwords.txt", "r", encoding = "utf-8")]
	stopwords.append(" ")
	return stopwords

def classify(comment):
	wordlist = [i for i in jieba.lcut(comment) if i.strip() and i not in stopwords_list]
	cnt = {'-1':0, '0':0, '1':0, '2':0, '3':0}
	for key, val in models.items():
		if key == "FastText":
			res = val[2].predict(" ".join(wordlist))[0][0][9:]
			cnt[str(res)] += val[1]
		else:
			with open(val[0], "rb") as infile:
				worddict = dict([word, True] for word in wordlist)
				res = val[2].classify(worddict)
				cnt[str(res)] += val[1]
	return sorted(cnt.items(), key = lambda x:x[1], reverse = True)[0][0]


stopwords_list = get_stopwords_list()
for key, val in models.items():
	if key == "FastText":
		val[2] = fasttext.load_model(val[0])
	else:
		with open(val[0], "rb") as infile:
			val[2] = pickle.load(infile)

cnt = {'-1':0, '0':0, '1':0, '2':0, '3':0}
with open("mycomment.json", "r", encoding = "utf-8") as infile:
	for line in infile:
		data = json.loads(line)
		print(data["content"])
		cnt[classify(data["content"])] += 1

with open("Result.txt", "w", encoding = "utf-8") as outfile:
	sum = cnt['-1']+cnt['0']+cnt['3']+cnt['2']+cnt['1']
	per = {'-1':0, '0':0, '1':0, '2':0, '3':0}
	per['-1'] = floor(cnt['-1'] / sum * 100);
	per['0'] = floor(cnt['0'] / sum * 100);
	per['1'] = floor(cnt['1'] / sum * 100);
	per['2'] = floor(cnt['2'] / sum * 100);
	per['3'] = 100 - per['-1'] - per['0'] - per['1'] - per['2'];
	score = floor((cnt['3']*3+cnt['2']*2+cnt['1'])/(cnt['3']+cnt['2']+cnt['1'])*33+1)
	outfile.write(str(per['3']) + " " + str(per['2'])\
	 + " " + str(per['1']) + " " + str(per['-1']) + " " + str(per['0']) + " ")
	outfile.write(str(score) + " ")
	if score >= 83:
		outfile.write("1 ")
	elif score >= 67:
		outfile.write("2 ")
	else:
		outfile.write("3 ")
