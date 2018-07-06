import numpy
# from time import sleep


def load_data_set(file_name):  # 读取文件数据
    data_mat = []
    label_mat = []
    with open(file_name) as f:
        for line in f.readlines():
            line_arr = line.strip().split('\t')
            data_mat.append([float(line_arr[0]), float(line_arr[1])])
            label_mat.append(float(line_arr[2]))
    return data_mat, label_mat


def select_random_j(i, m):  # 在0-m范围内随机生成j，j不能和i相同
    j = i  # we want to select any J not equal to i
    while j == i:
        j = int(numpy.random.uniform(0, m))
    return j


def clip_alpha(aj, high, low):  # aj超过上限或者下限，则等于上限或者下限
    if aj > high:
        aj = high
    if aj < low:
        aj = low
    return aj


def smo_simple(data_mat_in, class_labels, c, toler, loop):
    data_matrix = numpy.mat(data_mat_in)
    label_matrix = numpy.mat(class_labels).transpose()
    b = 0
    m, n = numpy.shape(data_matrix)
    alphas = numpy.mat(numpy.zeros((m, 1)))
    _iter = 0
    while _iter < loop:  # 外循环
        alpha_pairs_changed = 0
        for i in range(m):
            prediction_i = numpy.float(numpy.multiply(alphas, label_matrix).T * (data_matrix * data_matrix[i, :].T)) + b
            error_i = prediction_i - numpy.float(label_matrix[i])
            if (label_matrix[i] * error_i and alphas[i] < c) or (label_matrix[i]*error_i > toler and alphas[i] > 0):
                j = select_random_j(i, m)
                prediction_j = numpy.float(numpy.multiply(alphas, label_matrix).T *
                                           (data_matrix * data_matrix[j, :].T)) + b
                error_j = prediction_j - numpy.float(label_matrix[j])
                alpha_i_old = alphas[i].copy()
                alpha_j_old = alphas[j].copy()
                if label_matrix[i] != label_matrix[j]:
                    low = max(0, alphas[j] - alphas[i])
                    high = min(c, c + alphas[j] - alphas[i])
                else:
                    low = max(0, alphas[j] + alphas[i] - c)
                    high = min(c, alphas[j] + alphas[i])
                if low == high:
                    print("low = high")
                    continue
                eta = 2.0 * data_matrix[i, :] * data_matrix[j, :].T -\
                    data_matrix[i, :] * data_matrix[i, :].T - data_matrix[j, :] * data_matrix[j, :].T
                if eta >= 0:
                    print("eta > 0")
                    continue
                alphas[j] -= label_matrix[j] * (error_i - error_j) / eta
                alphas[j] = clip_alpha(alphas[j], high, low)
                if numpy.abs(alphas[j] - alpha_j_old) < 0.00001:
                    print("j not moving enough")
                    continue
                alphas[i] += label_matrix[j] * label_matrix[i] * (alpha_j_old - alphas[j])
                b1 = b - error_i - label_matrix[i] * (alphas[i] - alpha_i_old) * \
                     data_matrix[i, :] * data_matrix[i, :].T -\
                     label_matrix[j] * (alphas[j] * alpha_j_old) \
                     * data_matrix[i, :] * data_matrix[j, :].T
                b2 = b - error_j - label_matrix[i] * (alphas[i] - alpha_i_old) * \
                     data_matrix[i, :] * data_matrix[j, :].T -\
                     label_matrix[j] * (alphas[j] * alpha_j_old) \
                     * data_matrix[j, :] * data_matrix[j, :].T
                if 0 < alphas[i] < c:
                    b = b1
                elif 0 < alphas[j] < c:
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alpha_pairs_changed += 1
                print("iter: %d i:%d, pairs changed %d" % (_iter, i, alpha_pairs_changed))
        if alpha_pairs_changed == 0:
            _iter += 1
        else:
            _iter = 0
        print("iteration number: %d" % _iter)
    return b, alphas


if __name__ == "__main__":
    data_arr, label_arr = load_data_set("testSet.txt")
    _b, _alphas = smo_simple(data_arr, label_arr, 0.6, 0.001, 40)
    print(_b)
    print(_alphas[_alphas > 0])
