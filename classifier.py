import csv
import jieba
import pickle
import fasttext

models = {}
# models["NaiveBayes"] = ("models/model_NaiveBayes.pickle", 0.5400)
models["MNB"] = ("models/model_MNB.pickle", 0.7099)
models["BNB"] = ("models/model_BNB.pickle", 0.7045)
models["LR"] = ("models/model_LR.pickle", 0.7199)
models["SGD"] = ("models/model_SGD.pickle", 0.7153)
models["SVC"] = ("models/model_SVC.pickle", 0.6645)
models["LinearSVC"] = ("models/model_LinearSVC.pickle", 0.6745)
models["NuSVC"] = ("models/model_NuSVC.pickle", 0.6886)
models["FastText"] = ("models/model_FastText.bin", 0.7226)

def get_stopwords_list():
	""" 获取停用词表，返回包含停用词的列表 """
	stopwords = [line.strip() for line in open("my_stopwords.txt")]
	stopwords.append("hellip")
	stopwords.append(" ")
	stopwords.append("\n")
	return stopwords

def classify(comment):
	stopwords_list = get_stopwords_list()
	wordlist = [i for i in jieba.lcut(comment) if i.strip() and i not in stopwords_list]
	res = {}
	for key, val in models.items():
		if key == "FastText":
			model = fasttext.load_model(val[0])
			res[key] = model.predict(" ".join(wordlist))[0][0][9:]
			res[key] = str(res[key])
		else:
			with open(val[0], "rb") as infile:
				model = pickle.load(infile)
				worddict = dict([word, True] for word in wordlist)
				res[key] = model.classify(worddict)
				res[key] = str(res[key])
	cnt = {}
	cnt["-1"] = cnt["0"] = cnt["1"] = cnt["2"] = cnt["3"] = 0
	for key, val in models.items():
		cnt[res[key]] += val[1]
	return sorted(cnt.items(), key = lambda x:x[1], reverse = True)[0][0]

# with open("jdComment_TestSet.csv", newline = "") as infile:
# 	reader = csv.DictReader(infile)
# 	tot = 0
# 	bingo = 0
# 	for row in reader:
# 		tot += 1
# 		if tot % 100 == 0:
# 			print(tot)
# 		bingo += (classify(row["content"]) == str(row["tag"]))
# 	print(bingo, tot, bingo / tot)