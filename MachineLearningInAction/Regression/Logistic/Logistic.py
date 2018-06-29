import numpy


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


if __name__ == "__main__":
    data, label = load_data_set()
    weight = grad_ascent(data, label)
    plot_best_fit(weight.getA())
