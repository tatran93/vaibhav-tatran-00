from tkinter import *
from tkinter import messagebox

import base64 


screen = Tk()
screen.geometry("420x420")
screen.title("Encyrtion and Decyrtion")
screen.configure(bg="blue")
def encrypt():
     passward=code.get()
     if passward=="1234":
         screen1=Toplevel(screen)
         screen1.title("encryption")
         screen1.geometry("400x250")
         screen1.configure(bg="red")
         
         message=text1.get(1.0, END)
         encode_message = message.encode("ascii")  
         base64_bytes = base64.b64encode(encode_message)
         encrypt = base64_bytes.decode("ascii")
         Label(screen1,text="your code is Encrypted",font="impack 15 bold").place(x=30,y=75) 
         text2=Text(screen1,font="30",wrap=WORD)
         text2.place(x=2,y=30,width=390,height=180)
         text2.insert(END,encrypt)
         
     elif(passward==""):
         messagebox.showerror("Error","tuje c* banne ko main hi mila tha kya ")
     elif(passward!="1234"):
         messagebox.showerror("Oops","abee tu kch pagal bhe hai kya c*")
         
def decrypt():
    passward=code.get()
    if passward=="1234":
         screen2=Toplevel(screen)
         screen2.title("decryption")
         screen2.geometry("400x250")
         screen2.configure(bg="grey")
         
         message=text1.get(1.0, END)
         encode_message = message.encode("ascii")  
         base64_bytes = base64.b64decode(encode_message)
         encrypt = base64_bytes.decode("ascii")
         Label(screen2,text="your code is Encrypted",font="impack 15 bold").place(x=30,y=75) 
         text2=Text(screen2,font="30",wrap=WORD)
         text2.place(x=2,y=30,width=390,height=180)
         text2.insert(END,encrypt)
         
    elif(passward==""):
        messagebox.showerror("Error","tuje c* banne ko main hi mila tha kya ")
    elif(passward!="1234"):
        messagebox.showerror("Oops","abee tu kch pagal bhe hai kya c*")
                 
 
def reset():
    text1.delete(1.0,END)
    code.set("")
 
                 
Label(screen,text="enter the text for encyrtion and decyrtion",font="impack 15 bold", bg="green").place(x=10,y=10)
text1=Text(screen ,font="20")
text1.place(x=10,y=50,width=395,height=120)

Label(screen,text="enter secert key",font="impack 13 bold").place(x=130,y=185)
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=110,y=220)

Button(screen,text="Encrytion",font="impack 15 bold",bg="yellow",command=encrypt).place(x=15,y=280,width=170)
Button(screen,text="Decrytion",font="impack 15 bold",bg="skyblue",command=decrypt).place(x=220,y=280,width=170)
Button(screen,text="Reset",font="impack 15 bold",bg="red",command=reset).place(x=110,y=350,width=200)

mainloop()

