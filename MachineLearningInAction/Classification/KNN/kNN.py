import os
import numpy
import operator


def create_data_set():
    group = numpy.array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels


def classify_knn(test_data, training_data, training_labels, k):
    training_data_size = training_data.shape[0]
    diff_matrix = numpy.tile(test_data, (training_data_size, 1)) - training_data  # tile在列方向上重复param1共param2次
    sq_diff_matrix = diff_matrix ** 2
    sq_distances = sq_diff_matrix.sum(axis=1)
    distances = sq_distances ** 0.5  # 计算距离
    sorted_dist_index = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = training_labels[sorted_dist_index[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def file_to_matrix(filename):
    with open(filename) as file:
        lines_list = file.readlines()
        lines_count = len(lines_list)
        return_matrix = numpy.zeros((lines_count, 3))  # 3个特征，对应3列的全0矩阵
        label_list = []  # 标签
        i = 0
        for line in lines_list:
            line = line.strip().split("\t")
            return_matrix[i, :] = line[0:3]
            label_list.append(int(line[-1]))
            i += 1
        return return_matrix, label_list


def auto_norm(data_set):
    _min = data_set.min(0)  # 每一列的最小值
    _max = data_set.max(0)  # 每一列的最大值
    ranges = _max - _min
    m = data_set.shape[0]
    norm_data_set = data_set - numpy.tile(_min, (m, 1))  # tile将_min在行（纵）方向上重复m次，列方向（横）1次
    norm_data_set = norm_data_set / numpy.tile(ranges, (m, 1))
    return norm_data_set, ranges, _min


def dating_class_test():
    ho_ratio = 0.1
    dating_matrix, dating_label = file_to_matrix("datingTestSet2.txt")
    norm_matrix, ranges, _min = auto_norm(dating_matrix)
    m = norm_matrix.shape[0]
    num_test = int(m*ho_ratio)
    error_count = 0
    for i in range(num_test):
        classifier_result = classify_knn(norm_matrix[i, :], norm_matrix[num_test:m, :], dating_label[num_test:m], 3)
        # 参数1：测试数据1~num_test，参数23：训练数据num_test~m
        print("the classifier came back with: %d, the real answer is: %d" % (classifier_result, dating_label[i]))
        if classifier_result != dating_label[i]:
            error_count += 1
    print("the total error rate is: %f" % (error_count / float(num_test)))
    print(error_count, num_test)


def img_to_vector(filename):
    return_vec = numpy.zeros((1, 1024))
    with open(filename) as file:
        for i in range(32):
            line_str = file.readline()  # 文件中的每一行
            for j in range(32):  # 都存储在一行数组里
                return_vec[0, 32*i+j] = int(line_str[j])
    return return_vec


def handwriting_class_test():
    hw_labels = []
    training_file_list = os.listdir('trainingDigits')  # load the training set
    m = len(training_file_list)
    training_matrix = numpy.zeros((m, 1024))
    for i in range(m):
        file_name_str = training_file_list[i]
        file_name = file_name_str.split('.')[0]
        class_num_str = int(file_name.split('_')[0])
        hw_labels.append(class_num_str)
        training_matrix[i, :] = img_to_vector('trainingDigits/%s' % file_name_str)
    test_file_list = os.listdir('testDigits')   # iterate through the test set
    error_count = 0.0
    m_test = len(test_file_list)
    for i in range(m_test):
        file_name_str = test_file_list[i]
        file_name = file_name_str.split('.')[0]   # take off .txt
        class_num_str = int(file_name.split('_')[0])
        vector_under_test = img_to_vector('testDigits/%s' % file_name_str)
        classifier_result = classify_knn(vector_under_test, training_matrix, hw_labels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifier_result, class_num_str))
        if classifier_result != class_num_str:
            error_count += 1.0
    print("\n the total number of errors is: %d" % error_count)
    print("\n the total error rate is: %f" % (error_count/float(m_test)))


if __name__ == '__main__':
    handwriting_class_test()
    # group, labels = create_data_set()
    # print(classify_knn([1, 1], group, labels, 2))
    # dating_matrix, dating_label = file_to_matrix("datingTestSet2.txt")
    # import matplotlib
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(dating_matrix[:, 0], dating_matrix[:, 1], 15*numpy.array(dating_label), 15*numpy.array(dating_label))
    # plt.show()
    # # 创建 3D 图形对象
    # from mpl_toolkits.mplot3d import Axes3D
    # import matplotlib.pyplot as plt

    # fig = plt.figure()
    # ax = Axes3D(fig)
    #
    # # 绘制线型图
    # ax.scatter(dating_matrix[:, 0], dating_matrix[:, 1], dating_matrix[:, 2], 15*numpy.array(dating_label),
    #            15*numpy.array(dating_label), 15*numpy.array(dating_label))
    #
    # # 显示图
    # plt.show()
