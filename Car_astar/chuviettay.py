import os
import numpy
import array as arr
import struct
class load_mnist():
    def __init__(self):
        self.train = 'train-images.idx3-ubyte'
        self.label_train = 'train-labels.idx1-ubyte'
        self.test = 't10k-images.idx3-ubyte'
        self.label_test = 't10k-labels.idx1-ubyte'

    def Load_train(self):
        image_train, labels_train = self.load(self.train, self.label_train)
        pass

    def load_test(self):
        image_test, labels_test = self.load(self.test, self.label_test)
        pass
    def process_image(self, image):
        pass
    def load(self, path, label):
        with open(path, 'rb') as file_path:
            magic, number, rows, cols = struct.unpack('>IIII', file_path.read(16))
            image_data = arr.array('B', file_path.read())
        with open(label, 'rb') as file_lable:
            magic, number = struct.unpack('>II', file_path.read(8))
            labels = arr.array('B', file_lable)
        images = []
        for i in range(number):
            images.append([0] * rows * cols)
        for i in range(number):
            images[i, :] = image_data[i * rows * cols: (i + 1) * rows * cols]
        return images, labels
    def display(self, image):









