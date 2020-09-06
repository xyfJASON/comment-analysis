from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

import seg_sentence as seg

def train_NaiveBayes(training_set):
	return NaiveBayesClassifier.train(training_set)

def train_MNB(training_set):
	MNB_classifier = SklearnClassifier(MultinomialNB())
	return MNB_classifier.train(training_set)

def train_BNB(training_set):
	BNB_classifier = SklearnClassifier(BernoulliNB())
	return BNB_classifier.train(training_set)

def train_LR(training_set):
	LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
	return LogisticRegression_classifier.train(training_set)

def train_SGD(training_set):
	SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
	return SGDClassifier_classifier.train(training_set)

def train_SVC(training_set):
	SVC_classifier = SklearnClassifier(SVC())
	return SVC_classifier.train(training_set)

def train_LinearSVC(training_set):
	LinearSVC_classifier = SklearnClassifier(LinearSVC())
	return LinearSVC_classifier.train(training_set)

def train_NuSVC(training_set):
	NuSVC_classifier = SklearnClassifier(NuSVC())
	return NuSVC_classifier.train(training_set)

def predictComment(model, comment):
	"""
	用分类器 model 预测 comment 的标签
	"""
	wordlist = seg.segSentence(comment)
	worddict = dict([word, True] for word in wordlist)
	return model.classify(worddict)