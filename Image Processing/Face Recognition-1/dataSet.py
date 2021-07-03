import os
import cv2
import datetime
# import numpy as np
face_classifer = cv2.CascadeClassifier("xml/face.xml")
smail_classifer = cv2.CascadeClassifier("xml/smail.xml")
# name = input("Enter your name : ")
# try:
#    dir = os.makedirs(name)
# except:
#    print("File already exist ")
def dataSetOfImage():
    def face_extractor(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifer.detectMultiScale(gray, 1.3, 5)
        if faces is():
            return  None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]



        return cropped_face

    cap = cv2.VideoCapture(1)
    count = 0
    while True:
        ret, frame = cap.read()
        cropped_image = face_extractor(frame)
        if cropped_image is not None:
            count += 1
            face = cv2.resize(cropped_image, (200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # file_name_path = "data_set_images/"+name+"/"+str(count)+".jpg"
            current_time = datetime.datetime.now()
            file_name_path = "data_set_images/"+str(current_time)+".jpg"

            print(file_name_path)
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
             print("Face Not Found")
        if cv2.waitKey(1) == 13 or count == 100:
            break

    cap.release()
    print("Data Set completed...... ")
    cv2.destroyAllWindows()

dataSetOfImage()
