import tkinter as tk
from PIL import Image, ImageTk
from plyer import notification
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load('alarm-sound.mp3')

root =tk.Tk()
root.title("Clock")
canvas = tk.Canvas(root, width=780, height=439)
canvas.grid(columnspan =4, rowspan = 6)

#instructions
instructions = tk.Label(root, text ="Set your alarm and never miss a thing", font ="Raleway")
c_inst=canvas.create_window(253,400,anchor="nw",window=instructions)


#background
load = Image.open('background.jpg')
render = ImageTk.PhotoImage(load)
wall_paper=canvas.create_image(0,0,image=render,anchor="nw")


#logo
logo =Image.open('clock.png')
logo =ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.Image = logo
logo_sym=canvas.create_window(340,45,anchor="nw",window=logo_label)

root.resizable(width=False,height=False)


a_time = 0
x= [0,0]
def a():
    global a_time,x,play
    play = True
    a_time=e.get()
    if a_time != "":
        notification.notify("alarm","your alarm has been set",timeout =5)       
    x = list(a_time.split(':'))
    clock()
    print(a_time)
    print(x)
    return

play = False

def clock():
            global a_time,x,play
            second=time.strftime("%S")
            hour=time.strftime("%I")
            minute=time.strftime("%M")
            am_pm=time.strftime("%p")
            day=time.strftime("%A")
            date=time.strftime("%e")
            mon=time.strftime("%B")
            t=hour+':'+minute+':'+second
            today=mon+','+date+' ,'+day
            
            timer.config(text=t)
            td=canvas.create_text(390,200,fill="black",font=("bold",30),text=day+","+ date +' '+mon)

            
            if str(hour) == str(x[0]) and str(minute) == str(x[1]):
                if int(second)< 15 and play == True:
                    play = False
                    pygame.mixer.music.play()
                elif play == False and int(second)>15:
                    pygame.mixer.music.stop()
                                                       
            timer.after(1000,clock)

                    
timer=tk.Label(root,text="",font=("ds-digital",48),fg="blue",bg='black')
e=tk.Entry(root,bg="black",fg="white",font = 5)
mybutton=tk.Button(root,text='set alarm',padx=5,pady=5,command=a,fg='black',bg='white')

c_timer=canvas.create_window(250,100,anchor="nw",window=timer)
c_e=canvas.create_window(290,250,anchor="nw",window=e) 
c_button=canvas.create_window(350,280,anchor="nw",window=mybutton)

clock()
root.mainloop()
