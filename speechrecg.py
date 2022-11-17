import pyttsx3
#import speech_recognition
from tkinter import *
import os

engine1=pyttsx3.init()
print(os.curdir)

def speakyi():

    text1 = tx1.get(1.0, END)
    engine1.say(text1)
    engine1.runAndWait()
    engine1.stop()
    #voicespeed=150
    #engine.setProperty('rate',voicespeed)


window1_1=Tk()
window1_1.title('speech_recog')
window1_1.geometry('490x550+00+00')
window1_1.configure(bg="black")
#image_icon = PhotoImage(file ='.png')
#window1_1.iconphoto(False, image_icon)


logoimp1=PhotoImage(file = 'bgmp3.png')
Label(window1_1,image=logoimp1, bg = "black",height=700).place(x=1,y=0)


logoimp=PhotoImage(file = 'images.png')
Label(window1_1,image=logoimp,bg='powder blue',height=90,width=400,font='arial 80 bold').place(x=19,y=50)




#f=Frame(window1_1,width=999999,height=999999,bg='black').pack()
Label(text='* text to voice converrter *',font='arial 17 bold',fg='red',bg='yellow').place(x=110,y=300)
window1_1.resizable(False, False)

tx1=Text(window1_1,bg='white',fg = "black", font=("calibri 15"),relief=GROOVE,wrap=WORD)
tx1.place(x=50,y=150, height=200, width=400)
Scrollbar1=Scrollbar(window1_1)
Scrollbar1.place(x=37,y=150, height = 200)
Scrollbar1.configure(command=tx1.yview)
tx1.configure(yscrollcommand=Scrollbar1.set)

#Label(text='hit the "press" btn to listen written text ',fg='white').pack()
Button(text='press',font="arial,15,bold",bg='red',fg='black',bd=5,command=speakyi).place(x=220,y=100)


window1_1.mainloop()
