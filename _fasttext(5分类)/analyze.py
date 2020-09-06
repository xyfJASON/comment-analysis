import fasttext

import seg_sentence as seg

def train(train_file_name, valid_file_name):
	"""
	用训练集进行训练，返回训练后的 model
	用验证集进行自动调参
	"""
	# return fasttext.train_supervised(input = train_file_name, \
		# lr = 0.1, epoch = 25, wordNgrams = 2, bucket = 200000, dim = 50, loss = 'hs')
	return fasttext.train_supervised(input = train_file_name, \
		autotuneValidationFile = valid_file_name, \
		autotuneDuration = 1200, \
		autotuneModelSize = "100M")

def predictComment(model, wordcnt, limit, comment):
	"""
	用分类器 model 预测 comment 的标签
	"""
	res = []
	for word in seg.segSentence(comment):
		if wordcnt.get(word) == None:
			continue
		if wordcnt[word] > limit:
			res.append(word)
	return model.predict(" ".join(res))[0][0][9:]