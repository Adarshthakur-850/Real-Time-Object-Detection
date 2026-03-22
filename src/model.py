from ultralytics import YOLO
from .config import MODEL_PATH, CONF_THRESHOLD
import cv2

class ObjectDetector:
    def __init__(self, model_path=MODEL_PATH):
        self.model = YOLO(model_path)

    def predict(self, frame):
        """
        Performs object detection on a single frame.
        Returns:
            results: list of detection results
        """
        results = self.model.predict(
            source=frame,
            conf=CONF_THRESHOLD,
            stream=True,
            verbose=False
        )
        return next(results)
