from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagement:
   
    def __init__(self,root):
        self.root=root
        self.root.title("library Management System")
        self.root.resizable(0,0)
        self.root.geometry("1550x800+0+0")

        # variable
        self.member_var=StringVar()
        self.joinc_var=StringVar()
        self.phoneno_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.codeposti_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.borrow_var=StringVar()
        self.due_var=StringVar()
        self.late_var=StringVar()
        self.fine_var=StringVar()
        self.expiry_var=StringVar()
    
        lbltitle=Label(self.root,text="مدیریت کتابخانه",bg='#1C6758',fg='white',bd=20,relief=RIDGE,font=('IRANSANSWEB',25,'bold'),padx=1,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        frame=Frame(self.root,bd=0,bg='#1C6758')
        frame.place(x=0,y=120,width=1550,height=400)

        # dataframeleft
        DataFrameLeft=LabelFrame(frame,text="  عضویت کتابخانه  ",bg='#1C6758',fg='white',bd=8,relief=RIDGE,font=('IRANSANSWEB',16,'bold'))
        DataFrameLeft.place(x=50,y=2,width=880,height=380)

        lblMember=Label(DataFrameLeft,text=": نوع عضویت",font=('IRANSANSWEB',11),padx=2,pady=5,bg='#1C6758')
        lblMember.place(x=730,y=3)
        comboMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=('IRANSANSWEB',11),width=20,state="readonly")
        comboMember["value"]=("ادمین","اعضا")
        comboMember.place(x=520,y=6)

        lbljoincode=Label(DataFrameLeft,text=": کد عضویت",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lbljoincode.place(x=734,y=50)
        txt_joincode=Entry(DataFrameLeft,textvariable=self.joinc_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_joincode.place(x=520,y=53)

        lblphoneno=Label(DataFrameLeft,text=": شماره همراه",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblphoneno.place(x=735,y=96)
        txt_phoneno=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_phoneno.place(x=520,y=99)

        lblّFname=Label(DataFrameLeft,text=": نام ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّFname.place(x=735,y=140)
        txt_Fname=Entry(DataFrameLeft,textvariable=self.firstname_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_Fname.place(x=520,y=145)

        lblّLname=Label(DataFrameLeft,text=": نام خانوادگی",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّLname.place(x=734,y=182)
        txt_Lname=Entry(DataFrameLeft,textvariable=self.lastname_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_Lname.place(x=520,y=188)

        lblّAddress=Label(DataFrameLeft,text=": آدرس ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّAddress.place(x=734,y=225)
        txt_Address=Entry(DataFrameLeft,textvariable=self.address_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_Address.place(x=520,y=233)

        lblّpostcode=Label(DataFrameLeft,text=": کد پستی ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّpostcode.place(x=734,y=270)
        txt_postcode=Entry(DataFrameLeft,textvariable=self.codeposti_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_postcode.place(x=520,y=276)
    # ================================================================================
        lblّbookid=Label(DataFrameLeft,text=": کد کتاب ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّbookid.place(x=300,y=3)
        txt_bookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_bookid.place(x=80,y=6)

        lblّbookname=Label(DataFrameLeft,text=": نام کتاب ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّbookname.place(x=300,y=50)
        txt_bookname=Entry(DataFrameLeft,textvariable=self.bookname_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_bookname.place(x=80,y=53)

        lblّbarrowdate=Label(DataFrameLeft,text=": تاریخ  قرض ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّbarrowdate.place(x=300,y=96)
        txt_barrowdate=Entry(DataFrameLeft,textvariable=self.borrow_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_barrowdate.place(x=80,y=99)

        lblّduedate=Label(DataFrameLeft,text=": تاریخ  تحویل ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّduedate.place(x=300,y=140)
        txt_duedate=Entry(DataFrameLeft,textvariable=self.due_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_duedate.place(x=80,y=145)

        lblّlatedue=Label(DataFrameLeft,text=": دیرکرد  ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّlatedue.place(x=300,y=182)
        txt_latedue=Entry(DataFrameLeft,textvariable=self.late_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_latedue.place(x=80,y=188)

        lblّfineprice=Label(DataFrameLeft,text=": هزینه  دیرکرد ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّfineprice.place(x=300,y=225)
        txt_fineprice=Entry(DataFrameLeft,textvariable=self.fine_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_fineprice.place(x=80,y=233)

        lblّexpiration=Label(DataFrameLeft,text=":  تاریخ انقضا عضویت ",font=('IRANSANSWEB',11),padx=2,bg='#1C6758')
        lblّexpiration.place(x=300,y=270)
        txt_expiration=Entry(DataFrameLeft,textvariable=self.expiry_var,font=('IRANSANSWEB',11),bd=0,fg='#1C6758',background='#A7C4BC',width=22)
        txt_expiration.place(x=80,y=275)
        
        # dataframeRight
        DataFrameRight=LabelFrame(frame,text="   جزئیات کتاب  ",bg='#1C6758',fg='white',bd=8,relief=RIDGE,font=('IRANSANSWEB',16,'bold'))
        DataFrameRight.place(x=975,y=2,width=520,height=380)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=4,sticky="ns")


        Booklist=['شاهنامه','دیوان حافظ','رباعیات خیام','آینه در آینه','هشت کتاب',
                  'مثل خون در رگ های من','دیوان شهریار','اشعار سیمین بهبهانی',
                  'لیلی و مجنون','بهارستان ','هزار و یک شب','شوهر آهو خانم',
                  'سمفونی مردگان','گورستان آرزو','کولی و نامه عشق','پاسخ به تاریخ',
                  'ملت عشق','بیشعوری','بوف کور','چشمهایش','گناه','لطفا گوسفند نباشید',
                  'ماتیلدا','اثر انگشت','زنان زیرک','اثر مرکب','صد سال تنهایی','یک عاشقانه آرام','سووشون','چهار اثر']
        
        ListBox=Listbox(DataFrameRight,font=('IRANSANSWEB',11),width=50,height=12,bg='#A7C4BC',bd=0)
        ListBox.grid(row=0,column=3,padx=10)
        listScrollbar.config(command=ListBox.yview)
        for item in Booklist:
            ListBox.insert(END,item)
        
        def SelectBook(event):
            x=event.widget
            value=int(x.curselection()[0])
            index=x.get(value)
            if(index=="شاهنامه"):
                self.bookid_var.set("bkid1")
                self.bookname_var.set("شاهنامه")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="دیوان حافظ"):
                self.bookid_var.set("bkid2")
                self.bookname_var.set("دیوان حافظ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="رباعیات خیام"):
                self.bookid_var.set("bkid3")
                self.bookname_var.set("رباعیات خیام")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="آینه در آینه"):
                self.bookid_var.set("bkid4")
                self.bookname_var.set("آینه در آینه")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="هشت کتاب"):
                self.bookid_var.set("bkid5")
                self.bookname_var.set("هشت کتاب")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="مثل خون در رگ های من"):
                self.bookid_var.set("bkid6")
                self.bookname_var.set("مثل خون در رگ های من")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="دیوان شهریار"):
                self.bookid_var.set("bkid7")
                self.bookname_var.set("دیوان شهریار")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="اشعار سیسمین بهبهانی"):
                self.bookid_var.set("bkid8")
                self.bookname_var.set("اشعار سیمین بهبهانی")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="لیلی و مجنون"):
                self.bookid_var.set("bkid9")
                self.bookname_var.set("لیلی و مجنون")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="بهارستان"):
                self.bookid_var.set("bkid10")
                self.bookname_var.set("بهارستان")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="هزار و یک شب"):
                self.bookid_var.set("bkid11")
                self.bookname_var.set("هزار و یک شب")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="شوهر آهو خانم"):
                self.bookid_var.set("bkid12")
                self.bookname_var.set("شوهر آهو خانم")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000") 
                
            elif(index=="سمفونی مردگان"):
                self.bookid_var.set("bkid13")
                self.bookname_var.set("سمفونی مردگان")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000") 
                
            elif(index=="گورستان آرزو"):
                self.bookid_var.set("bkid14")
                self.bookname_var.set("گورستان آرزو")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="کولی و نامه عشق"):
                self.bookid_var.set("bkid15")
                self.bookname_var.set("کولی و نامه عشق")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")
            
            elif(index=="پاسخ به تاریخ"):
                self.bookid_var.set("bkid16")
                self.bookname_var.set("پاسخ به تاریخ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="ملت عشق"):
                self.bookid_var.set("bkid17")
                self.bookname_var.set("ملت عشق")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="بیشعوری"):
                self.bookid_var.set("bkid18")
                self.bookname_var.set("بیشعوری")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="بوف کور"):
                self.bookid_var.set("bkid19")
                self.bookname_var.set("بوف کور")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="چشمهایش"):
                self.bookid_var.set("bkid20")
                self.bookname_var.set("چشمهایش")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="گناه"):
                self.bookid_var.set("bkid21")
                self.bookname_var.set("گناه")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="لطفا گوسفند نباشید"):
                self.bookid_var.set("bkid22")
                self.bookname_var.set("لطفا گوسفند نباشید")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="ماتیلدا"):
                self.bookid_var.set("bkid23")
                self.bookname_var.set("ماتیلدا")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")
            
            elif(index=="اثر انگشت"):
                self.bookid_var.set("bkid24")
                self.bookname_var.set("اثر انگشت")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="زنان زیرک"):
                self.bookid_var.set("bkid25")
                self.bookname_var.set("زنان زیرک")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="اثر مرکب"):
                self.bookid_var.set("bkid26")
                self.bookname_var.set("اثر مرکب")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="صد سال تنهایی"):
                self.bookid_var.set("bkid27")
                self.bookname_var.set("صد سال تنهایی")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="یک عاشقانه آرام"):
                self.bookid_var.set("bkid28")
                self.bookname_var.set("یک عاشقانه آرام")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="سووشون"):
                self.bookid_var.set("bkid29")
                self.bookname_var.set("سووشون")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")

            elif(index=="چهار اثر"):
                self.bookid_var.set("bkid30")
                self.bookname_var.set("چهار اثر")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.late_var.set("بدون تاخیر")
                self.fine_var.set("20,000")
            

        ListBox.bind("<<ListboxSelect>>",SelectBook)
        

        # button frame
        FrameButton=Frame(self.root,bd=3,bg='#1C6758')
        FrameButton.place(x=0,y=520,width=1550,height=70)

        btnAddData=Button(FrameButton,command=self.adda_data,text='  افزودن ',font=('IRANSANSWEB',11,'bold'),width=24,bg='#A7C4BC',fg='#111',bd=0,padx=8,pady=4)
        btnAddData.place(x=50,y=0)

        btnupdateData=Button(FrameButton,command=self.updatedata,text=' ویرایش ',font=('IRANSANSWEB',11,'bold'),width=24,bg='#A7C4BC',fg='#111',bd=0,padx=8,pady=4)
        btnupdateData.place(x=350,y=0)

        # 
        btndeleteData=Button(FrameButton,command=self.DltData,text=' حذف ',font=('IRANSANSWEB',11,'bold'),width=24,bg='#A7C4BC',fg='#111',bd=0,padx=8,pady=4)
        btndeleteData.place(x=650,y=0)

        btnResetData=Button(FrameButton,command=self.Reset,text=' بازنشانی ',font=('IRANSANSWEB',11,'bold'),width=24,bg='#A7C4BC',fg='#111',bd=0,padx=8,pady=4)
        btnResetData.place(x=950,y=0)

        btnExit=Button(FrameButton,command=self.iExit,text=' خروج ',font=('IRANSANSWEB',11,'bold'),width=24,bg='#A7C4BC',fg='#111',bd=0,padx=8,pady=4)
        btnExit.place(x=1250,y=0)

        # ifo frame
        FrameDetails=Frame(self.root,bd=3,bg='#1C6758')
        FrameDetails.place(x=0,y=595,width=1550,height=250)
         
        Table_frame=Frame(FrameDetails,bd=1,bg='#91D3AF')
        Table_frame.place(x=20,y=7,width=1500,height=185)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","joincode","phone",
                                                             "name","lname","address","postcode",
                                                             "bookid","bookname","borrowdate","duedate",
                                                             "latedue","fineprice","expiration"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="نوع عضویت")
        self.library_table.heading("joincode",text="کد عضویت")
        self.library_table.heading("phone",text="شماره همراه")
        self.library_table.heading("name",text="نام")
        self.library_table.heading("lname",text="نام خانوادگی")
        self.library_table.heading("address",text="آدرس")
        self.library_table.heading("postcode",text="کد پستی")
        self.library_table.heading("bookid",text="کد کتاب")
        self.library_table.heading("bookname",text="نام کتاب")
        self.library_table.heading("borrowdate",text="تاریخ قرض")
        self.library_table.heading("duedate",text="تاریخ تحویل")
        self.library_table.heading("latedue",text="دیر کرد")
        self.library_table.heading("fineprice",text=" هزینه دیر کرد")
        self.library_table.heading("expiration",text="دیر تاریخ انقضا عضویت")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=80)
        self.library_table.column("joincode",width=80)
        self.library_table.column("phone",width=100)
        self.library_table.column("name",width=100)
        self.library_table.column("lname",width=120)
        self.library_table.column("address",width=150)
        self.library_table.column("postcode",width=100)
        self.library_table.column("bookid",width=80)
        self.library_table.column("bookname",width=100)
        self.library_table.column("borrowdate",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("latedue",width=70)
        self.library_table.column("fineprice",width=100)
        self.library_table.column("expiration",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host='localhost', user='root', password='1111',database='mydata')
        mycursor=conn.cursor()
        mycursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.joinc_var.get(),
            self.phoneno_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.codeposti_var.get(),
            self.bookid_var.get(),
            self.bookname_var.get(),
            self.borrow_var.get(),
            self.due_var.get(),
            self.late_var.get(),
            self.fine_var.get(),
            self.expiry_var.get()
            ))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("تبریک","فرد با موفقیت ثبت شد")
    
    def updatedata(self):
        conn=mysql.connector.connect(host='localhost', user='root', password='1111',database='mydata')
        mycursor=conn.cursor()
        mycursor.execute("update library set Member=%s,PhoneNo=%s,FirstName=%s,LastName=%s,Address=%s,PostCode=%s,BookId=%s,BookName=%s,BarrowDate=%s,DueDate=%s,LateDue=%s,FinePrice=%s,Expiration=%s where JoinCode=%s",(
            self.member_var.get(),
            self.phoneno_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.codeposti_var.get(),
            self.bookid_var.get(),
            self.bookname_var.get(),
            self.borrow_var.get(),
            self.due_var.get(),
            self.late_var.get(),
            self.fine_var.get(),
            self.expiry_var.get(),
            self.joinc_var.get()))
        conn.commit()
        self.fetch_data()
        self.Reset()
        conn.close()
        messagebox.showinfo("تبریک","ویراش با موفقیت انجام شد")

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', user='root', password='1111',database='mydata')
        mycursor=conn.cursor()
        mycursor.execute("select * from library")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
       

        self.member_var.set(row[0])
        self.joinc_var.set(row[1])
        self.phoneno_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address_var.set(row[5])
        self.codeposti_var.set(row[6])
        self.bookid_var.set(row[7])
        self.bookname_var.set(row[8])
        self.borrow_var.set(row[9])
        self.due_var.set(row[10])
        self.late_var.set(row[11])
        self.fine_var.set(row[12])
        self.expiry_var.set(row[13])

    def Reset(self):
        self.member_var.set(""),
        self.joinc_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.phoneno_var.set(""),
        self.address_var.set(""),
        self.codeposti_var.set(""),
        self.bookid_var.set(""),
        self.bookname_var.set(""),
        self.borrow_var.set(""),
        self.due_var.set(""),
        self.late_var.set(""),
        self.fine_var.set(""),
        self.expiry_var.set(""),

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("مدیریت کتابخانه","آیا میخواهید خارج شوید؟")
        if iExit>0:
            self.root.destroy()
            return
    
    def DltData(self):
        if self.joinc_var.get()=="" or self.phoneno_var.get()=="":
            messagebox.showerror("اخطار","ابتدا  فرد مورد نظر را انتخاب کنید")

        else:
          conn=mysql.connector.connect(host='localhost', user='root', password='1111',database='mydata')
          mycursor=conn.cursor()
          query="delete from library where JoinCode=%s"
          value=(self.joinc_var.get(),)
          mycursor.execute(query,value)

          conn.commit()
          self.fetch_data()
          self.Reset()
          conn.close()
          messagebox.showinfo("تبریک","فرد مورد نظر با موفقیت حذف شد")


librpage=Tk()
obj=LibraryManagement(librpage)
librpage.mainloop()
