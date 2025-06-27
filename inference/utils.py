import cv2

def display_frame(window_name, frame):
    cv2.imshow(window_name, frame)
    return cv2.waitKey(1) & 0xFF
