import norm_csvdata as norm
import transform_for_fasttext as trans
import analyze as anal
import cut

import fasttext

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")
fieldnames = ("_id", "user", "content", "creationTime", "referenceName")

data_set = "villa/jdComment_DataSet.csv"
data_set_norm = "villa/jdComment_DataSetNorm.csv"

train_set = "jdComment_TrainSet.csv"
train_file = "jdComment.train"

valid_set = "jdComment_ValidSet.csv"
valid_file = "jdComment.valid"

test_set = "jdComment_TestSet.csv"
test_file = "jdComment.test"

""" get train set for fasttext based on train_set and save it in train_file """
""" get valid set for fasttext based on valid_set and save it in valid_file """
""" get test set for fasttext based on test_set and save it in test_file """

# cut.cutDataSet_general(data_set, data_set_norm, "villa/" + test_set, 1000)
# trans.trans_for_fasttext("villa/" + test_set, "villa/" + test_file, "content", "tag")
# trans.overSampling("villa/" + test_file, "-1", "0", "1", "2", "3")

# for i in range(1, 4):
	# file_prefix = "villa/stage" + str(i) + "/"
	# cut.cutDataSet_stage(data_set_norm, \
	# 	file_prefix + train_set, file_prefix + valid_set, file_prefix + test_set, 10000, 13000, i)
	# trans.trans_for_fasttext(file_prefix + train_set, file_prefix + train_file, "content", "tag")
	# trans.trans_for_fasttext(file_prefix + valid_set, file_prefix + valid_file, "content", "tag")
	# trans.trans_for_fasttext(file_prefix + test_set, file_prefix + test_file, "content", "tag")
	# trans.segSentence(file_prefix + train_file)
	# trans.segSentence(file_prefix + valid_file)
	# trans.segSentence(file_prefix + test_file)
	# trans.reduce(3, file_prefix + train_file, file_prefix + valid_file, file_prefix + test_file)
	# if i <= 2:
	# 	trans.overSampling(file_prefix + train_file, "0", "1")
	# 	trans.overSampling(file_prefix + valid_file, "0", "1")
	# 	trans.overSampling(file_prefix + test_file, "0", "1")
	# else:
	# 	trans.overSampling(file_prefix + train_file, "1", "2", "3")
	# 	trans.overSampling(file_prefix + valid_file, "1", "2", "3")
	# 	trans.overSampling(file_prefix + test_file, "1", "2", "3")

""" get and save the training model """
model = [None for i in range(4)]
# for i in range(1, 4):
	# file_prefix = "villa/stage" + str(i) + "/"
	# model[i] = anal.train(file_prefix + train_file, file_prefix + valid_file)
	# model[i].save_model("villa/model_stage" + str(i) + "_jdComment.bin")

""" test the training model """
for i in range(1, 4):
	model[i] = fasttext.load_model("villa/model_stage" + str(i) + "_jdComment.bin")
	# print(model[i].test("villa/stage" + str(i) + "/" + test_file))

tot = 0
bingo = 0
with open("villa/" + test_file) as infile:
	for row in infile:
		i = 9
		tag = ""
		while row[i] != ' ':
			tag += row[i]
			i += 1
		res = anal.predictComment(model, row[i+1:-2])
		if res == tag:
			bingo += 1
		tot += 1
print(bingo / tot)

# norm.normalization(predict_set, predict_set_norm, fieldnames)
# anal.predictFile(model, predict_set_norm, predict_set_result, fieldnames_with_tag, "content")
# print(model.predict("没有达到期望值"))
# print(model.predict("很糟糕，到处都脱线了"))
# print(model.predict("糟糕"))
# print(model.predict("很差，不会再来了"))
# print(model.predict("穿的很难受"))
# print(model.predict("鞋子太大了"))
# print(model.predict("鞋底有点硬，不是很舒服"))
# print(model.predict("差评"))
# print(model.predict("太差了"))
# print(model.predict("很一般，不值得"))
# print(model.predict("非常不值得"))
# print(model.predict("不好"))