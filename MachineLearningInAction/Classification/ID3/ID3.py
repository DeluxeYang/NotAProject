from math import log


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


if __name__ == '__main__':
    print(cal_shannon_ent(create_data_set()[0]))
