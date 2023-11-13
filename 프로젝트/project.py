import cv2
import imutils
from imutils.video import VideoStream
import time
import numpy as np
from tflite_runtime.interpreter import Interpreter
import tflite_runtime.interpreter as tflite

# 초기화
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# 설정
exercise_duration = 60  # 운동 시간 (초)
count_interval = 5  # 카운팅 간격 (초)
frame_rate = 30  # 프레임 속도

# 카운팅 변수
count = 0
start_time = time.time()
next_count_time = start_time + count_interval

# TensorFlow Lite 모델 로딩
interpreter = tflite.Interpreter(model_path="your_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

while time.time() - start_time < exercise_duration:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # 전처리: 모델에 맞게 이미지 크기 변경 및 정규화
    input_data = cv2.resize(frame, (input_details[0]['shape'][2], input_details[0]['shape'][1]))
    input_data = np.expand_dims(input_data, axis=0)
    input_data = (input_data.astype(np.float32) / 255.0)

    # 모델 추론
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # 감지된 운동자세에 대한 후속 처리 로직을 추가하세요.

    # 예시로 감지된 경우에 카운팅
    if time.time() >= next_count_time:
        count += 1
        next_count_time += count_interval
        print(f"운동 횟수: {count}")

    # 프레임을 보여줌 (필요시)
    cv2.imshow("Exercise Cam", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# 정리
vs.stop()
cv2.destroyAllWindows()
