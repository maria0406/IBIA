import os
import time
import uuid
import cv2
import keyboard

IMAGES_PATH = "C:\\Users\\maria\\OneDrive\\Desktop\\RealTimeObjectDetection\\Tensorflow\\workspace\\images"



labels = [{'name':'hello', 'id':31},{'name':'i love you', 'id':32}, 
          {'name':'sorry', 'id':33},{'name':'yes', 'id':34},{'name':'no', 'id':35},{'name':'bye', 'id':36},
          {'name':'house', 'id':37}, {'name':'z', 'id':26}] 
number_imgs = 15

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label['name']), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('camera check')
    print(f'Collecting for {label["name"]}')
    time.sleep(4)
    
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label['name'], f'{label["name"]}_{uuid.uuid1()}.png')
        cv2.imwrite(imagename, frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    
    # Prompt user to press Enter to continue
    print(f'Press Enter to continue to the next label ({chr(label["id"] + ord("a") - 1)})...')
    keyboard.wait('enter')

cv2.destroyAllWindows()