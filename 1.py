
#                                ----NOTE-TAKING-APP-USING-TKINTER-AND-DATABASE----BY-YASH JAIN-----


from tkinter import *
import tkinter.font as font
import sqlite3

#CREATING-DATABASE

con=sqlite3.connect("notes.db")
cursorobj= con.cursor()
cursorobj.execute("CREATE TABLE IF NOT EXISTS all_notes(title text PRIMARY KEY, body text)")
con.commit()

#MAIN-WINDOW

root=Tk()
root.title('Note Taking App')
root.geometry('700x500+300+80')
topframe=Frame(root)
topframe.pack()

#ADD-NEW-NOTE

def add_new():
    root1=Tk()
    root1.title('Add New Note')
    root1.geometry('600x300+350+150')
    font_b1 = font.Font(size='20', weight='bold')
    label1 = Label(root1, text='Title:', fg='purple', font=font_b1)
    label1.grid(row=0, column=0)
    title = Entry(root1, width='60')
    title.grid(row=0, column=1)
    body = Text(root1, width='80')
    body.grid(columnspan=10)

#INSERT-INTO-NOTE

    def s1_note():
        note_insert1 = "INSERT INTO all_notes(title,body) values('%s1','%s')" % (title, body)
        cursorobj.execute(note_insert1)
        con.commit()

    save_but1 = Button(root1, text='Save', bg='orange', fg='purple', width='15', command=s1_note)
    save_but1.grid(row=0, column=5)

#EDIT-NEW-NOTE

def edit_note():
    root2=Tk()
    root2.title('Edit Note')
    root2.geometry('600x300+350+150')
    font_b1 = font.Font(size='20', weight='bold')
    label1 = Label(root2, text='Title:', fg='purple', font=font_b1)
    label1.grid(row=0, column=0)
    title = Entry(root2, width='60')
    title.grid(row=0, column=1)
    body = Text(root2, width='80')
    body.grid(columnspan=10)

#UPDATE-NOTE

    def s2_note():
        note_insert2 = "UPDATE all_notes SET body='%s' where title='%s'" % (body, title)
        cursorobj.execute(note_insert2)
        con.commit()

    save_but2 = Button(root2, text='Save', bg='orange', fg='purple', width='15', command=s2_note)
    save_but2.grid(row=0, column=5)

#DELETE-NOTE

def delete():
    root3 = Tk()
    root3.title('Edit Note')
    root3.geometry('700x50+300+250')
    font_b1 = font.Font(size='20', weight='bold')
    label1 = Label(root3, text='Title of Note to Delete:', fg='purple', font=font_b1)
    label1.grid(row=0, column=0)
    title = Entry(root3, width='60')
    title.grid(row=0, column=1)

#DELETE-FUNC

    def s3_note():
        note_insert3 = "DELETE FROM all_notes WHERE title ='%s'" % (title)
        cursorobj.execute(note_insert3)
        con.commit()

    del_but2 = Button(root3, text='Delete', bg='orange', fg='purple', width='15', command=s3_note)
    del_but2.grid(row=0, column=5)

#SEARCH-NOTE

def search():
    cursorobj.execute("SELECT * FROM all_notes")
    t=cursorobj.fetchall()
    for title in t:
        print(title)

#MAIN-WINDOW-

font_b1=font.Font(size='13',weight='bold')
button1=Button(topframe,text='Add New Note',font=font_b1,bg='orange',fg='purple',width='15',command=add_new)
button2=Button(topframe,text='Edit Note',font=font_b1,bg='orange',fg='purple',width='15',command=edit_note)
button3=Button(topframe,text='Delete Note',font=font_b1,bg='orange',fg='purple',width='15',command=delete)
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
label1=Label(topframe,text='Search Notes')
label1.grid(row=1,sticky=W)
entry1=Entry(topframe,width='50')
entry1.grid(row=2,column=0)
font_b2=font.Font(size='9',weight='bold')
button4=Button(topframe,text='Search',font=font_b2,bg='orange',fg='purple',height='1',width='15',command=search)
button4.grid(row=2,column=1)
bottomframe=Frame(root)
bottomframe.pack(fill='both',expand=True)
font_b3=font.Font(size='25',weight='bold')
label3=Label(bottomframe,text='--All Notes--',font=font_b3)
label3.pack(side=TOP)

#LISTBOX-DISPLAY-ALL-NOTES

label2=Listbox(bottomframe,font=font_b3)

#SCROLL-BAR

scroll = Scrollbar(bottomframe, command=label2.yview)
label2.configure(yscrollcommand=scroll.set)
label2.pack(side=LEFT,fill='both',expand=True)
scroll.pack(side=RIGHT, fill=Y)

#DISPLAY-ALL-NOTES

cursorobj.execute("SELECT * FROM all_notes")
t = cursorobj.fetchall()
for title in t:
    label2.insert(END,title)

root.mainloop()
