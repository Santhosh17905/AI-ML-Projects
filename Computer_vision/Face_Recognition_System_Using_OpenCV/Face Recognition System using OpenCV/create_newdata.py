import cv2, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'

# Ask user which person's data to collect
sub_data = input('Enter person name to collect data for (e.g., "Elon", "Steve", "YourName"): ').strip()
if not sub_data:
    sub_data = 'kalam'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)
    print(f'Created new folder: {path}')
else:
    print(f'Saving to existing folder: {path}')

(width, height) = (130, 100)
num_images = 30  # collect 30 images per person   


face_cascade = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)  # camera ini
print(f'Collecting {num_images} images for {sub_data}... Press ESC to stop early')
count = 1
while count <= num_images:
    print(count)
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        file_path = os.path.join(path, f'{count}.png')
        cv2.imwrite(file_path, face_resize)
        print(f'Saved: {file_path}')
    count += 1
	
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
print(f'\nData collection complete! Saved {count-1} images to: {path}')
