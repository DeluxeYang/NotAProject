import numpy
import operator


def create_data_set():
    group = numpy.array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels


def classify_knn(test_data, training_data, training_labels, k):
    training_data_size = training_data.shape[0]
    diff_matrix = numpy.tile(test_data, (training_data_size, 1)) - training_data
    print(diff_matrix)
    sq_diff_matrix = diff_matrix ** 2
    sq_distances = sq_diff_matrix.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_index = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = training_labels[sorted_dist_index[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    group, labels = create_data_set()
    print(classify_knn([0, 0], group, labels, 2))
