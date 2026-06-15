import cv2, numpy, os
size = 4
haar_file = 'haarcascade_frontalface_default.xml'
# make datasets path relative to this script file to avoid cwd issues
script_dir = os.path.dirname(os.path.abspath(__file__))
datasets = os.path.join(script_dir, 'datasets')
print(f'Using datasets directory: {datasets}')
# prediction threshold and verbosity
PREDICTION_THRESHOLD = 800
VERBOSE = True
print('Training...')
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            print(f'Trying to load: {path}')
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
            print(labels)
        id += 1
(width, height) = (130, 100)

## filter out unreadable images and validate training data
filtered_images = []
filtered_labels = []
for img, lab in zip(images, labels):
    if img is None:
        print(f'Warning: failed to read an image for label {lab}')
        continue
    filtered_images.append(img)
    filtered_labels.append(lab)

if len(filtered_images) == 0:
    raise ValueError("No training images were loaded. Check the 'datasets' folder and image file paths.")

images = numpy.array(filtered_images)
labels = numpy.array(filtered_labels)

from collections import Counter
label_counts = Counter(labels)
print(f'Training samples: {len(images)}, label distribution: {label_counts}')
if len(images) < 2:
    raise ValueError('Need at least two training samples to train a recognizer.')
if len(label_counts) < 2:
    print('Warning: Fisherfaces requires at least two distinct subjects. Consider using more subjects or use LBPH as fallback.')
## try multiple recognizer creation methods for compatibility
try:
    model = cv2.face.FisherFaceRecognizer_create()
except Exception:
    try:
        model = cv2.face.createFisherFaceRecognizer()
    except Exception:
        try:
            model = cv2.face.LBPHFaceRecognizer_create()
            print('Using LBPHFaceRecognizer as a fallback recognizer')
        except Exception:
            raise ImportError('No suitable face recognizer found in cv2.face.\n'
                              'Install opencv-contrib-python (pip install opencv-contrib-python)')

model.train(images, labels)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
cnt=0
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #converting gray scale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))

        prediction = model.predict(face_resize)
        if VERBOSE:
            label = prediction[0]
            conf = prediction[1]
            name = names.get(label, 'Unknown')
            print(f'Frame prediction -> label: {label} name: {name} confidence: {conf:.2f}')
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < PREDICTION_THRESHOLD:
            cv2.putText(im,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_COMPLEX,1,(51, 255, 255))
            print (names[prediction[0]])
            cnt=0
        else:
            cnt+=1
            cv2.putText(im,'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            if(cnt>100):
                print("Unknown Person")
                cv2.imwrite("input.jpg",im)
                cnt=0
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
