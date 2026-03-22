import os

CAMERA_ID = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS = 30

MODEL_PATH = "yolov8n.pt"  # Will automatically download if not present
CONF_THRESHOLD = 0.5
IOU_THRESHOLD = 0.45

SHOW_FPS = True
WINDOW_NAME = "Real-Time Object Detection"
BOX_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SCALE = 0.6
THICKNESS = 2
