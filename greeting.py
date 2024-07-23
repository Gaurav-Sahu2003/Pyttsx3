import pyttsx3
import datetime

engine=pyttsx3.init()
x=datetime.datetime.now()

password=input("Enter your password : ")
if password=="seed" :
   hour=int(x.strftime("%H"))
   if hour < 12:
       print("GOOD MORNING")
       engine.say("good morning")
       engine.runAndWait()
   elif 12<= hour < 18 :
       print("GOOD AFTERNOON")
       engine.say("good afternoon")
       engine.runAndWait()  
   else:
       print("GOOD EVENING")
       engine.say("good evening")
       engine.runAndWait() 
    
    
else:
    print("invalid password")
    engine.say("invalid password")
    engine.runAndWait()