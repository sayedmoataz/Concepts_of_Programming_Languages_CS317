from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import tkinter as tk

GuiFun_Bouns()
############### G U I ###########

def GuiFun_Bouns() :
    HEIGHT = 600
    WIDTH = 600

    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)
    my_email = entry.get()

    label = tk.Label(frame, text="Enter your email", font=40)
    label.place(relx=0.7, relheight=1, relwidth=0.3)

    frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
    frame2.place(relx=0.5, rely=0.3, relwidth=1, relheight=0.1, anchor='n')

    entry2 = tk.Entry(frame2, font=40)
    entry2.place(relwidth=0.65, relheight=1)
    my_password = entry2.get()

    label2 = tk.Label(frame2, text="Enter your password", font=40)
    label2.place(relx=0.7, relheight=1, relwidth=0.317)

    frame3 = tk.Frame(root, bg='#80c1ff', bd=5)
    frame3.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.1, anchor='n')

    entry3 = tk.Entry(frame3, font=40)
    entry3.place(relwidth=0.65, relheight=1)
    his_email = entry3.get()

    label3 = tk.Label(frame3, text="Email of user", font=40)
    label3.place(relx=0.7, relheight=1, relwidth=0.317)

    button1 = tk.Button(root, text="Like and comment", font=40, anchor='se', command= LikeAndCommentFun()).pack()
    button2 = tk.Button(root, text="Follow", font=40, anchor='sw', command=followfun()).pack()

    root.mainloop()

