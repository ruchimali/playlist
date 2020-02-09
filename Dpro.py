
from tkinter import *
from pygame import mixer


root=Tk()
root.configure(height=900,width=1500,bg='sea green')
global v_list
v_list=[1,4,5]

def stop():
    mixer.music.pause()
def start():
    mixer.music.unpause()
def rewindit():
    mixer.music.rewind()



def nextsongque():
    lab2.configure(bg='#FFDB58')
    image1.configure(image=im4,anchor=N)
    lab3.configure(bg='orange')
    mixer.init()
    mixer.music.load('D:\Project\song3.mp3')
    mixer.music.play()
    play_next2.place_forget()
    buu3.place(x=640,y=630)

    
     
def nextsong():
    lab1.configure(bg='#FFDB58')
    image1.configure(image=im3,anchor=S)
    lab2.configure(bg='orange')
    mixer.init()
    mixer.music.load('D:\Project\song2.mp3')
    mixer.music.play()
    
    play_next.place_forget()
    play_next2.place(x=640,y=630)
       
                
    
    
def playsongs():
    lab3.configure(bg='#FFDB58')
    b3.place_forget()
    buu3.place_forget()
    play_next.place(x=640,y=630)
    mixer.init()
    bu1=Button(root,font=('ALGERIAN',24),text='STOP',bg='#FFDB58',command=stop)
    bu1.place(x=250,y=200)
    bu2=Button(root,font=('ALGERIAN',24),text='START',bg='#FFDB58',command=start)
    bu2.place(x=250,y=280)
    bu3=Button(root,font=('ALGERIAN',24),text='REWIND',bg='#FFDB58',command=rewindit)
    bu3.place(x=250,y=360)
    
         

    
    lab1.configure(bg='orange')
    image1.configure(image=im2)
    mixer.init()
    mixer.music.load('D:\Project\song1.mp3')
    mixer.music.play()
    
    
    


          
              
    

    
def exitit():
    root.destroy()


but3=Button(root,font=('ALGERIAN',24),text='EXIT',bg='#FFDB58',command=exitit)
b3=Button(root,font=('ALGERIAN',24),text='PLAY MY PLAYLIST',bg='#FFDB58',command=playsongs)
b3.place(x=150,y=230)
buu3=Button(root,font=('ALGERIAN',24),text='PLAY NEXT SONG',bg='#FFDB58',command=playsongs)
im1=PhotoImage(file="pic.png")
image1=Button(root,height=310, width=410,image=im1)

form1=Label(root,height=600,width=10,bg='light green')
form1.place(x=0,y=0)
form2=Label(root,height=4,width=250,bg='light green')
form2.place(x=0,y=0)
form3=Label(root,height=4,width=250,bg='light green')
form3.place(x=0,y=750)
form4=Label(root,height=250,width=10,bg='light green')
form4.place(x=1460,y=0)
im3=PhotoImage(file="pic4.png")
im4=PhotoImage(file="pic3.png")
lab1=Label(root,font=('ALGERIAN',24),text='CHEAP THRILLS ',bg='#FFDB58')
lab2=Label(root,font=('ALGERIAN',24),text='FADED',bg='#FFDB58')
lab3=Label(root,font=('ALGERIAN',24),text='WHAT MAKES YOU BEAUTIFUL',bg='#FFDB58')
play_next=Button(root,font=('ALGERIAN',24),text='PLAY NEXT SONG',bg='#FFDB58',command=nextsong)
play_next2=Button(root,font=('ALGERIAN',24),text='PLAY NEXT SONG',bg='#FFDB58',command=nextsongque)
im2=PhotoImage(file="pic2.png")
lab1.place(x=594,y=420)
lab2.place(x=594,y=470)
lab3.place(x=594,y=520)
labb=Label(root,font=('ALGERIAN',30),text='POP PLAYLIST ',bg='light green')
labb.place(x=100,y=10)

but3.place(x=260,y=630)


image1.place(x=600,y=80)
root.mainloop()

