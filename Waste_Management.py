# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1odQ4v6W0_GyG7K5oS_tLXMhpABadoeH2
"""

from google.colab import drive

drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %pip install ultralytics
import ultralytics
ultralytics.checks()

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="DQ084MQZOJFQ6IQMiCpH")
project = rf.workspace("object-detection-cfmul").project("waste-detection-0momv")
version = project.version(5)
dataset = version.download("yolov8")

from ultralytics import YOLO
model=YOLO('yolov8n.pt')

model.train(data = '/content/data.yaml',epochs=20)

custom=YOLO('/content/runs/detect/train/weights/best.pt')

custom.predict('/content/add_data/test/images',save=True)

!yolo detect predict model= '/content/runs/detect/train/weights/best.pt' source='/content/testing_video.mp4'