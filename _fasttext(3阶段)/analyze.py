import fasttext
import csv

import seg_sentence as seg

def train(train_file_name, valid_file_name):
	"""
	用训练集进行训练，返回训练后的 model
	用验证集进行自动调参
	"""
	return fasttext.train_supervised(input = train_file_name, \
		lr = 0.1, epoch = 25, wordNgrams = 2, bucket = 200000, dim = 50, loss = 'hs')
	# return fasttext.train_supervised(input = train_file_name, \
	# 	autotuneValidationFile = valid_file_name, \
	# 	autotuneDuration = 300)

def predictComment(model, comment):
	"""
	用分类器 model 预测 comment 的标签
	"""
	com = seg.segSentence(comment)
	predict_tag1 = model[1].predict(" ".join(com))
	if predict_tag1[0][0][9:] == "0":
		return "0"
	predict_tag2 = model[2].predict(" ".join(com))
	if predict_tag2[0][0][9:] == "0":
		return "-1"
	predict_tag3 = model[3].predict(" ".join(com))
	return predict_tag3[0][0][9:]