import cv2
from .config import WINDOW_NAME, SHOW_FPS, TEXT_COLOR, BOX_COLOR, FONT_SCALE, THICKNESS

class Visualizer:
    def __init__(self):
        pass

    def draw_results(self, frame, result, fps=None):
        """
        Draws bounding boxes and labels on the frame.
        """
        annotated_frame = result.plot()

        if SHOW_FPS and fps is not None:
             cv2.putText(
                annotated_frame,
                f"FPS: {fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                BOX_COLOR,
                THICKNESS
            )

        return annotated_frame

    def show(self, frame):
        cv2.imshow(WINDOW_NAME, frame)

    def close(self):
        cv2.destroyAllWindows()
