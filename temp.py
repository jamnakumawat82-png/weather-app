from tkinter import * 
from tkinter import ttk
import requests
 
def getdata():
	city = city_name.get()
	data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=591506d5aa6cece309e0b43b427e43e5").json()
	lb1.config(text=data["weather"][0]["main"])
	lb2.config(text=data["weather"][0]["description"])
	lb3.config(text=int(data["main"]["temp"]-273.15))
	lb4.config(text=data["main"]["pressure"])



root = Tk()
root.title("A Weather app Demo")
root.config(bg="blue")
root.geometry("650x500")

lb1 = Label(root,text="Weather App",font=("Time new roman",40,"bold"))
lb1.place(x=100,y=25,height=50,width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
"Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
"Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]

city_name = StringVar()
com = ttk.Combobox(root,text="Weather App",values=list_name,
	font=("Time new roman",15,"bold"),textvariable=city_name)
com.place(x=150,y=100,height=40,width=350)



l1 = Label(root,text="Weather Climate",font=("Time new roman",20))
l1.place(x=40,y=220,height=50,width=230)
lb1 = Label(root,font=("Time new roman",20))
lb1.place(x=290,y=220,height=50,width=230)

l2 = Label(root,text="Weather Description",font=("Time new roman",17))
l2.place(x=40,y=290,height=50,width=230)
lb2 = Label(root,font=("Time new roman",17))
lb2.place(x=290,y=290,height=50,width=230)

l3 = Label(root,text="Temperature",font=("Time new roman",20))
l3.place(x=40,y=360,height=50,width=230)
lb3 = Label(root,font=("Time new roman",20))
lb3.place(x=290,y=360,height=50,width=230)

l4 = Label(root,text="Pressure",font=("Time new roman",20))
l4.place(x=40,y=430,height=50,width=230)
lb4 = Label(root,font=("Time new roman",20))
lb4.place(x=290,y=430,height=50,width=230)

but1 = Button(root,text="Done",font=("Time new roman",15,"bold"),command=getdata)
but1.place(x=275,y=160,height=40,width=100)

root.mainloop()