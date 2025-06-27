from ultralytics import YOLO
import torch

class YOLODetector:
    def __init__(self, model_path):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        self.model = YOLO(model_path).to(device)

    def infer(self, frame):
        results = self.model(frame)
        return results[0]

    def draw(self, results):
        return results.plot()
