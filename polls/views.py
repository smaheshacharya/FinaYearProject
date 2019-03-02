from django.shortcuts import render
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')
def ecommerce(request):
    return render(request,'ecommerce.html')
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
# def login(request):
#     form = LoginForm(request.POST or None) 
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user =authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'login.html', {'form': form})
# import cv2
# import numpy as np

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# url ='http://192.168.1.10:8080/shot.jpg'
# cap = cv2.VideoCapture(0)
# while True:
#     ret , img = cap.read()
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     face = face_cascade.detectMultiScale(gray,1.3,5)#depending upon size of image

#     for (x,y,w,h) in face:
#         cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]

#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#     cv2.imshow('image',img)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()           
