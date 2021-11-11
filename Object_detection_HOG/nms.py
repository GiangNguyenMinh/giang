import numpy as np
class NMS (object):
    def __init__(self, overlap_threshold=0.4):
        self.overlap_threshold = overlap_threshold
    def __call__(self, box):
        return self.non_max_suppress(box, self.overlap_threshold)
    def non_max_suppress(self, box, over_threshold):
        if len(box) == 0:
            return []
        #if box.dtype.kind("i"):
        box = box.astype('float')
        pick = []
        x1 = box[:, 0]
        y1 = box[:, 1]
        x2 = box[:, 2]
        y2 = box[:, 3]
        area = (x2 - x1 + 1)*(y2 - y1 + 1)
        idxs = np.argsort(y2)
        while len(idxs) > 0:
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)
            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])
            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)
            overlap = (w * h) / area[idxs[:last]]
            idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > over_threshold)[0])))
        return box[pick].astype("int")

