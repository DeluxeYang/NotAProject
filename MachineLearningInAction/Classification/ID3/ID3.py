from math import log
import operator
import Tree_Plotter


def cal_shannon_ent(data_set):  # 计算香农熵
    num_entries = len(data_set)
    label_count = {}
    for feature in data_set:
        _label = feature[-1]
        if _label not in label_count:
            label_count[_label] = 0
        label_count[_label] += 1
    shannon_ent = 0
    for k, v in label_count.items():
        prob = float(v) / num_entries
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def split_data_set(data_set, axis, value):
    return_data_set = []
    for feature in data_set:
        if feature[axis] == value:
            reduced_feature = feature[:axis]
            reduced_feature.extend(feature[axis+1:])
            return_data_set.append(reduced_feature)
    return return_data_set


def choose_best_feature_to_split(data_set):
    num_features = len(data_set[0]) - 1  # 特征数，最后一列是标签
    base_entropy = cal_shannon_ent(data_set)  # 原数据熵
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):  # 遍历每个特征
        unique_values = set([example[i] for example in data_set])  # 特征的值
        new_entropy = 0.0
        for value in unique_values:  # 遍历每个值
            sub_data_set = split_data_set(data_set, i, value)  # 根据值划分数据集
            prob = len(sub_data_set) / float(len(data_set))  # 权
            new_entropy += prob * cal_shannon_ent(sub_data_set)  # 计算划分的香农熵
        info_gain = base_entropy - new_entropy  # 信息增益：划分的熵 - 原基本熵
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


def create_data_set():
    data_set = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


def majority_count(class_list):  # 返回大多数
    class_count = {}
    for vote in class_list:
        if vote not in class_count:
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):  # 递归创建属
    class_list = [x[-1] for x in data_set]
    if class_list.count(class_list[0]) == len(class_list):  #
        return class_list[0]
    if len(class_list[0]) == 1:
        return majority_count(class_list)
    best_feature = choose_best_feature_to_split(data_set)
    best_feature_label = labels[best_feature]
    my_tree = {best_feature_label: {}}
    del labels[best_feature]
    feature_values = [x[best_feature] for x in data_set]
    unique_values = set(feature_values)
    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feature_label][value] = create_tree(split_data_set(data_set, best_feature, value), sub_labels)
    return my_tree


def classify(input_tree, feature_labels, test_vec):
    first_str = list(input_tree.keys())[0]
    second_dict = input_tree[first_str]
    feature_index = feature_labels.index(first_str)
    key = test_vec[feature_index]
    value_of_feature = second_dict[key]
    if isinstance(value_of_feature, dict):
        class_label = classify(value_of_feature, feature_labels, test_vec)
    else:
        class_label = value_of_feature
    return class_label


def store_tree(input_tree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(input_tree, fw)
    fw.close()


def grab_tree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


def lenses():
    with open("lenses.txt") as f:
        _lenses = [x.strip().split('\t') for x in f.readlines()]
        lenses_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
        lenses_tree = create_tree(_lenses, lenses_labels)
        Tree_Plotter.createPlot(lenses_tree)


if __name__ == '__main__':
    # _tree = create_tree(*create_data_set())
    # print(classify(_tree, ['no surfacing', 'flippers'], [1, 0]))
    lenses()
