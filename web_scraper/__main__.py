"""
Verison: 0.0.3
Release Date: 12-13-2020
Language:  Python
Author:  Sean Lyons
Email: slyons494@gmail.com

"""


from bs4 import BeautifulSoup
import requests
from tkinter import *
from lxml import html
import os
from requests.exceptions import RequestException


"""

Define tkinter variables.

"""


root = Tk()
root.wm_title("Wishing Well   |   web scraper")
root.geometry("475x160")
root.resizable(False,False)


e1 = Entry(root)
e1.place(x=160,y=20)
e1.insert(0,"https://example.com/")

e2 = Entry(root)
e2.place(x=320,y=20)

label_1 = Label(root,text="Status", fg="Blue")
label_1.place(x=320,y=40)
label_2 = Label(root,text="Status", fg="Blue")
label_2.place(x=320,y=100)

e3 = Entry(root)
e3.place(x=160,y=80)
e3.insert(0,"https://example.com/")

e4 = Entry(root)
e4.place(x=320,y=80)


"""

Define entry boxes functions.

"""


def robots():
    try:
        url = e1.get()
        print(url)
        session = requests.Session()
        site = session.get(f"{url}robots.txt",timeout=10)
        data = site.text
        convert = BeautifulSoup(data, features='lxml')
        search = convert.find_all
        print(str(search))
        e2.insert(0,"Found robots.txt.")
        label_1_green = Label(root,text="Status", fg="Green")
        label_1_green.place(x=320,y=40)
        session.close()
    
    except requests.ConnectionError as e:
        e2.insert(0,"Connection Error:  Robots.txt not found.")
        label_1_red = Label(root,text="Status", fg="Red")
        label_1_red.place(x=320,y=40)
        print(str(e))

    except requests.Timeout as e:
        e2.insert(0,"Timeout Error:  Robots.txt not found.")
        label_1_red = Label(root,text="Status", fg="Red")
        label_1_red.place(x=320,y=40)
        print(str(e))

    except requests.RequestException as e:
        e2.insert(0,"Unspecified Error:  Robots.txt not found.")
        label_1_red = Label(root,text="Status", fg="Red")
        label_1_red.place(x=320,y=40)
        print(str(e))

def scrape_page():
    try:
        url = e3.get()
        print(url)
        session = requests.Session()
        site = session.get(f"{url}",timeout=10)
        data = site.text
        convert = BeautifulSoup(data, features='lxml')
        search = convert.find_all
        print(str(search))
        e4.insert(0,"webpage retrieved")
        label_2_green = Label(root,text="Status", fg="Green")
        label_2_green.place(x=320,y=100)
        session.close()
        
    except requests.ConnectionError as e:
        e4.insert(0,"Connection Error:  webpage not found.")
        label_2_red = Label(root,text="Status", fg="Red")
        label_2_red.place(x=320,y=100)
        print(str(e))

    except requests.Timeout as e:
        e4.insert(0,"Timeout Error:  webpage not found.")
        label_2_red = Label(root,text="Status", fg="Red")
        label_2_red.place(x=320,y=100)
        print(str(e))

    except requests.RequestException as e:
        e4.insert(0,"Unspecified Error:  webpage not found.")
        label_2_red = Label(root,text="Status", fg="Red")
        label_2_red.place(x=320,y=100)
        print(str(e))


"""

Define menu bar functions.

"""


def close():
    quit()


"""

Define GUI variables.

"""


menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
file_menu.add_command(label="Close", command=close)
menu.add_cascade(label="File", menu=file_menu)


"""

Define tkinter button functions.

"""


b1 = Button(root, text="Check robots.txt", width=15,command=robots,activebackground="pink", activeforeground="blue")
b1.place(x=20,y=20)

b2 = Button(root, text="Scrape web page", width=15,command=scrape_page,activebackground="pink", activeforeground="blue")
b2.place(x=20,y=80)


def main():
    root.mainloop()
