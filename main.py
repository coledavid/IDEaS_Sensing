import yaml
from camera.oak_camera import OakCamera
from inference.yolo_wrapper import YOLODetector
from inference.utils import display_frame
import cv2

def load_config(path="config/settings.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()

    # Initialize camera
    cam = OakCamera(
        resolution=tuple(config["camera"]["resolution"]),
        fps=config["camera"]["fps"]
    )
    cam.start_stream()

    # Initialize YOLO
    detector = YOLODetector(config["yolo"]["model_path"])

    while True:
        frame = cam.get_frame()
        results = detector.infer(frame)
        annotated = detector.draw(results)
        if display_frame("OAK-D YOLO Inference", annotated) == ord('q'):
            break

    cam.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
