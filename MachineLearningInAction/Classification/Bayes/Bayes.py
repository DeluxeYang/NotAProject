import numpy


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


if __name__ == '__main__':
    ds, cv = load_data_set()
    vocabs = create_vocab_list(ds)
    print(set_of_words_to_vec(vocabs, ds[0]))
