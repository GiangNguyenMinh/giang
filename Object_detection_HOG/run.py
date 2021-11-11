import os
import sys
import yaml
from scake import Scake
from person_detector import PersonDetector
from HOG import HOG
from nms import NMS
def main(yaml_file):
    with open(yaml_file) as f:
        config = yaml.safe_load(f)
    s = Scake(config, class_mapping=globals())
    s.run()
if __name__ == "__main__":
    main(yaml_file="hog.yml")

