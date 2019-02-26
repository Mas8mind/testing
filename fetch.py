from tkinter import *
import wikipedia
from googlesearch import search
def wiki():
    entry_value=entry.get()
    answer.delete(1.0,END)
    try:
        answer_value=wikipedia.summary(entry_value)
        answer.insert(INSERT,answer_value)
    except:
        answer.insert(INSERT,"Please check your input or your internet connection")
def google(): 
    entry_value=entry.get()
    answer.delete(1.0,END)
    try:
        for url in search(entry_value, tld='es', lang='es', stop=5 ):
            answer.insert(INSERT,url)
    except:
        answer.insert(INSERT,"Please check your input or your internet connection")
root=Tk()
topframe=Frame(root)
entry=Entry(topframe)
entry.pack()
button1=Button(topframe,text="wikipedia",command=wiki)
button2=Button(topframe,text="google links",command=google)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
topframe.pack(side=TOP)
bottomframe=Frame(root)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottomframe,width=30,height=20,wrap=WORD,yscrollcommand=scroll.set)
answer.pack()
scroll.config(command=answer.yview)
bottomframe.pack(side=BOTTOM)
root.geometry("300x300")
root.mainloop()
