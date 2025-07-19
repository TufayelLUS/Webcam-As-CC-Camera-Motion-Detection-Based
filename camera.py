import cv2
import os
import time
from collections import deque
from datetime import datetime

VIDEO_SAVE_FOLDER = "videos"
os.makedirs(VIDEO_SAVE_FOLDER, exist_ok=True)

# Parameters
PRE_RECORD_SECONDS = 5
POST_RECORD_SECONDS = 10
FPS = 30

def current_time_str():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def create_video_writer(frame_width, frame_height, filename):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    return cv2.VideoWriter(filename, fourcc, FPS, (frame_width, frame_height))

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
height, width = frame.shape[:2]

pre_record_buffer = deque(maxlen=PRE_RECORD_SECONDS * FPS)
recording = False
last_motion_time = None
video_writer = None

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(gray)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = any(cv2.contourArea(c) > 500 for c in contours)

    pre_record_buffer.append(frame.copy())

    current_time = time.time()

    if motion_detected:
        last_motion_time = current_time
        if not recording:
            filename = os.path.join(VIDEO_SAVE_FOLDER, f"motion_{current_time_str()}.avi")
            video_writer = create_video_writer(width, height, filename)
            for buffered_frame in pre_record_buffer:
                video_writer.write(buffered_frame)
            recording = True
            print(f"Started recording: {filename}")

    if recording:
        video_writer.write(frame)

        if last_motion_time and current_time - last_motion_time >= POST_RECORD_SECONDS:
            recording = False
            video_writer.release()
            video_writer = None
            pre_record_buffer.clear()
            print("Stopped recording.")

    cv2.imshow('Monitoring', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
