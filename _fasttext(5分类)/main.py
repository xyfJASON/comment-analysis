import norm_csvdata as norm
import transform_for_fasttext as trans
import analyze as anal
import cut

import fasttext

fieldnames_with_tag = ("_id", "user", "content", "creationTime", "referenceName", "tag")
fieldnames = ("_id", "user", "content", "creationTime", "referenceName")

data_set = "villa/jdComment_DataSet.csv"
data_set_norm = "villa/jdComment_DataSetNorm.csv"

train_set = "villa/jdComment_TrainSet.csv"
train_file = "villa/jdComment.train"

valid_set = "villa/jdComment_ValidSet.csv"
valid_file = "villa/jdComment.valid"

test_set = "villa/jdComment_TestSet.csv"
test_file = "villa/jdComment.test"

""" get train set for fasttext based on train_set and save it in train_file """
""" get valid set for fasttext based on valid_set and save it in valid_file """
""" get test set for fasttext based on test_set and save it in test_file """
cut.cutDataSet(data_set, data_set_norm, train_set, valid_set, test_set, 11000, 14000)
trans.trans_for_fasttext(train_set, train_file, "content", "tag")
trans.trans_for_fasttext(valid_set, valid_file, "content", "tag")
trans.trans_for_fasttext(test_set, test_file, "content", "tag")
trans.segSentence(train_file)
trans.segSentence(valid_file)
trans.segSentence(test_file)
wordcnt = trans.reduce(3, train_file, valid_file, test_file)
trans.overSampling(train_file, "-1", "0", "1", "2", "3")
trans.overSampling(valid_file, "-1", "0", "1", "2", "3")
trans.overSampling(test_file, "-1", "0", "1", "2", "3")

""" get and save the training model """
model = anal.train(train_file, valid_file)
model.save_model("villa/model_jdComment.bin")

""" test the training model """
# model = fasttext.load_model("villa/model_jdComment.bin")
print(model.test(test_file))

# print(anal.predictComment(model, wordcnt, 3, "没有达到期望值"))
# print(anal.predictComment(model, wordcnt, 3, "很糟糕，到处都脱线了"))
# print(anal.predictComment(model, wordcnt, 3, "糟糕"))
# print(anal.predictComment(model, wordcnt, 3, "很差，不会再来了"))
# print(anal.predictComment(model, wordcnt, 3, "穿的很难受"))
# print(anal.predictComment(model, wordcnt, 3, "鞋子太大了"))
# print(anal.predictComment(model, wordcnt, 3, "鞋底有点硬，不是很舒服"))
# print(anal.predictComment(model, wordcnt, 3, "差评"))
# print(anal.predictComment(model, wordcnt, 3, "太差了"))
# print(anal.predictComment(model, wordcnt, 3, "很一般，不值得"))
# print(anal.predictComment(model, wordcnt, 3, "非常不值得"))
# print(anal.predictComment(model, wordcnt, 3, "不好"))