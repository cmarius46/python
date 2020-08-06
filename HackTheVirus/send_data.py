import firebase_admin
from firebase_admin import credentials, firestore, storage
import random


import pyrebase
#config acia

config = {
    "apiKey": "AIzaSyCE_8CVn1Zio1f-EXpEgZtp-8aoyxpteVk",
    "authDomain": "bestcamera-7e901.firebaseapp.com",
    "databaseURL": "https://bestcamera-7e901.firebaseio.com/",
    "projectId": "bestcamera-7e901",
    "storageBucket": "bestcamera-7e901.appspot.com",
    "messagingSenderId": "1087271452402",
    "appId": "1:1087271452402:web:9c34a3417a21237ebe5a6b",
    "measurementId": "G-3J20J96NZX"

  };

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
add = random.randrange(9999999)
faceURL = "imagine/dumi" + str(add) + ".jpg"
path_local = "/home/gabi/Desktop/volcano.jpg"
imgurl = storage.child(faceURL).put(path_local)

db = firebase.database()

fever = "212"
initials = "hello"
danger_level = "DAMN"

storage = firebase.storage()

#imgurl=storage.child(faceURL).put("1.jpg")
img_url=storage.child(faceURL).get_url(imgurl['downloadTokens'])

data = {
	"faceURL" : img_url,
	"febra" : fever,
	"initials": initials,
	"pericol" : danger_level
}

db.child("jale").push(data)

#imgurl = storage.child("1.jpg").put("1.jpg",user['idToken'])    
#img_url = storage.child("1.jpg").get_url(imgurl['downloadTokens'])
