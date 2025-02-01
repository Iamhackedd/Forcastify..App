import tkinter as tk
import requests
from datetime import datetime, timedelta
from tkinter import ttk,messagebox
import pytz

def getWeather():

    try:
        
        
        api="464b6535df7dee469f6d0d0eecc4abc5"
        city=text.get()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api}"
        response=requests.get(url)
        data=response.json()
##        print(data)

        cw.config(text="CURRENT WEATHER")
        
        #city and time
        nam=data['name']
        cname.config(text=nam)
        un.config(text="|")
        
        #time
        timezone=data['timezone']
##        utc_n=datetime.utcnow()
        utc_n = datetime.now(pytz.utc)
        ltime=utc_n+timedelta(seconds=timezone)
        ftime=ltime.strftime("%H:%M")
        clock.config(text=ftime)

        #weather details
        condition=data['weather'][0]['main']
        description=data['weather'][0]['description']
        temp=(data['main']['temp'])
        temp=int(temp-273.15)
        pressure=data['main']['pressure']
        humidity=data['main']['humidity']
        wind=data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","Feels","like",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        dp.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Something went wrong",e)
##        print(e)
   




root=tk.Tk()

root.title("Weather App")
root.geometry("900x500")
root.configure(bg="white")
root.resizable(0,0)

#Search box
sp=tk.PhotoImage(file="sbox.png")
sbox=tk.Label(image=sp,bg="white",justify="center")
sbox.pack()

#search entry
text=tk.Entry(root,justify="center",width=22,font=("poppins",23,"bold"),bg="#404040",border="0",fg="white")
text.place(x=240,y=21)
text.focus()

#Search icon
si=tk.PhotoImage(file="sicon.png")
sricon=tk.Button(image=si,bg="#404040",borderwidth="0",cursor="hand2",command=getWeather)
sricon.place(x=590,y=12)

#logo
l=tk.PhotoImage(file="logo.png")
lg=tk.Label(image=l,bg="white")
lg.place(x=170,y=100)

#Result Upper section
cw=tk.Label(root,font=("arial",15,"bold"),bg="white")
cw.place(x=440,y=90)

un=tk.Label(root,font=("arial",18,"bold"),bg="white")
un.place(x=535,y=115)

cname=tk.Label(root,font=("Helvetica",17),bg="white")
cname.place(x=440,y=120)

clock=tk.Label(root,font=("Helvetica",15),bg="white")
clock.place(x=560,y=120)

#description box
d=tk.PhotoImage(file="dbox.png")
db=tk.Label(image=d,bg="white")
db.pack(padx=5,pady=10,side="bottom")

#descriptions
lbw=tk.Label(root,text="WIND", font=("Helvetica",15,"bold"),fg="white",bg="#00B5EF")
lbw.place(x=120,y=400)

lbh=tk.Label(root,text="HUMIDITY", font=("Helvetica",15,"bold"),fg="white",bg="#00B5EF")
lbh.place(x=250,y=400)

lbd=tk.Label(root,text="DESCRIPTION", font=("Helvetica",15,"bold"),fg="white",bg="#00B5EF")
lbd.place(x=430,y=400)

lbp=tk.Label(root,text="PRESSURE", font=("Helvetica",15,"bold"),fg="white",bg="#00B5EF")
lbp.place(x=650,y=400)

t=tk.Label(font=("arial",70,"bold"),fg="#ee666d",bg="white")
t.place(x=430,y=170)
c=tk.Label(font=("arial",13,"bold"),bg="white")
c.place(x=430,y=290)

w=tk.Label(text="...",font=("arial",20,"bold"),bg="#00b5ef")
w.place(x=120,y=430)

h=tk.Label(text="...",font=("arial",20,"bold"),bg="#00b5ef")
h.place(x=270,y=430)

dp=tk.Label(text="...",font=("arial",20,"bold"),bg="#00b5ef")
dp.place(x=430,y=430)

p=tk.Label(text="...",font=("arial",20,"bold"),bg="#00b5ef")
p.place(x=670,y=430)


root.mainloop()




