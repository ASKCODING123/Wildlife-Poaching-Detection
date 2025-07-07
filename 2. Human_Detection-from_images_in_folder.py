import os
import time
import cv2
from ultralytics import YOLO

folder_path = "C:/Users/ASK/PycharmProjects/PythonProject/Downloaded_Photos"
model = YOLO('yolov8n.pt')
processed_images = set()

def is_file_ready(file_path, wait_time=1.0):
    try:
        initial_size = os.path.getsize(file_path)
        time.sleep(wait_time)
        final_size = os.path.getsize(file_path)
        return initial_size == final_size
    except Exception:
        return False

def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f" Cannot read image: {image_path}")
        return

    results = model(image)
    person_detected = False

    for result in results:
        for box in result.boxes:
            if int(box.cls) == 0:
                person_detected = True

    label = " Human Detected" if person_detected else "No Human Detected"
    color = (0, 0, 255) if person_detected else (0, 255, 0)
    image = cv2.resize(image, (640, 480))

    cv2.putText(image, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    cv2.imshow(f"Result - {os.path.basename(image_path)}", image)
    cv2.moveWindow(f"Result - {os.path.basename(image_path)}", 100, 100)

    cv2.waitKey(3000)
    cv2.destroyAllWindows()

while True:
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]

    for file in image_files:
        file_path = os.path.join(folder_path, file)

        if file_path not in processed_images:
            if is_file_ready(file_path):
                print(f"\n Processing image: {file}")
                try:
                    process_image(file_path)
                    processed_images.add(file_path)
                except Exception as e:
                    print(F" Error processing {file}: {e}")
            else:
                print(f" Skipping (not ready yet): {file}")

    print(" Waiting for new images...\n")
    time.sleep(10)
