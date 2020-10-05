import json
import jieba
import pickle
import fasttext

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
	stopwords = [line.strip() for line in open("my_stopwords.txt")]
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
		cnt[classify(data["content"])] += 1

with open("result.txt", "a", encoding = "utf-8") as outfile:
	outfile.write(str(cnt['-1']) + '\n')
	outfile.write(str(cnt['0']) + '\n')
	outfile.write(str(cnt['1']) + '\n')
	outfile.write(str(cnt['2']) + '\n')
	outfile.write(str(cnt['3']) + '\n')
	outfile.write(str((cnt['3']*3+cnt['2']*2+cnt['1'])/(cnt['3']+cnt['2']+cnt['1'])) + '\n')
