import cv2 as cv
import numpy as np
from sklearn import svm
from PIL import Image
import joblib
import operator
class PersonDetector(object):
    def __init__(self, input_img, feature_extractor, model, nms, image_pyramid, window_step=16, window_height=128, window_width=64,  prob_threshold=0.9):
        self.input_img = input_img
        self.feature_extractor = feature_extractor
        self.model = model
        self.nms = nms
        self.image_pyramid = image_pyramid
        self.window_step = window_step
        self.window_height = window_height
        self.window_width = window_width
        self.prob_threshold = prob_threshold
        self.person_model = joblib.load(self.model)
    def read_pillow(self, img_path, isGray=True):
        pill = Image.open(img_path).convert("RGB")
        img = np.array(pill)
        img = img[:, :, ::-1].copy()
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return img
    def fit_model(self, img_hog_process):
        pred = self.person_model.predict(np.array([img_hog_process]))  # dự đoán ảnh
        pred_percent = self.person_model.predict_proba(np.array([img_hog_process]))  # đưa ra tỉ lệ dự đoán
        proc = pred_percent[0]
        laybel, value_percent = max(enumerate(proc), key=operator.itemgetter(1))
        isPerson = laybel == 1
        return isPerson, value_percent
    def __call__(self):
        img = self.read_pillow(self.input_img, isGray=True)
        h = img.shape[0]
        w = img.shape[1]
        img_dir = cv.imread(self.input_img)
        box = []
        for idex, new_height in enumerate(self.image_pyramid):
            new_width = int(new_height/h*w)
            if self.window_height > new_height or self.window_width > new_width:
                continue
            new_pyramid = cv.resize(img, dsize=(new_width, new_height))
            range_y = new_height - self.window_height
            range_x = new_width - self.window_width
            x = 0
            y = 0
            while y <= range_y:
                while x <= range_x:
                    print("run")
                    path = new_pyramid[y:y+self.window_height, x:x+self.window_width]
                    hog_pyramid = self.feature_extractor(path)
                    isPerson, value_percent = self.fit_model(hog_pyramid)
                    if isPerson and value_percent > self.prob_threshold:
                        x1 = int(x/new_width*w)
                        y1 = int(y/new_height*h)
                        x2 = int((x+self.window_width)/new_width*w)
                        y2 = int((y+self.window_height)/new_height*h)
                        box.append([x1, y1, x2, y2])
                        print("boxx")
                    x += self.window_step
                x = 0
                y += self.window_step
        boxes = self.nms(np.array(box))
        # boxes = np.array(box)
        for x in boxes:
            cv.rectangle(img_dir, (x[0], x[1]), (x[2], x[3]), (0, 255, 0), 2)

        cv.imwrite("out.jpg", img_dir)

        











