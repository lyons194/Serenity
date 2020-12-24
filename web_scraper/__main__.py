"""
Verison: 0.0.3
Release Date: 12-24-2020
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
import time


"""

Define memory variables

"""


memory_bank = []


"""

Define tkinter GUI template widgets

"""


root = Tk()
root.wm_title("Wishing Well   |   web scraper")
root.geometry("600x290")
root.resizable(False,False)

set_cwd_entry = Entry(root)
set_cwd_entry.place(x=160,y=20,width=415)
set_cwd_entry.insert(0,"EXAMPLE:   C:\\\\Users\\\\User Name\\\\Documents")

robots_txt_entry = Entry(root)
robots_txt_entry.place(x=160,y=80,width=415)
robots_txt_entry.insert(0,"https://example.com/")

webpage_entry = Entry(root)
webpage_entry.place(x=20,y=140,width=340)
webpage_entry.insert(0,"https://example.com/specific-page/within-website")

html_entry = Entry(root)
html_entry.place(x=375,y=140,width=60)

class_entry = Entry(root)
class_entry.place(x=455,y=140,width=120)

status_message = Entry(root)
status_message.place(x=20,y=240,width=540)

cwd_label = Label(root,text="Status",fg="Blue")
cwd_label.place(x=375,y=40)

html_label = Label(root,text="HTML",fg="Black")
html_label.place(x=375,y=160)

class_label = Label(root,text="Class",fg="Black")
class_label.place(x=455,y=160)

updates_label = Label(root,text="Status Updates",fg="Black")
updates_label.place(x=20,y=260)


"""

Define tkinter GUI entry widgets functionality

"""


def display_message(x):
    try:
        status_message.delete(0,END)
        x_convert=str(x)
        status_message.insert(0,f"{x_convert}")
        
    except:
        status_message.insert(0,"Error: status message unavailable.")

def set_cwd():
    try:
        #current working directory objects
        cwd = set_cwd_entry.get()
        os.chdir(f"{cwd}")

        cwd_label = Label(root,text="Status",fg="Green")
        cwd_label.place(x=375,y=40)
        set_cwd_entry.delete(0,END)
        set_cwd_entry.insert(0,f"{os.getcwd()}")
        
    except:
        cwd_label = Label(root,text="Status",fg="Red")
        cwd_label.place(x=375,y=40)
        set_cwd_entry.delete(0,END)
        set_cwd_entry.insert(0,"EXAMPLE:   C:\\\\Users\\\\User Name\\\\Documents")


"""

.txt file functions

"""


def robots_report(title,request_code,request_reason,page_contents):
    with open(f"{title}.txt","w") as file:
        file.write(f"DOCUMENT TITLE = {title} robots.txt report\n\n")
        file.write(f"REQUEST CODE = {request_code}\n\n")
        file.write(f"REQUEST REASON = {request_reason}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nCODE RETRIEVED:\n\n*  *  *  *  *  *\n\n\n\n{page_contents}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nEND OF DOCUMENT.\n\n*  *  *  *  *  *")

def scrape_report(title,request_code,request_reason):
    with open(f"{title}.txt","w") as file:
        file.write(f"DOCUMENT TITLE = {title} web scraping session report\n\n")
        file.write(f"REQUEST CODE = {request_code}\n\n")
        file.write(f"REQUEST REASON = {request_reason}\n\n")
        file.write(f"\n\n*  *  *  *  *  *\n\nCODE RETRIEVED:\n\n*  *  *  *  *  *\n\n\n\n")
        
        for item in enumerate(memory_bank):
            file.write(f"{item}\n\n")
            
        file.write(f"\n\n\n\n*  *  *  *  *  *\n\nEND OF DOCUMENT.\n\n*  *  *  *  *  *")


"""

Web scraping functions

"""


def robots():
    try:
        #retrieving input data from tkinter widget
        url = str(robots_txt_entry.get())
        url_digest = url.split("/")

        #requesting data from specified website
        session = requests.Session()
        site = session.get(f"{url}robots.txt",timeout=10)

        #https request data
        status_code = site.status_code
        status_reason = site.reason

        #analyzing site data via BeautifulSoup
        data = site.text
        convert = BeautifulSoup(data, features='lxml')
        search = convert.find_all
        result = str(search)
        
        try:
            #generate scraping session .txt report
            robots_report(url_digest[2],status_code,status_reason,result)
            display_message(f"Success:  {url_digest[2]} report created in:  {os.getcwd()}")
            
        except:
            display_message("Error:  could not generate scrape .txt report.")
            
        try:
            #close existing https request session
            session.close()
            
        except:
            quit()
    
    except requests.ConnectionError as e:
        display_message("Connection Error:  Robots.txt not found.")

    except requests.Timeout as e:
        display_message("Timeout Error:  Robots.txt not found.")

    except requests.RequestException as e:
        display_message("Unspecified Error:  Robots.txt not found.")

def scrape_page():
    try:
        #retrieving input data from tkinter widgets
        url = str(webpage_entry.get())
        scrape_html = str(html_entry.get())
        scrape_class = str(class_entry.get())

        #requesting data from specified website
        session = requests.Session()
        site = session.get(f"{url}",timeout=60)

        #https request data
        status_code = site.status_code
        status_reason = site.reason

        #searching for HTML elements via class method
        data = BeautifulSoup(site.content, "html.parser")
        search = data.find_all(f"{scrape_html}",class_=f"{scrape_class}")

        #Adding scraped data to temporary memory
        for item in search:
            memory_bank.append(item)

        try:
            #generate scraping session .txt report
            scrape_report("new",status_code,status_reason)
            display_message(f"Success:  scraping report created in:  {os.getcwd()}")

        except:
            display_message("Error:  could not generate scrape .txt report.")

        #CMD terminal testing objects
        for item in enumerate(memory_bank):
            print(item)
        
        try:
            session.close()
            memory_bank.clear()
            print("https request session closed")
            print("memory cache cleared")
            
        except:
            quit()
        
    except requests.ConnectionError as e:
        display_message("Connection Error:  webpage not found.")

    except requests.Timeout as e:
        display_message("Timeout Error:  webpage not found.")

    except requests.RequestException as e:
        display_message("Unspecified Error:  webpage not found.")


"""

Define menu bar functions.

"""


def close():
    quit()

def reset():
    try:
        robots_txt_entry.delete(0,END)
        robots_txt_entry.insert(0,"")
        webpage_entry.delete(0,END)
        webpage_entry.insert(0,"")
        html_entry.delete(0,END)
        html_entry.insert(0,"")
        class_entry.delete(0,END)
        class_entry.insert(0,"")
        status_message.delete(0,END)
        status_message.insert(0,"")
    except:
        display_message("Error:  could not clear widget contents.")


"""

Define tkinter GUI variables.

"""


menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
file_menu.add_command(label="Close", command=close)
file_menu.add_command(label="Reset",command=reset)
menu.add_cascade(label="File", menu=file_menu)


"""

Define tkinter button functions.

"""

set_cwd_button = Button(root,text="Set directory",width=15,command=set_cwd,activebackground="pink",activeforeground="blue")
set_cwd_button.place(x=20,y=20)

b1 = Button(root, text="Check robots.txt", width=15,command=robots,activebackground="pink", activeforeground="blue")
b1.place(x=20,y=80)

b2 = Button(root, text="Scrape web page", width=15,command=scrape_page,activebackground="pink", activeforeground="blue")
b2.place(x=20,y=170)


"""


__main__ program entry point


"""


def main():
    root.mainloop()
