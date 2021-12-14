import threading
from tkinter import *

from oauth2client.client import Error
from settings import *
from tkinter import messagebox
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import strftime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
dataBase = firestore.client()

class MyApp:

    def __init__(self,window):

        self.window = window
        self.window.geometry("800x600")
        self.window.title("TalkUp")
        self.window.configure(bg="#ffffff")
        self.frame = Frame(self.window)
        self.frame.pack()
        self.canvas = Canvas(
            self.frame,
            bg="#ffffff",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.pack()
    
        self.font_tup = ("Noto Sans", 12, "bold")


        self.background_img = PhotoImage(file=f"images/background.png")
        self.background = self.canvas.create_image(
            365.0, 301.5,
            image=self.background_img)

        self.img0 = PhotoImage(file=f"images/img0.png")
        self.b0 = Button(
            self.frame,
            command=self.signUp,
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place(
            x=542, y=435,
            width=208,
            height=72)

        self.entry0_img = PhotoImage(file=f"images/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            639.0, 259.0,
            image=self.entry0_img)

        self.entryEmail = StringVar()
        self.entryPass = StringVar()


        self.entry0 = Entry(
            self.frame,
            foreground="#303030",
            textvariable=self.entryEmail,
            font=self.font_tup,
            bd=0,
            bg="#dbd9d9",
            highlightthickness=0)
        self.entry0.place(
            x=543.0, y=231,
            width=192.0,
            height=54)

        self.entry1_img = PhotoImage(file=f"images/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(
            641.0, 366.0,
            image=self.entry1_img)

        self.entry1 = Entry(
            self.frame,
            textvariable=self.entryPass,
            foreground="#303030",
            show="•",
            font=self.font_tup,
            bd=0,
            bg="#d8d7d7",
            highlightthickness=0)

        self.entry1.place(
            x=545.0, y=338,
            width=192.0,
            height=54)

    def Login(self):
        email = self.newentryEmail.get()
        password = self.newentryPass.get()

        try:
            user = auth.sign_in_with_email_and_password(email=email,password=password)
            userId = user['localId']
            nickNameData = dataBase.collection('userData').document(f'{userId}')
            self.loggeduserNickName = nickNameData.get().to_dict()
            nickyname = self.loggeduserNickName['nickname']
            self.chatPage(self.frame1,nickyname)

        except Exception as e:
            print(e)
            messagebox.showerror(message="Incorrect credentials !",title="Try Again")
            self.newentryEmail.set("")
            self.newentryPass.set("")                

    def goToLoginPage(self):
        self.frame.pack_forget()
        self.frame1 = Frame(self.window)
        self.frame1.pack()
        self.canvas1 = Canvas(
            self.frame1,
            bg="#ffffff",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas1.pack()

        self.img1 = PhotoImage(file=f"images/image.png")
        self.b0 = Button(
                self.frame1,
                image=self.img1,
                borderwidth=0,
                highlightthickness=0,
                command=self.Login,
                relief="flat")

        self.b0.place(
                x=296, y=438,
                width=208,
                height=72)

        self.entry0_img = PhotoImage(file=f"images/img_textBox0.png")
        self.entry0_bg = self.canvas1.create_image(
                400.0, 272.0,
                image=self.entry0_img)


        self.newentryEmail = StringVar()
        self.newentryPass = StringVar()


        self.entryNew = Entry(
                self.frame1,
                textvariable=self.newentryEmail,
                font=self.font_tup, 
                bd=0,
                bg="#dbd9d9",
                highlightthickness=0)
        self.entryNew.pack()
        self.entryNew.place(
                x=304.0, y=244,
                width=192.0,
                height=54)

        self.entry1_img = PhotoImage(file=f"images/img_textBox0.png")
        self.entry1_bg = self.canvas1.create_image(
                400.0, 369.0,
                image=self.entry1_img)

        self.entryNew2 = Entry(
                self.frame1,
                textvariable=self.newentryPass,
                font=self.font_tup, 
                bd=0,
                bg="#d8d7d7",
            show="•",
                highlightthickness=0)
        self.entryNew2.pack()
        self.entryNew2.place(
                x=304.0, y=341,
                width=192.0,
                height=54)

        self.background_img = PhotoImage(file=f"images/background1.png")
        self.background = self.canvas1.create_image(
                413.0, 234.5,
                image=self.background_img)

    def signUp(self):
        self.email = self.entry0.get()
        self.password = self.entry1.get()
        try:
            self.user = auth.create_user_with_email_and_password(self.email, self.password)
            self.nickNamePage(frame=self.frame)
        except Exception as e:
            status = messagebox.askyesno(
            title="Login", message="Email already exist, do you want to login instead ?")     
            if  status == True:
                self.goToLoginPage()
            if  status == False:
                messagebox.showwarning(title="Warning", message="Please SignIn Again!")
                self.entryEmail.set("")
                self.entryPass.set("")

    def nickNamePage(self,frame):

        self.nickName = StringVar()
        self.prevFrame = frame
        self.prevFrame.pack_forget()
        self.nickFrame = Frame(self.window)
        self.nickFrame.pack()

        self.nickCanvas = Canvas(
            self.nickFrame,
            bg="#ffffff",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.nickCanvas.pack()

        self.img0 = PhotoImage(file=f"images/hopin.png")
        self.b0 = Button(
            self.nickFrame,
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.addNickName,
            relief="flat")

        self.b0.place(
            x=526, y=116,
            width=208,
            height=72)


        self.entry0_img = PhotoImage(file=f"images/textbox.png")
        self.entry0_bg = self.nickCanvas.create_image(
            625.0, 84.0,
            image=self.entry0_img)

        self.entry0 = Entry(
            self.nickFrame,
            textvariable=self.nickName,
            font=self.font_tup,
            bd=0,
            bg="#dbd9d9",
            highlightthickness=0)

        self.entry0.insert(0, 'Enter Nickname here !')

        self.entry0.place(
            x=529.0, y=56,
            width=192.0,
            height=54)
        self.entry0.configure(state=DISABLED, disabledbackground='#DBD9D9')


        def on_click(event):
            self.entry0.configure(state=NORMAL)
            self.entry0.delete(0, END)
            self.entry0.unbind('<Button-1>', on_click_id)


        on_click_id = self.entry0.bind('<Button-1>', on_click)

        self.background_img = PhotoImage(file=f"images/backgroundnick.png")
        self.background = self.nickCanvas.create_image(
            416.5, 315.5,
            image=self.background_img)

    def addNickName(self):
        name = self.nickName.get()
        if self.nickName.get() == "":
            messagebox.showerror(
                message="Please Enter Nickname!", title="NickName")   
        else:        
            data = {'nickname':name}
            userId = self.user['localId']
            dataBase.collection('userData').document(f'{userId}').set(data)
            self.chatPage(self.nickFrame,name)

    def chatPage(self,frame,name):
        
        self.temp = name
        self.newFrame = frame
        self.newFrame.pack_forget()
        self.chatFrame = Frame(self.window)
        self.chatFrame.pack()
        self.canvas = Canvas(
            self.chatFrame,
            bg="#ffffff",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.pack()
        self.entry0_img = PhotoImage(file=f"images/usertextbox.png")
        self.entry0_bg = self.canvas.create_image(
        330.0, 35.0,
        image=self.entry0_img)

        newText = StringVar()
        newText.set("Hello, "+self.temp)

        self.entry0 = Entry(
            self.chatFrame,
            fg='#000000',
            textvariable=newText,
            font=("Adobe Gothic Std B", 20, "bold"),
            bd=0,
            bg="#ffffff",
            state=DISABLED,
            disabledbackground="#ffffff",
            disabledforeground="#000000",
            highlightthickness=0)

        self.entry0.place(
            x=97.0, y=10,
            width=466.0,
            height=48)

        self.entry1_img = PhotoImage(file=f"images/bigtextbox.png")
        self.entry1_bg = self.canvas.create_image(
            406.5, 549.0,
            image=self.entry1_img)


        self.entry1 = Entry(
            self.chatFrame,
            font=("lato",12),
            bd=0,
            bg="#dbd9d9",
            highlightthickness=0)

        self.entry1.focus()
        self.entry1.bind("<Return>",self.on_enter_pressed)

        self.entry1.place(
            x=54.0, y=521,
            width=705.0,
            height=54)


        self.img0 = PhotoImage(file=f"images/send.png")
        self.b0 = Button(
            self.chatFrame,
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command= lambda : self.on_enter_pressed(NONE),
            relief="flat")

        self.b0.place(
            x=730, y=528,
            width=46,
            height=43)

        self.background_img = PhotoImage(file=f"images/chatframe.png")
        self.background = self.canvas.create_image(
            395.5, 251.5,
            image=self.background_img)

        self.img1 = PhotoImage(file=f"images/logout.png")
        self.b1 = Button(
            self.chatFrame,
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command= self.returnToMainPage,
            relief="flat")

        self.b1.place(
            x=740, y=15,
            width=44,
            height=45)

        self.entryText = Text(
            self.chatFrame,
            bg='#115CC9',
            fg='white',
            font=('Comic Sans', 15,),
            relief='flat',
            state=DISABLED
        )

        self.entryText.place(
            x=100, y=100,
            width=600,
            height=360,
        )

        self.timeLabel = Label(self.chatFrame, font=(
            'calibri', 12, 'bold'), fg='black', bg='white')
        self.timeLabel.place(
            x=600,y=16,
            height=50,
            width=100
        )

        self.getTime()
        doc_ref = dataBase.collection('messages').document('users')
        doc_watch = doc_ref.on_snapshot(self.on_snapshot)
        
    def on_snapshot(self,doc_snapshat, changes, read_time):
        callback_done = threading.Event()
        for doc in doc_snapshat:
            dict = doc.to_dict()
            if self.temp not in dict:
                for key in dict:
                    msg = f"{key}: {dict[key]}\n\n"
                    self.entryText.configure(state=NORMAL)
                    self.entryText.insert(END,msg)
                    self.entryText.configure(state=DISABLED)
        callback_done.set()
            
    def on_enter_pressed(self,event):
        msg = self.entry1.get()
        self._insert_message(msg=msg,sender=self.temp)

    def _insert_message(self,msg,sender):
        if not msg:
            return

        self.entry1.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        data = {f'{sender}':msg}
        dataBase.collection('messages').document('users').set(data)
        self.entryText.configure(state=NORMAL)
        self.entryText.insert(END,msg1)
        self.entryText.configure(state=DISABLED)

    def returnToMainPage(self):
        dataBase.collection('messages').document('users').update({f'{self.temp}':firestore.DELETE_FIELD})
        exit()

    def getTime(self):
        self.time = StringVar()
        self.time = strftime('%H:%M:%S %p')
        self.timeLabel.config(text=self.time)
        self.timeLabel.after(1000,self.getTime)


if __name__ == '__main__':
    window = Tk()
    icon = PhotoImage(file="images/T1.png")
    window.iconbitmap("images/T1.ico")
    window.iconphoto(False,icon)
    window.resizable(False, False)
    myApp = MyApp(window)
    window.mainloop()
