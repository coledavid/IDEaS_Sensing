import depthai as dai

class OakCamera:
    def __init__(self, resolution=(640, 480), fps=30):
        self.resolution = resolution
        self.fps = fps
        self.pipeline = self._create_pipeline()
        self.device = None
        self.video_queue = None

    def _create_pipeline(self):
        pipeline = dai.Pipeline()
        cam = pipeline.createColorCamera()
        cam.setPreviewSize(*self.resolution)
        cam.setInterleaved(False)
        cam.setFps(self.fps)

        xout = pipeline.createXLinkOut()
        xout.setStreamName("video")
        cam.preview.link(xout.input)

        return pipeline

    def start_stream(self):
        self.device = dai.Device(self.pipeline)
        self.video_queue = self.device.getOutputQueue(name="video", maxSize=4, blocking=False)

    def get_frame(self):
        in_frame = self.video_queue.get()
        return in_frame.getCvFrame()

    def close(self):
        if self.device:
            self.device.close()
