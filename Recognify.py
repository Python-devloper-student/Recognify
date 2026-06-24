import cv2#thanks to cv2 this project uses cv2 library
from deepface import DeepFace#thanks to deep face this project uses deepface community
import pyttsx3
class Recon:
    def __init__(self,camera_0_or_1):#init it takes camera argument use 0 for inbuilt and 1 for externa
     pyttsx3.speak('Welcome to recognify community')#don't worry it will not crah this now officially added by them
     self.camera=cv2.VideoCapture(camera_0_or_1)
     self.face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')#to idetify face
     self.users=[]
     with open('users.txt','a')as noteboook: # creating empty file so it can work wll and load previous registries
          noteboook.write('')
     with open('users.txt','r') as notebook:
        data=notebook.read()
     if data:
       data_list=((data.lstrip("'[")).rstrip("]'")).split(',')
       for i in data_list:
          self.users.append(i.strip("'"))
    def register(self,name):
       s,img=self.camera.read()
       path=name+'.png'
       cv2.imwrite(path,img)
       self.users.append(path)
       with open('users.txt','w')as notebook:
          notebook.write(str(self.users))
    def scan(self):
       detected=[]
       s,img=self.camera.read()
       iimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       faces=self.face_detector.detectMultiScale(iimg,1.2)
       if len(faces)>0:
          print(len(faces),' faces dtected ',end='\r')
          for face in faces:
             x,y,w,h=face
             face_img=img[y:y+h,x:x+w]
             for i in self.users:
                reference=cv2.imread(i)
                try:
                 result=DeepFace.verify(reference,face_img)#varifying face
                 if result['verified']:
                    detected.append((i.split('.'))[0])
                except ValueError :
                   pass
       print('\n Found: \n',detected)
       return detected
pyttsx3.speak('it may take some time to initialize ')#don't worry it will not crah this now officially added by them
print('once initialized it will be fast',end='\r')
