import cv2 as cv
class HOG(object):
    # def __init__(self, window_height=128, window_width=64, cell_size=8, block_size=2, bins=9):
    #     self.window_height = window_height
    #     self.window_width = window_width
    #     self.cell_size = cell_size
    #     self.block_size = block_size
    #     self.bins = bins
    # def __call__(self, c_img):
    #     if len(c_img.shape) > 2:
    #         img = cv.cvtColor(c_img, cv.COLOR_BGR2GRAY)
    #     else:
    #         img = c_img
    #     h, w = img.shape
    #     if h != self.window_height or w != self.window_width:
    #         img = cv.resize(src=img, dsize=(self.window_width, self.window_height))
    #         h, w = img.shape
    #
    #     # gradient
    #     xkernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    #     ykernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    #     dx = cv.filter2D(img, cv.CV_32F, xkernel)
    #     dy = cv.filter2D(img, cv.CV_32F, ykernel)
    #     # ma and di
    #     magnitude = np.sqrt(np.square(dx) + np.square(dy))
    #     direction = np.arctan(np.divide(dy, dx + 0.00001))
    #     direction = np.degrees(direction)
    #     for a in range(direction.shape[0]):
    #         for b in range(direction.shape[1]):
    #             if direction[a, b] < 0:
    #                 direction[a, b] += 180
    #
    #     # 1x9 histogram for full cell
    #     num_cell_x = w // self.cell_size
    #     num_cell_y = h // self.cell_size
    #     full_his_cell = np.zeros((num_cell_y, num_cell_x, self.bins))
    #     for x in range(num_cell_x):
    #         for y in range(num_cell_y):
    #             ma_cur_cell = magnitude[y * self.cell_size:y * self.cell_size + self.cell_size,
    #                           x * self.cell_size:x * self.cell_size + self.cell_size]
    #             di_cur_cell = direction[y * self.cell_size:y * self.cell_size + self.cell_size,
    #                           x * self.cell_size:x * self.cell_size + self.cell_size]
    #             bins_hist = np.zeros(9)
    #             for cx in range(self.cell_size):
    #                 for cy in range(self.cell_size):
    #                     if di_cur_cell[cx, cy] >= 0 and di_cur_cell[cx, cy] < 20:
    #                         bins_hist[0] += ((20 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[1] += ((di_cur_cell[cx, cy] - 0) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 20 and di_cur_cell[cx, cy] < 40:
    #                         bins_hist[1] += ((40 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[2] += ((di_cur_cell[cx, cy] - 20) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 40 and di_cur_cell[cx, cy] < 60:
    #                         bins_hist[2] += ((60 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[3] += ((di_cur_cell[cx, cy] - 40) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 60 and di_cur_cell[cx, cy] < 80:
    #                         bins_hist[3] += ((80 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[4] += ((di_cur_cell[cx, cy] - 60) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 80 and di_cur_cell[cx, cy] < 100:
    #                         bins_hist[4] += ((100 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[5] += ((di_cur_cell[cx, cy] - 80) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 100 and di_cur_cell[cx, cy] < 120:
    #                         bins_hist[5] += ((120 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[6] += ((di_cur_cell[cx, cy] - 100) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 120 and di_cur_cell[cx, cy] < 140:
    #                         bins_hist[6] += ((140 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[7] += ((di_cur_cell[cx, cy] - 120) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 140 and di_cur_cell[cx, cy] < 160:
    #                         bins_hist[7] += ((160 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[8] += ((di_cur_cell[cx, cy] - 140) / 20) * ma_cur_cell[cx, cy]
    #                     if di_cur_cell[cx, cy] >= 160 and di_cur_cell[cx, cy] <= 180:
    #                         bins_hist[8] += ((180 - di_cur_cell[cx, cy]) / 20) * ma_cur_cell[cx, cy]
    #                         bins_hist[0] += ((di_cur_cell[cx, cy] - 160) / 20) * ma_cur_cell[cx, cy]
    #                     full_his_cell[cx, cy, :] = bins_hist
    #     # nomalazions block
    #     hog_vec = np.zeros((num_cell_y - 1, num_cell_x - 1, self.block_size * self.block_size * self.bins))
    #     for bx in range(num_cell_x - 1):
    #         for by in range(num_cell_y - 1):
    #             bx_front = bx
    #             bx_behin = bx + self.block_size
    #             by_front = by
    #             by_behin = by + self.block_size
    #             vec = full_his_cell[by_front:by_behin, bx_front:bx_behin, :].flatten(order="F")
    #             hog_vec[by, bx, :] = vec / np.sqrt(sum(x ** 2 for x in vec))
    #             if np.isnan(hog_vec[by, bx, :]).any():
    #                 hog_vec[by, bx, :] = vec
    #     return hog_vec.flatten(order="F")
    def __init__(self, window_height=128, window_width=64, cell_size=8, block_size=2, bins=9):
        self.window_height = window_height
        self.window_width = window_width
        self.cell_size = cell_size
        self.block_size = block_size
        self.bins = bins
    def __call__(self, cv_img):
        if len(cv_img.shape) > 2:
            img = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        else:
            img = cv_img
        h, w = img.shape
        if h != self.window_height or w != self.window_width:
            img = cv.resize(src=img, dsize=(self.window_width, self.window_height))
            h, w = img.shape
        # xkernel = np.array([[-1, 0, 1]])
        # ykernel = np.array([[-1], [0], [1]])
        # dx = cv.filter2D(img, cv.CV_32F, xkernel)
        # dy = cv.filter2D(img, cv.CV_32F, ykernel)
        #
        # # histogram
        # magnitude = np.sqrt(np.square(dx) + np.square(dy))
        # orientation = np.arctan(np.divide(dy, dx + 0.00001))
        # orientation = np.degrees(orientation)
        # orientation += 90
        #
        # num_cell_x = w // self.cell_size
        # num_cell_y = h // self.cell_size
        # hist_tensor = np.zeros([num_cell_y, num_cell_x, self.bins])
        # for cx in range(num_cell_x):
        #     for cy in range(num_cell_y):
        #         ori = orientation[cy * self.cell_size:cy * self.cell_size + self.cell_size,
        #               cx * self.cell_size:cx * self.cell_size + self.cell_size]
        #         mag = magnitude[cy * self.cell_size:cy * self.cell_size + self.cell_size,
        #               cx * self.cell_size:cx * self.cell_size + self.cell_size]
        #         hist, _ = np.histogram(ori, bins=self.bins, range=(0, 180), weights=mag)
        #         hist_tensor[cy, cx, :] = hist
        # # normalization
        # redundant_cell = self.block_size - 1
        # feature_tensor = np.zeros(
        #     [num_cell_y - redundant_cell, num_cell_x - redundant_cell, self.block_size * self.block_size * self.bins])
        # for bx in range(num_cell_x - redundant_cell):
        #     for by in range(num_cell_y - redundant_cell):
        #         by_from = by
        #         by_to = by + self.block_size
        #         bx_from = bx
        #         bx_to = bx + self.block_size
        #         v = hist_tensor[by_from:by_to, bx_from:bx_to, :].flatten()
        #         feature_tensor[by, bx, :] = v / np.sqrt(sum(x ** 2 for x in v))
        #         if np.isnan(feature_tensor[by, bx, :]).any():
        #             feature_tensor[by, bx, :] = v
        #
        # return feature_tensor.flatten()
        Cell_Size = (self.cell_size, self.cell_size)
        Block_Size = (self.block_size, self.block_size)
        Bins = self.bins
        WinSize = (w, h)
        BlockSize = (Block_Size[1] * Cell_Size[1], Block_Size[0] * Cell_Size[0])
        blockStride = (Cell_Size[1], Cell_Size[0])
        hog_fearture = cv.HOGDescriptor(_winSize=WinSize,
                                        _blockSize=BlockSize,
                                        _blockStride=blockStride,
                                        _cellSize=Cell_Size,
                                        _nbins=Bins)
        hog_vec = hog_fearture.compute(img)
        hog_vec = hog_vec.flatten()
        return hog_vec



