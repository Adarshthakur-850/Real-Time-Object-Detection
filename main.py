import cv2
import time
from src.camera import VideoCap
from src.model import ObjectDetector
from src.visualizer import Visualizer
from src.config import CAMERA_ID

def main():
    try:
        cap = VideoCap(CAMERA_ID)
        detector = ObjectDetector()
        visualizer = Visualizer()
    except Exception as e:
        print(f"Error initializing modules: {e}")
        return

    print("Starting Main Loop... Press 'q' to exit.")

    prev_time = 0

    try:
        while True:
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
            prev_time = curr_time

            frame = cap.read_frame()
            if frame is None:
                print("Failed to capture frame")
                break

            results = detector.predict(frame)

            output_frame = visualizer.draw_results(frame, results, fps)
            visualizer.show(output_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        cap.release()
        visualizer.close()
        print("Cleanup done.")

if __name__ == "__main__":
    main()
