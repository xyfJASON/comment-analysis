import jieba

def get_stopwords_list():
	""" 获取停用词表，返回包含停用词的列表 """
	stopwords = [line.strip() for line in open("stopwords/my_stopwords.txt")]
	stopwords.append("hellip")
	stopwords.append(" ")
	stopwords.append("\n")
	return stopwords

def segSentence(sentence):
	"""
	对一个句子进行分词，并去除停用词
	返回由分出的词组成的列表
	"""
	stopwords_list = get_stopwords_list()
	return [i for i in jieba.lcut(sentence) if i.strip() and i not in stopwords_list]