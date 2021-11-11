import cv2 as cv
import numpy as np
img ="1.jpg"
gray = cv.imread(img, cv.COLOR_BGR2GRAY)
gray = cv.resize(gray, dsize=(64, 128))

cell_size = (8, 8)  # h x w in pixels
block_size = (2, 2)  # h x w in cells
nbins = 9

winSize = (64, 128)

blockSize = (block_size[1] * cell_size[1], block_size[0] * cell_size[0])

blockStride = (cell_size[1], cell_size[0])
print('Kích thước bức ảnh crop theo winSize (pixel): ', winSize)
print('Kích thước của 1 block (pixel): ', blockSize)
print('Kích thước của block stride (pixel): ', blockStride)


hog = cv.HOGDescriptor(_winSize=winSize,
                        _blockSize=blockSize,
                        _blockStride=blockStride,
                        _cellSize=cell_size,
                        _nbins=nbins)

n_cells = (16, 8)
print('Kích thước lưới ô vuông (ô vuông): ', n_cells)

hog_feats = hog.compute(gray)


print('Kích thước hog feature (h, w, block_size_h, block_size_w, nbins): ', hog_feats.flatten())
