import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

model = ''

def training_data_set():
    data_path = "data_set_images/"
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    # onlyfiles = []
    # for userNameDir in listdir(data_path):
    #     print("*********",userNameDir)
    #     for userName in listdir(userNameDir):
    #             print(userName)
    #             if isfile(data_path,userNameDir, userName):
    #                 onlyfiles.append(userName)


    Training_Data, Labels = [], []

    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    # for userNameDir in listdir(data_path):
    #     # for userName in listdir(userNameDir):
    #         for i, files in enumerate(onlyfiles):
    #             image_path = data_path + userNameDir + onlyfiles[i]
    #             images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    #             Training_Data.append(np.asarray(images, dtype=np.uint8))
    #             Labels.append(i)

    Labels = np.asarray(Labels, dtype=np.int32)
    global  model
    model = cv2.face.LBPHFaceRecognizer_create()
    print('*********************** model *', model)


    model.train(np.asarray(Training_Data), np.asarray(Labels))

    print("Dataset Model Training Completed ")


def find_face():
    face_classifer = cv2.CascadeClassifier("xml/face.xml")
    def face_detector(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifer.detectMultiScale(gray, 1.3, 5)
        if faces is():
            return img,[]
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200, 200))

            return img, roi

    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame= cap.read()
        frame = cv2.flip(frame, 1)
        image, face = face_detector(frame)

        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)
            print('********************',result)

            if result[1] < 500:
                confidence = int(100*(1-(result[1])/300))
            if confidence > 82:
                 cv2.putText(image, "krishna", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255, 255), 1)
                 # cv2.imshow("Face cropper", image)
            else:
                cv2.putText(image, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0, 255), 2)
                # cv2.imshow("Face cropper", image)
            cv2.imshow("Face cropper", image)

        except:
            cv2.putText(image, "Face not found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, ( 255 , 0, 0), 2)
            cv2.imshow("Face cropper", image)
        if cv2.waitKey(1) == 13:
             break

    cap.release()
    cv2.destroyAllWindows()

try:
    training_data_set()
    find_face()
except:
 print("Dataset model is not available ")
