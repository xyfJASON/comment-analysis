import transform_for_nltk as trans
import analyze as anal
import cut

import pickle
from nltk import classify

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")
fieldnames = ("_id", "user", "content", "creationTime", "referenceName")

data_set = "villa/jdComment_DataSet.csv"
train_set = "villa/jdComment_TrainSet.csv"
test_set = "villa/jdComment_TestSet.csv"

""" get train set for fasttext based on train_set and save it in train_file """
""" get test set for fasttext based on test_set and save it in test_file """
# cut.cutDataSet(data_set, train_set, test_set, 14000)
# train_nltk = trans.trans_for_nltk(train_set, "content", "tag")
# test_nltk = trans.trans_for_nltk(test_set, "content", "tag")
# with open("villa/train_nltk.pickle", "wb") as outfile:
# 	pickle.dump(train_nltk, outfile)
# with open("villa/test_nltk.pickle", "wb") as outfile:
# 	pickle.dump(test_nltk, outfile)
with open("villa/train_nltk.pickle", "rb") as infile:
	train_nltk = pickle.load(infile)
with open("villa/test_nltk.pickle", "rb") as infile:
	test_nltk = pickle.load(infile)

""" get and save the training model """
# model = anal.train_NaiveBayes(train_nltk) # Naive Bayes
# model = anal.train_MNB(train_nltk) # MultinomialNB
# model = anal.train_BNB(train_nltk) # BernoulliNB
# model = anal.train_LR(train_nltk) # Logistic Regression
# model = anal.train_SGD(train_nltk) # Stochastic Gradient Descent
# model = anal.train_SVC(train_nltk) # SVC
# model = anal.train_LinearSVC(train_nltk) # Linear SVC
# model = anal.train_NuSVC(train_nltk) # NuSVC
# print(classify.accuracy(model, test_nltk))
# model.show_most_informative_features(15)
# with open("villa/model_SGD.pickle", "wb") as outfile:
	# pickle.dump(model, outfile)

""" load models  """
with open("villa/model_BNB.pickle", "rb") as infile:
	model = pickle.load(infile)

# print(anal.predictComment(model, "没有达到期望值"))
# print(anal.predictComment(model, "很糟糕，到处都脱线了"))
# print(anal.predictComment(model, "糟糕"))
# print(anal.predictComment(model, "很差，不会再来了"))
# print(anal.predictComment(model, "穿的很难受"))
# print(anal.predictComment(model, "鞋子太大了"))
# print(anal.predictComment(model, "鞋底有点硬，不是很舒服"))
# print(anal.predictComment(model, "差评"))
# print(anal.predictComment(model, "太差了"))
# print(anal.predictComment(model, "很一般，不值得"))
# print(anal.predictComment(model, "非常不值得"))
# print(anal.predictComment(model, "不好"))