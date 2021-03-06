import numpy
import math
import random


def load_data_set():
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return posting_list, class_vec


def create_vocab_list(data_set):  # 将data_set中的词提取出来，形成一个set, 所有的词
    vocab_set = set()  # create empty set
    for document in data_set:
        vocab_set = vocab_set | set(document)  # union of the two sets
    return list(vocab_set)


def set_of_words_to_vec(vocab_list, input_set):  # 查看在某一条记录中的词，在所有的词当中的出现情况
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return return_vec


def train_naive_bayes_0(train_matrix, train_category):
    num_train_docs = len(train_matrix)  # 训练文档总数
    num_words = len(train_matrix[0])  # 所有出现过的总词数
    p_abusive = sum(train_category)/float(num_train_docs)  # category里，侮辱性为1，非侮辱性为0，因此sum等于侮辱性总数
    p0_num = numpy.ones(num_words)  # 0非侮辱性统计
    p1_num = numpy.ones(num_words)  # 1侮辱性统计
    p0_denominator = 2.0  # 分母
    p1_denominator = 2.0  # 分母
    for i in range(num_train_docs):
        if train_category[i] == 1:  # 侮辱性
            p1_num += train_matrix[i]
            p1_denominator += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denominator += sum(train_matrix[i])
    p1_vec = numpy.log(p1_num / p1_denominator)  # 各个词是侮辱性的条件概率率
    p0_vec = numpy.log(p0_num / p0_denominator)
    return p0_vec, p1_vec, p_abusive


def classify_naive_bayes(vec_to_classify, p0_vec, p1_vec, p1_class):
    p1 = sum(vec_to_classify * p1_vec) + math.log(p1_class)
    p0 = sum(vec_to_classify * p0_vec) + math.log(1.0 - p1_class)
    return 1 if p1 > p0 else 0


def testing_naive_bayes():
    list_posts, list_classes = load_data_set()
    vocab_list = create_vocab_list(list_posts)
    train_mat = []
    for x in list_posts:
        train_mat.append(set_of_words_to_vec(vocab_list, x))
    p0_vec, p1_vec, p_ab = train_naive_bayes_0(numpy.array(train_mat), numpy.array(list_classes))
    test = ['love', 'my', 'dalmation']
    this_doc = numpy.array(set_of_words_to_vec(vocab_list, test))
    print(test, 'classified as: ', classify_naive_bayes(this_doc, p0_vec, p1_vec, p_ab))
    test = ['stupid', 'garbage']
    this_doc = numpy.array(set_of_words_to_vec(vocab_list, test))
    print(test, 'classified as: ', classify_naive_bayes(this_doc, p0_vec, p1_vec, p_ab))


def bag_of_words_to_vec_mn(vocab_list, input_set):
    res = [0]*len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            res[vocab_list.index(word)] += 1
    return res


def text_parse(big_string):  # input is big string, #output is word list
    import re
    list_of_tokens = re.split(r'\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]


def spam_test():
    doc_list = []
    class_list = []
    full_text = []
    for i in range(1, 26):
        word_list = text_parse(open('email/spam/%d.txt' % i, "r", errors='ignore').read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        word_list = text_parse(open('email/ham/%d.txt' % i, "r", errors='ignore').read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    vocab_list = create_vocab_list(doc_list)  # create vocabulary
    training_set = [i for i in range(50)]
    test_set = []  # create test set
    for i in range(10):  # 随机抽取10个作为测试样本，并从原list删除
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del (training_set[rand_index])
    train_mat = []
    train_classes = []
    for doc_index in training_set:  # train the classifier (get probs) trainNB0
        train_mat.append(bag_of_words_to_vec_mn(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
    p0_v, p1_v, p_spam = train_naive_bayes_0(numpy.array(train_mat), numpy.array(train_classes))
    error_count = 0
    for doc_index in test_set:  # classify the remaining items
        word_vector = bag_of_words_to_vec_mn(vocab_list, doc_list[doc_index])
        if classify_naive_bayes(numpy.array(word_vector), p0_v, p1_v, p_spam) != class_list[doc_index]:
            error_count += 1
            print("classification error", doc_list[doc_index])
    print('the error rate is: ', float(error_count) / len(test_set))


if __name__ == '__main__':
    # testing_naive_bayes()
    spam_test()
