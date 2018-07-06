import numpy
import random


def load_data_set():
    data_mat = []
    label_mat = []
    f = open("testSet.txt")
    for line in f.readlines():
        line_list = line.strip().split()
        data_mat.append([1.0, float(line_list[0]), float(line_list[1])])
        label_mat.append(int(line_list[2]))
    return data_mat, label_mat


def sigmoid(in_x):
    return 1.0 / (1 + numpy.exp(-in_x))


def grad_ascent(data_mat_in, class_labels):
    data_matrix = numpy.mat(data_mat_in)  # numpy矩阵
    label_matrix = numpy.mat(class_labels).transpose()  # numpy 矩阵转为列向量
    m, n = numpy.shape(data_matrix)
    alpha = 0.001
    max_loop = 500
    weights = numpy.ones((n, 1))
    for k in range(max_loop):
        h = sigmoid(data_matrix * weights)  # dm矩阵 * w权重列向量 = 列向量，再进行sigmoid运算
        error = label_matrix - h  # 真实类别与预测类别的差值
        weights = weights + alpha * data_matrix.transpose() * error  # transpose：转置
    return weights


def plot_best_fit(weights):
    import matplotlib.pyplot as plt
    data_mat, label_mat = load_data_set()
    data_list = numpy.array(data_mat)
    n = numpy.shape(data_list)[0]
    x_cord1 = []
    y_cord1 = []
    x_cord2 = []
    y_cord2 = []
    for i in range(n):
        if int(label_mat[i]) == 1:
            x_cord1.append(data_list[i, 1])
            y_cord1.append(data_list[i, 2])
        else:
            x_cord2.append(data_list[i, 1])
            y_cord2.append(data_list[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_cord1, y_cord1, s=30, c='red', marker='s')
    ax.scatter(x_cord2, y_cord2, s=30, c='green')
    x = numpy.arange(-3, 3, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def stochastic_grad_ascent0(data_matrix, class_labels):
    m, n = numpy.shape(data_matrix)
    alpha = 0.01
    weights = numpy.ones(n)  # initialize to all ones
    for i in range(m):
        h = sigmoid(sum(data_matrix[i] * weights))
        error = class_labels[i] - h
        weights = weights + alpha * error * numpy.array(data_matrix[i])
    return weights


def stochastic_grad_ascent1(data_matrix, class_labels, loop=150):
    m, n = numpy.shape(data_matrix)
    weights = numpy.ones(n)  # initialize to all ones
    for j in range(loop):
        data_index = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01  # alpha decreases with iteration, does not
            rand_index = int(random.uniform(0, len(data_index)))  # go to 0 because of the constant
            h = sigmoid(numpy.sum(data_matrix[rand_index] * weights))
            error = class_labels[rand_index] - h
            weights = weights + alpha * error * numpy.array(data_matrix[rand_index])
            del (data_index[rand_index])
    return weights


def classify_vector(in_x, weights):
    prob = sigmoid(sum(in_x * weights))
    return 1.0 if prob > 0.5 else 0.0


def colic_test():
    fr_train = open('horseColicTraining.txt')
    fr_test = open('horseColicTest.txt')
    training_set = []
    training_labels = []
    for line in fr_train.readlines():
        curr_line = line.strip().split('\t')
        _list = []
        for i in range(21):
            _list.append(float(curr_line[i]))
        training_set.append(_list)
        training_labels.append(float(curr_line[21]))
    train_weights = stochastic_grad_ascent1(numpy.array(training_set), training_labels, 1000)
    error_count = 0
    num_test_vec = 0.0
    for line in fr_test.readlines():
        num_test_vec += 1.0
        curr_line = line.strip().split('\t')
        _list = []
        for i in range(21):
            _list.append(float(curr_line[i]))
        if int(classify_vector(numpy.array(_list), train_weights)) != int(curr_line[21]):
            error_count += 1
    error_rate = (float(error_count) / num_test_vec)
    print("the error rate of this test is: %f" % error_rate)
    return error_rate


def multi_test():
    num_tests = 10
    error_sum = 0.0
    for k in range(num_tests):
        error_sum += colic_test()
    print("after %d iterations the average error rate is: %f" % (num_tests, error_sum / float(num_tests)))


if __name__ == "__main__":
    # data, label = load_data_set()
    # weight = stochastic_grad_ascent1(data, label)
    # plot_best_fit(weight)
    multi_test()
