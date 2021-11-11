import os
import struct
import array as ar
import numpy
train = os.path.join('MNIST', 'train-images-idx3-ubyte', 'train-images.idx3-ubyte')
with open(train, 'rb') as file:
    t = struct.unpack(">IIII", file.read(16))
    image_data = ar.array("B", file.read())
print(t)


rows = 3
coles = 4
item = []
item.append([0]* rows * coles + [1]* rows)
print(item)