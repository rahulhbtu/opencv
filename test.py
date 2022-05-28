import math
from socket import IP_DEFAULT_MULTICAST_LOOP
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTK


class ChatBot:
    def__init__(self, root):
    self.root = root
    self.root.title("ChatBot")
    self.root.geometry("730*620+0+0")

    # for title
    main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
    main_frame.pack()
    img_chat = Image.open('chatbot.jpg')
    img_chat = img_chat.resize((200, 70)
    Img_chat.ANTILIAS)
    self.photoimg = ImageTK.PhotoImage(img_chat)

    Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, images=self.photoimg,
                        text='CHAT ME', font=('arial', 30, 'bold'), fg='green', bg='white'))
    Title_label.pack(side=TOP)
    self.scroll_y = ttk.Scrollbar(main_frame, oriented=VERTICAL)
    self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14),
                     yscrollcommand=self.scroll_y.set)
    self.scroll_y.pack(side=RIGHT, fill=Y)
    self.text.pack()

    btn_frame = Frame(self.root, bd=4, bg="white", width=730)
    btn_frame.pack()
    label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
    label_1.grid(row=0, column=0, padx=5, sticky=W)
    self.entry = ttk.Entry(btn_frame, width=40, font=('times new roman', 16, 'bold'))
    self.entry.grid(row=0, column=0, padx=5, sticky=W)
    self.send = Botton(btn_frame, text="send>>", font=('arial', 15, 'bold'), width=8, bg='green')
    self.send.grid(row=0, column=2, padx=5, sticky=W)
    self.clear = Botton(btn_frame, text="clear data", font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
    self.clear.grid(row=0, column=2, padx=5, sticky=W)

    self.msg = ' '
    self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='green', bg='white')
    self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    # *******************function declaration*************************


def send(self):
    send = '\t\t\t' + 'You ' + self.entry.get()
    self.text.insert(END, '\n' + send)

    if (self.entry.get() == " "):
        self.msg = 'please enter some data'
        self.label_11.config(text=self.msg, fg='red')
    else:
        self.msg = ''
        self.label_11.config(text=self.msg, fg='red')
    if (self.entry.get() == 'hello'):
        self.text.insert(END, '\n\n' + 'Bot: Hi')

    elif (self.entry.get() == 'hi'):
        self.text.insert(END, '\n\n' + 'Bot: Hello')
    elif (self.entry.get() == 'who created you'):
        self.text.insert(END, '\n\n' + 'Bot: jai gurudev')
    else:
        self.text.insert(END, '\n\n' + 'Bot: bye')


if__name__ - -'main__':
root = Tk()
obj = ChatBot(root)
root.mainloop()
