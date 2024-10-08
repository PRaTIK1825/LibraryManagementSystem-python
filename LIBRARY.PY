from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        


        #==============================variable=============================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

#=====================================DataFrameLeft==========================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,text="Member Type",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,text="PRN NO",padx=2,bg="powder blue",font=("arial",12,"bold"))
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)

        lbltitle=Label(DataFrameLeft,text="ID No:",padx=2,pady=4,bg="powder blue",font=("arial",12,"bold"))
        lbltitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,text="FirstName",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,text="LastName",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,text="Address1",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,text="Address2",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,text="Post Code",padx=2,pady=4,bg="powder blue",font=("arial",12,"bold"))
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblMobile.grid(row=8,column=0,sticky=W)
        txtFirstMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtFirstMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,text="Book Id",padx=2,bg="powder blue",font=("arial",12,"bold"))
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,text="Book Title",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,text="Author Name",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,text="Date Borrowed",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,text="Date Due",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,text="Days On Book",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblDateOverDate=Label(DataFrameLeft,text="Date Over Date",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblDateOverDate.grid(row=6,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",13,"bold"),width=29)
        txtDateOverDate.grid(row=6,column=3)

        lblLateReturnFine=Label(DataFrameLeft,text="Late Return Fine",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblLateReturnFine.grid(row=7,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,text="Actual Price",padx=2,pady=6,bg="powder blue",font=("arial",12,"bold"))
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

#=======================================Data Frame Right===============================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listBooks=['Head Firt Book','Learn Python The Hard Way','Python Programming',"Secrete Rahshy",'Python CookBook','Into to Machine Learning','Fluent Python','The Algortihm','The technich Python','Machine Tecno','My Python','Joss Eliff guru','Elite Jungle Python','Jungli Python','Mumbai Python','Intro Python','programming python','Machine Python'
                   ,'Advance Python','Inton Python','RedChilli Python','Ishq Python','Java Programming','Html Programming','Fake Mustache','rich dad and poor dad','sidekicks','the charlie','Pie','when life gives you',
                   'vanished','popularity papers','the ghost','Junonia']

    
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BK ID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BK ID8796")
                self.booktitle_var.set("basics of python")
                self.author_var.set("ZED SHAW")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="Python Programming"):
                self.bookid_var.set("BK ID1245")
                self.booktitle_var.set("Intro to python Comp Science")
                self.author_var.set("John")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.580")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BK ID2456")
                self.booktitle_var.set("Python CookBook")
                self.author_var.set("sarah guaido")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")    

            elif (x=="Into to Machine Learning"):
                self.bookid_var.set("BK ID8853")
                self.booktitle_var.set("Into to Machine Learning")
                self.author_var.set("Brian james")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.550")

            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BK ID0145")
                self.booktitle_var.set("Secrete")
                self.author_var.set("michael")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.58")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif (x=="Fluent Python"):
                self.bookid_var.set("BK ID4444")
                self.booktitle_var.set("Python ")
                self.author_var.set("jessica goel")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.26")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")

            elif (x=="The Algortihm"):
                self.bookid_var.set("BK ID5655")
                self.booktitle_var.set("Python algorithm")
                self.author_var.set("R.L.sttene")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.64")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.600")

            elif (x=="The technich Python"):
                self.bookid_var.set("BK ID2322")
                self.booktitle_var.set("Python techniques")
                self.author_var.set("Johua")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.80")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="Machine Tecno"):
                self.bookid_var.set("BK ID2386")
                self.booktitle_var.set("Machine Learning")
                self.author_var.set("louis joy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.56")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.839")

            elif (x=="My Python"):
                self.bookid_var.set("BK ID2311")
                self.booktitle_var.set("python Learning")
                self.author_var.set("stephen king")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.80")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif (x=="Joss Eliff guru"):
                self.bookid_var.set("BK ID6373")
                self.booktitle_var.set("beloved")
                self.author_var.set("lord viru")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.76")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.760")


            elif (x=="Elite Jungle Python"):
                self.bookid_var.set("BK ID2335")
                self.booktitle_var.set("mark twain")
                self.author_var.set("louis joy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.33")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.899")


            elif (x=="Jungli Python"):
                self.bookid_var.set("BK ID253")
                self.booktitle_var.set("python")
                self.author_var.set("herman")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.93")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif (x=="Mumbai Python"):
                self.bookid_var.set("BK ID2374")
                self.booktitle_var.set("python level")
                self.author_var.set("emest root")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.534")

            elif (x=="Intro Python"):
                self.bookid_var.set("BK ID2356")
                self.booktitle_var.set("deep python")
                self.author_var.set("john autesn")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.54")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.435")

            elif (x=="programming python"):
                self.bookid_var.set("BK ID6436")
                self.booktitle_var.set("GUI python")
                self.author_var.set("washington")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.79")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.955")  

            elif (x=="Advance Python"):
                self.bookid_var.set("BK ID3386")
                self.booktitle_var.set("advanced python")
                self.author_var.set("william")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.85")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.344")  

            elif (x=="Inton Python"):
                self.bookid_var.set("BK ID2786")
                self.booktitle_var.set("python learning")
                self.author_var.set("george orwell")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.92")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1076")  

            elif (x=="RedChilli Python"):
                self.bookid_var.set("BK ID8386")
                self.booktitle_var.set("python game")
                self.author_var.set("virgina woolf")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.42")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.882")  

            elif (x=="Ishq Python"):
                self.bookid_var.set("BK ID2086")
                self.booktitle_var.set("python role")
                self.author_var.set("james joyce")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.88")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.522")  

            elif (x=="Java Programming"):
                self.bookid_var.set("BK ID2380")
                self.booktitle_var.set("java Learning")
                self.author_var.set("franz kafka")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.83")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.985")  

            elif (x=="Html Programming"):
                self.bookid_var.set("BK ID9386")
                self.booktitle_var.set("Html Learning")
                self.author_var.set("harper lee")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.74")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1299")  

            elif (x=="Fake Mustache"):
                self.bookid_var.set("BK ID1386")
                self.booktitle_var.set("hobbit")
                self.author_var.set("J.R.R tolkien")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.63")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.734")  

            elif (x=="rich dad and poor dad"):
                self.bookid_var.set("BK ID2286")
                self.booktitle_var.set("lord")
                self.author_var.set("salman rushdie")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.41")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.842")  

            elif (x=="sidekicks"):
                self.bookid_var.set("BK ID2486")
                self.booktitle_var.set("catch -22")
                self.author_var.set("leo tolstoy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.66")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1262")  

            elif (x=="the charlie"):
                self.bookid_var.set("BK ID23686")
                self.booktitle_var.set("charlie chaplin")
                self.author_var.set("dr.seuss")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.99")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.837")  

            elif (x=="Pie"):
                self.bookid_var.set("BK ID7386")
                self.booktitle_var.set("ulysses")
                self.author_var.set("tom clancy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.94")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1252")  

            elif (x=="when life gives you"):
                self.bookid_var.set("BK ID5386")
                self.booktitle_var.set("chance")
                self.author_var.set("james michener")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.29")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.855")  

            elif (x=="vanished"):
                self.bookid_var.set("BK ID8633")
                self.booktitle_var.set("demonished")
                self.author_var.set("A.A milne")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.97")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.873")  

            elif (x=="popularity papers"):
                self.bookid_var.set("BK ID2986")
                self.booktitle_var.set("newspaper")
                self.author_var.set("thompson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.52")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1333")                                               

            elif (x=="the ghost"):
                self.bookid_var.set("BK ID2396")
                self.booktitle_var.set("horror")
                self.author_var.set("michael roy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.87")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1288")  

            elif (x=="Junonia"):
                self.bookid_var.set("BK ID2383")
                self.booktitle_var.set("grapes")
                self.author_var.set("john grisham")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.62")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.999")  

            elif (x=="Machine Python"):
                self.bookid_var.set("BK ID2300")
                self.booktitle_var.set("machines")
                self.author_var.set("sylvia plath")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.69")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.899")  

        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

    #    =======================================Buttons frame================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        #    =======================================Infromation Frame================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Tabel_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Tabel_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Tabel_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Tabel_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Tabel_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile",
                                                           "bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine",
                                                           "finalprice","dateoverdue"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="Prn No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("finalprice",text="Final Price")
        self.library_table.heading("dateoverdue",text="DateOverDue")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("finalprice",width=100)
        self.library_table.column("dateoverdue",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="world")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                                ))   
                                                                                                             

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()


        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="world")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Postid=%s,Mobile=%s,Bookid=%s,booktitle=%s,Author=%s,Dateborrowed=%s,datedue=%s,Daysonbook=%s,Latereturnfine=%s,dateoverdue=%s,Finalprice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                ))










                                                                                                                
        
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")

        
        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="world")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from  library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID NO:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book Id:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Latereturnfine:\t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get==()=="":
            messagebox,messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="world")
        my_cursor=conn.cursor()
        query="delete from library where PRN_No=%s"
        value=(self.prn_var.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been deleted")
            
        

                                                                       
   
        
        
       
        


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()        