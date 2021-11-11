import cv2 as cv
import numpy as np
from PIL import Image
import os
import random
from sklearn import svm
import joblib

train_post_lst = "INRIAPerson/INRIAPerson/train_64x128_H96/pos.lst"
train_post_dir = "INRIAPerson/INRIAPerson/96X160H96/Train"
train_neg_lst = "INRIAPerson/INRIAPerson/train_64x128_H96/neg.lst"
train_neg_dir = "INRIAPerson/INRIAPerson/Train"
train_neg_num_per_image = 10
train_neg_range = (0.4, 1.0)

# hog
def hog(gray_img, cell_size=8, block_size=2, bins=9):
    img = gray_img
    Cell_Size = (cell_size, cell_size)
    Block_Size = (block_size, block_size)
    Bins = bins
    h, w = img.shape
    WinSize = (w, h)
    BlockSize = (Block_Size[1]*Cell_Size[1], Block_Size[0]*Cell_Size[0])
    blockStride = (Cell_Size[1], Cell_Size[0])
    hog_fearture = cv.HOGDescriptor(_winSize=WinSize,
                                    _blockSize=BlockSize,
                                    _blockStride=blockStride,
                                    _cellSize=Cell_Size,
                                    _nbins=Bins)
    hog_vec = hog_fearture.compute(gray_img)
    hog_vec = hog_vec.flatten()
    #hog 1
    # img = gray_img
    # h, w = img.shape
    # #gradient
    # xkernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # ykernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    # dx = cv.filter2D(img, cv.CV_32F, xkernel)
    # dy = cv.filter2D(img, cv.CV_32F, ykernel)
    # # ma and di
    # magnitude = np.sqrt(np.square(dx) + np.square(dy))
    # direction = np.arctan(np.divide(dy, dx + 0.00001))
    # direction = np.degrees(direction)
    # for a in range(direction.shape[0]):
    #     for b in range(direction.shape[1]):
    #         if direction[a, b] < 0:
    #             direction[a, b] += 180
    #
    # # 1x9 histogram for full cell
    # num_cell_x = w // cell_size
    # num_cell_y = h // cell_size
    # full_his_cell = np.zeros((num_cell_y, num_cell_x, bins))
    # for x in range(num_cell_x):
    #     for y in range(num_cell_y):
    #         ma_cur_cell = magnitude[y*cell_size:y*cell_size+cell_size, x*cell_size:x*cell_size+cell_size]
    #         di_cur_cell = direction[y*cell_size:y*cell_size+cell_size, x*cell_size:x*cell_size+cell_size]
    #         bins_hist = np.zeros(9)
    #         for cx in range(cell_size):
    #             for cy in range(cell_size):
    #                 if di_cur_cell[cx, cy] >= 0 and di_cur_cell[cx, cy] < 20:
    #                     bins_hist[0] += ((20 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[1] += ((di_cur_cell[cx, cy]-0) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 20 and di_cur_cell[cx, cy] < 40:
    #                     bins_hist[1] += ((40 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[2] += ((di_cur_cell[cx, cy]-20) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 40 and di_cur_cell[cx, cy] < 60:
    #                     bins_hist[2] += ((60 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[3] += ((di_cur_cell[cx, cy]-40) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 60 and di_cur_cell[cx, cy] < 80:
    #                     bins_hist[3] += ((80 - di_cur_cell[cx,cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[4] += ((di_cur_cell[cx, cy]-60) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 80 and di_cur_cell[cx, cy] < 100:
    #                     bins_hist[4] += ((100 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[5] += ((di_cur_cell[cx, cy]-80) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 100 and di_cur_cell[cx, cy] < 120:
    #                     bins_hist[5] += ((120 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[6] += ((di_cur_cell[cx, cy]-100) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 120 and di_cur_cell[cx, cy] < 140:
    #                     bins_hist[6] += ((140 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[7] += ((di_cur_cell[cx, cy]-120) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 140 and di_cur_cell[cx, cy] < 160:
    #                     bins_hist[7] += ((160 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[8] += ((di_cur_cell[cx, cy]-140) / 20) * ma_cur_cell[cx, cy]
    #                 if di_cur_cell[cx, cy] >= 160 and di_cur_cell[cx, cy] <= 180:
    #                     bins_hist[8] += ((180 - di_cur_cell[cx, cy])/20) * ma_cur_cell[cx, cy]
    #                     bins_hist[0] += ((di_cur_cell[cx, cy]-160) / 20) * ma_cur_cell[cx, cy]
    #                 full_his_cell[cx, cy, :] = bins_hist
    # # nomalazions block
    # hog_vec = np.zeros((num_cell_y - 1, num_cell_x - 1, block_size * block_size * bins))
    # for bx in range(num_cell_x - 1):
    #     for by in range(num_cell_y - 1):
    #         bx_front = bx
    #         bx_behin = bx + block_size
    #         by_front = by
    #         by_behin = by + block_size
    #         vec = full_his_cell[by_front:by_behin, bx_front:bx_behin, :].flatten(order="F")
    #         hog_vec[by, bx, :] = vec/np.sqrt(sum(x**2 for x in vec))
    #         if np.isnan(hog_vec[by, bx, :]).any():
    #             hog_vec[by, bx, :] = vec
    # return hog_vec.flatten(order="F")

    #hog2
    # img = gray_img
    # h, w = img.shape
    #
    # # gradient
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
    # num_cell_x = w // cell_size
    # num_cell_y = h // cell_size
    # hist_tensor = np.zeros([num_cell_y, num_cell_x, bins])
    # for cx in range(num_cell_x):
    #     for cy in range(num_cell_y):
    #         ori = orientation[cy * cell_size:cy * cell_size + cell_size, cx * cell_size:cx * cell_size + cell_size]
    #         mag = magnitude[cy * cell_size:cy * cell_size + cell_size, cx * cell_size:cx * cell_size + cell_size]
    #         hist, _ = np.histogram(ori, bins=bins, range=(0, 180), weights=mag)
    #         hist_tensor[cy, cx, :] = hist
    #
    # # normalization
    # redundant_cell = block_size - 1
    # feature_tensor = np.zeros(
    #     [num_cell_y - redundant_cell, num_cell_x - redundant_cell, block_size * block_size * bins])
    # for bx in range(num_cell_x - redundant_cell):
    #     for by in range(num_cell_y - redundant_cell):
    #         by_from = by
    #         by_to = by + block_size
    #         bx_from = bx
    #         bx_to = bx + block_size
    #         v = hist_tensor[by_from:by_to, bx_from:bx_to, :].flatten()
    #         feature_tensor[by, bx, :] = v / np.sqrt(sum(x ** 2 for x in v))
    #         if np.isnan(feature_tensor[by, bx, :]).any():
    #             feature_tensor[by, bx, :] = v
    #
    # return feature_tensor.flatten()
    return hog_vec

# read pillow

def read_pilow(img_path, is_gray=True):
    img_pli = Image.open(img_path).convert("RGB")
    img = np.array(img_pli)
    img = img[:, :, ::-1].copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img


def train(train_post_lst, train_post_dir, train_neg_lst, train_neg_dir, train_neg_num_per_image, train_neg_range):
    assert os.path.isfile(train_post_lst) and os.path.isfile(train_neg_lst)

    # file pos
    with open(train_post_lst) as f:
        file_post = f.readlines()
    positive_feature = []
    file_post = [os.path.join(train_post_dir, "/".join(flp.split("/")[1:])).strip() for flp in file_post]
    for idx, file in enumerate(file_post):
        imgpath = file
        if not os.path.isfile(imgpath):
            continue
        img = read_pilow(imgpath, is_gray=True)
        img = cv.resize(img, dsize=(64, 128))
        igp = hog(img)
        positive_feature.append(igp)
        print('[pos][%d/%d] @ %s' % (idx + 1, len(file_post), imgpath))
    positive_feature = np.array(positive_feature)

    # file neg
    with open(train_neg_lst) as f:
        file_neg = f.readlines()
    negative_feature = []
    file_neg = [os.path.join(train_neg_dir, "/".join(fln.split("/")[1:])).strip() for fln in file_neg]
    for idx, file in enumerate(file_neg):
        img_path = file
        if not os.path.isfile(img_path):
            continue
        img = read_pilow(img_path, is_gray=True)
        imgh, imgw = img.shape
        min_size = min(imgh, imgw)
        img_neg_crop = []
        for index in range(train_neg_num_per_image):
            random_size = random.uniform(train_neg_range[0], train_neg_range[1])
            random_height = int(random_size * min_size)
            random_wight = int(random_height * random.uniform(0.3, 0.7))
            random_post_x = random.randint(0, imgw - random_wight)
            random_post_y = random.randint(0, imgh - random_height)
            npath = img[random_post_y:random_post_y + random_height, random_post_x:random_post_x + random_wight]
            img_neg_crop.append(npath)
        for pathn in img_neg_crop:
            pathn = cv.resize(pathn, (64, 128))
            ign = hog(pathn)
            negative_feature.append(ign)
            print('[neg][%d/%d] @ %s' % (idx + 1, len(file_neg), img_path))
    negative_feature = np.array(negative_feature)

    # svm
    x = np.concatenate((negative_feature, positive_feature), axis=0)
    y = np.array([0]*negative_feature.shape[0] + [1]*positive_feature.shape[0])
    model = svm.SVC(C=0.01, kernel="rbf", probability=True)
    model = model.fit(x, y)
    print("end train")

    return model

# main
def main():
    svm_model = train(train_post_lst,
                      train_post_dir,
                      train_neg_lst,
                      train_neg_dir,
                      train_neg_num_per_image,
                      train_neg_range)
    out_model = "person_detection.joblib"
    joblib.dump(svm_model, out_model)


# run main
if __name__ == "__main__":
    main()








