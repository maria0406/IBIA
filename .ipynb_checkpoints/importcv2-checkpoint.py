import cv2
import os
import time
import uuid

IMAGES_PATH = 'path_to_your_images_directory'  # Update with your desired path
labels = []
number_imgs = 5

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('camera check')
    print(f'Collecting for {label}')
    time.sleep(4)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, f'{label}_{uuid.uuid1()}.png')
        cv2.imwrite(imagename, frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()

cv2.destroyAllWindows()
