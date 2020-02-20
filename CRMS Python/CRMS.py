from tkinter import*
import time
import tkinter.messagebox
start=''
def main():
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^WINDOW^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    root = Tk()
    root.geometry("1366x770+0+0")
    root.title("Car Repairing And Management System")
    canvas = Canvas(root, width = 1367, height = 771)
    bg_img = PhotoImage(file='D:\\2nd Sem\\Final CRMS\\info.gif')

    canvas.create_image(0, 0, anchor=NW, image= bg_img)
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^frame^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    f= Frame(canvas, width = 358 , height = 450, bg="black")
    f.place(x=530,y=80)

    f2= Frame(canvas, width = 358 , height = 450, bg="black")
    f2.place(x=915,y=80)

    f3= Frame(canvas, width = 470 , height = 560, bg="black")
    f3.place(x=30,y=80)

    f4= Frame(canvas, width = 741 , height = 90, bg="black")
    f4.place(x=530,y=550)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^CLASSES^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    class Info():
            def Receipt(self):
                    self.roo = Tk()
                    self.roo.configure(background="BISQUE")
                    self.roo.geometry("750x450+0+0")
                    self.roo.title("Rate List:")
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="RECEIPT:", fg="black", bg="BISQUE",bd=5)
                    self.rct.grid(row=0, column=2)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Name:", fg="black",bg="BISQUE",anchor=W)
                    self.rct.grid(row=1, column=1)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=name.get(), fg="steel blue",bg="BISQUE", anchor=W)
                    self.rct.grid(row=1, column=4)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Contact:", fg="black",bg="BISQUE", anchor=W)
                    self.rct.grid(row=2, column=1)
                    self.save= Phone.get()
                    if len(self.save) == 11:
                            ph =  phone
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=ph.get(), fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=2, column=4)
                    else:
                            ph =  phone
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="xxxxxx", fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=2, column=4)
                            tkinter.messagebox.showinfo('ERROR',"Please Enter Valid Phone Number")
                            
                    
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Car:", fg="black", bg="BISQUE",anchor=W)
                    self.rct.grid(row=3, column=1)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=(brand.get(),model.get(),modelyear.get()), fg="steel blue", bg="BISQUE",anchor=W)
                    self.rct.grid(row=3, column=4)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Registration Number:", fg="black", bg="BISQUE",anchor=W)
                    self.rct.grid(row=4, column=1)
                    self.save= Registration.get()
                    rg =  registration
                    if len(self.save) == 6:
                            rg =  registration
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=rg.get(), fg="steel blue",bg="BISQUE", anchor=W)
                            self.rct.grid(row=4, column=4)
                            
                    else:
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="xxxxxx", fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=4, column=4)
                            tkinter.messagebox.showinfo('ERROR',"Please Enter Valid Reg. Number")

                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Engine ID:", fg="black", bg="BISQUE",anchor=W)
                    self.rct.grid(row=5, column=1)
                    self.save= EngineID.get()
                    if len(self.save) == 7:
                            ei =  engineID
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=engineID.get(), fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=5, column=4)
                            
                    else:
                            ei = engineID
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="xxxxxx", fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=5, column=4)
                            tkinter.messagebox.showinfo('ERROR',"Please Enter Valid Engine ID")
                            
                    self.rct= Label(self.roo, font=('castellar', 15, 'bold'), text="Email:", fg="black", bg="BISQUE",anchor=W)
                    self.rct.grid(row=6, column=1)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=email.get(), fg="steel blue", bg="BISQUE",anchor=W)
                    self.rct.grid(row=6, column=4)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="CNIC:", fg="black", bg="BISQUE",anchor=W)
                    self.rct.grid(row=7, column=1)
                    self.save= CNIC.get()
                    if len(self.save) == 13:
                            CN =  cnic
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=CN.get(), fg="steel blue",bg="BISQUE", anchor=W)
                            self.rct.grid(row=7, column=4)
                            
                            
                    else:
                            CN =  cnic
                            self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="xxxxxx", fg="steel blue", bg="BISQUE",anchor=W)
                            self.rct.grid(row=7, column=4)
                            tkinter.messagebox.showinfo('ERROR',"Please Enter Valid CNIC Number")

                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Address:", fg="black",bg="BISQUE", anchor=W)
                    self.rct.grid(row=8, column=1)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text=address.get(), fg="steel blue",bg="BISQUE", anchor=W)
                    self.rct.grid(row=8, column=4)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="____________", fg="black",bg="BISQUE", anchor=W)
                    self.rct.grid(row=9, column=2)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="Visit After:", fg="black",bg="BISQUE", anchor=W)
                    self.rct.grid(row=10, column=1)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="3 days", fg="steel blue",bg="BISQUE", anchor=W)
                    self.rct.grid(row=10, column=4)
                    self.rct = Label(self.roo, font=('castellar', 15, 'bold'), text="total COST =", fg="steel blue",bg="BISQUE", anchor=W)
                    self.rct.grid(row=11, column=1)
                    self.rct = Label(self.roo, font=('arial', 15, 'bold'), text=("Rs.",value.get()), fg="steel blue",bg="BISQUE", anchor=W)
                    self.rct.grid(row=11, column=4)
                    if len(phone.get())==11 and len(CNIC.get()) == 13 and len(EngineID.get())==7 and len(Registration.get())== 6:
                            s = [  name.get() ,   ph.get() ,   brand.get(),   model.get() ,   modelyear.get() , rg.get() ,engineID.get() ,  email.get() ,   CN.get() ,  address.get()  ,   value.get()]
                            with open ('Data.txt',"a") as f:
                                    f.write(str(s))
                    else:
                            pass
                    self.roo.mainloop()

            def RATE(self):
                    self.roo = Tk()
                    self.roo.configure(background="BISQUE")
                    self.roo.geometry("500x300+0+0")
                    self.roo.title("Rate List:")
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Parts", fg="black", bg="BISQUE",bd=5)
                    self.rate.grid(row=0, column=0)
                    self.rate = Label(self.roo, font=('castellar', 15,'bold'), text="_____________", fg="white", bg="BISQUE",anchor=W)
                    self.rate.grid(row=0, column=2)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Cost", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=0, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Bumper", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=1, column=0)
                    self.rate= Label(self.roo, font=('aria', 15, 'bold'), text="1500Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=1, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Window Screen", fg="black",bg="BISQUE", anchor=W)
                    self.rate.grid(row=2, column=0)
                    self.rate = Label(self.roo, font=('aria', 15, 'bold'), text="2000Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=2, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Tyre", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=3, column=0)
                    self.rate = Label(self.roo, font=('aria', 15, 'bold'), text="1200Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=3, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Headlights", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=4, column=0)
                    self.rate = Label(self.roo, font=('arial', 15, 'bold'), text="1000Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=4, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Backlights", fg="black",bg="BISQUE", anchor=W)
                    self.rate.grid(row=5, column=0)
                    self.rate = Label(self.roo, font=('arial', 15, 'bold'), text="1000Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=5, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Sidemirror", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=6, column=0)
                    self.rate = Label(self.roo, font=('aria', 15, 'bold'), text="1600Rs/-", fg="steel blue",bg="BISQUE", anchor=W)
                    self.rate.grid(row=6, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Engine", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=7, column=0)
                    self.rate = Label(self.roo, font=('arial', 15, 'bold'), text="16000Rs/-", fg="steel blue",bg="BISQUE", anchor=W)
                    self.rate.grid(row=7, column=3)
                    self.rate = Label(self.roo, font=('castellar', 15, 'bold'), text="Silencer", fg="black", bg="BISQUE",anchor=W)
                    self.rate.grid(row=8, column=0)
                    self.rate = Label(self.roo, font=('arial', 15, 'bold'), text="1800Rs/-", fg="steel blue", bg="BISQUE",anchor=W)
                    self.rate.grid(row=8, column=3)

                    self.roo.mainloop()        

    class f_buttons():
        def qexit(self):
            root.destroy()

        def reset(self):
            name.set("")
            phone.set("")
            company.set("")
            address.set("")
            email.set("")
            cnic.set("")
            brand.set("")
            model.set("")
            modelyear.set("")
            registration.set("")
            engineID.set("")
            cartype.set("")
            
    value=StringVar()
    class COST():
        def click(self,number):
            global start
            start = start + str(number)
            value.set(start)
            x=value
                            
        def rdisplay(self):
            global start
            value.set('')
            

        def equals(self):
            global start
            self.sumup=str(eval(start))
            value.set(self.sumup)
                    

    class Main(f_buttons,COST,Info):
        pass
    
    S=Main()
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^HEADER^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    header= Label(canvas, font=('Castellar',25,'bold'),text="Car Repairing Management System:",bg="black",fg="White",bd=10,anchor='w')
    header.place(x=250,y=15)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^DAMAGE SELECTION^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    label1 = Label(canvas, text="Select Damaged Parts:", font=('castellar',20,"bold"),bg="BISQUE",fg="black")
    label1.place(x=60,y=90)

    display= Entry(canvas,font=('castellar',20,'bold'),textvariable=value, bd=5,insertwidth=7,bg="BURLYWOOD",justify='right')
    display.place(x=60,y=140)

    Bumper=Button(canvas,padx=57,pady=16,bd=4, fg="black", font=('castellar', 10,'bold'),text="Bumper",bg="BISQUE",command=lambda:S.click(1500) )
    Bumper.place(x=60,y=200)

    WindowScreen=Button(canvas,padx=21,pady=16,bd=4, fg="black", font=('castellar', 10,'bold'),text="Window Screen",bg="BISQUE",command=lambda:S.click(2000) )
    WindowScreen.place(x=60,y=265)

    Tyre=Button(canvas,padx=69,pady=16,bd=4, fg="black", font=('castellar', 10 ,'bold'),text="Tyre",bg="BISQUE",command=lambda:S.click(1200))
    Tyre.place(x=60,y=330)

    Headlights=Button(canvas,padx=47,pady=16,bd=4, fg="black", font=('castellar', 10,'bold'),text="Headlights",bg="BISQUE", command=lambda: S.click(1000) )
    Headlights.place(x=260,y=265)

    Backlights=Button(canvas,padx=47,pady=16,bd=4, fg="black", font=('castellar', 10,'bold'),text="Backlights",bg="BISQUE", command=lambda: S.click(1000) )
    Backlights.place(x=260,y=330)

    SideMirror=Button(canvas,padx=48,pady=16,bd=4, fg="black", font=('castellar', 10 ,'bold'),text="SideMirror",bg="BISQUE", command=lambda: S.click(800))
    SideMirror.place(x=260,y=200)

    Silencer=Button(canvas,padx=50,pady=16,bd=4, fg="black", font=('castellar', 10 ,'bold'),text=" Silencer",bg="BISQUE", command=lambda: S.click(1600))
    Silencer.place(x=60,y=395)

    Engine=Button(canvas,padx=65,pady=16,bd=4, fg="black", font=('castellar', 10 ,'bold'),text=" Engine",bg="BISQUE", command=lambda:S.click('16000') )
    Engine.place(x=260,y=395)

    Addition=Button(canvas,padx=73.5,pady=4,bd=4, fg="black", font=('castellar', 20 ,'bold'),text="+",bg="BISQUE", command=lambda:S.click('+') )
    Addition.place(x=60,y=460)

    Equals=Button(canvas,padx=83,pady=4,bd=4, fg="black", font=('castellar', 20 ,'bold'),text="=",bg="BISQUE", command=S.equals)
    Equals.place(x=260,y=460)

    Clear=Button(canvas,padx=140,pady=4,bd=4, fg="black", font=('castellar', 20 ,'bold'),text="Clear", bg="BURLYWOOD",command=S.rdisplay)
    Clear.place(x=60,y=550)
    
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^CUSTOMER Data^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    label2 = Label(canvas, text="Enter Your Data:", font=('castellar',20,"bold"),bg="BISQUE",fg="black")
    label2.place(x=510,y=90)

    name = StringVar()
    phone = StringVar()
    company = StringVar()
    address = StringVar()
    email = StringVar()
    cnic = StringVar()

    NAme= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Name:",fg="white")
    NAme.place(x=510,y=150)
    Name = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=name,bd=3,bg="BURLYWOOD" ,justify='left')
    Name.place(x=550,y=185)


    PHone= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Contact No.:",fg="white")
    PHone.place(x=510,y=210)
    Phone = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=phone, bd=3,bg="BURLYWOOD" ,justify='left')
    Phone.place(x=550,y=245)


    COmpany= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Company:",fg="white")
    COmpany.place(x=510,y=270)
    Company = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=company,bd=3 ,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Company.place(x=550,y=305)

    ADdress= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Address:",fg="white")
    ADdress.place(x=510,y=330)
    Address = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=address,bd=3 ,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Address.place(x=550,y=365)

    EMail= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Email:",fg="white")
    EMail.place(x=510,y=390)
    Email = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=email,bd=3 ,insertwidth=4,bg="BURLYWOOD" ,justify='left')
    Email.place(x=550,y=425)

    CNic= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="CNIC:",fg="white")
    CNic.place(x=510,y=450)
    CNIC = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=cnic ,bd=3,insertwidth=4,bg="BURLYWOOD" ,justify='left')
    CNIC.place(x=550,y=485)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Vehicle Info^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

    label3 = Label(canvas, text="Vehicle Data:",bg="BISQUE", font=('castellar',20,"bold"),fg="black")
    label3.place(x=900,y=90)

    brand = StringVar()
    model = StringVar()
    modelyear = StringVar()
    registration = StringVar()
    engineID = StringVar()
    cartype = StringVar()

    BRand= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Brand:",fg="white")
    BRand.place(x=900,y=150)
    Brand = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=brand ,bd=3,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Brand.place(x=940,y=185)

    MOdel= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Model:",fg="white")
    MOdel.place(x=900,y=210)
    Model = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=model ,bd=3,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Model.place(x=940,y=245)

    MOdelyear= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Model Year:",fg="white")
    MOdelyear.place(x=900,y=270)
    Modelyear = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=modelyear,bd=3 ,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Modelyear.place(x=940,y=305)

    REgistration= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Reg. Number:",fg="white")
    REgistration.place(x=900,y=330)
    Registration = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=registration,bd=3,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Registration.place(x=940,y=365)

    ID= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Engine ID:",fg="white")
    ID.place(x=900,y=390)
    EngineID = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=engineID,bd=3 ,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    EngineID.place(x=940,y=425)

    Type= Label(canvas, font=( 'castellar' ,14, 'bold' ),bg="black",text="Car Type:",fg="white")
    Type.place(x=900,y=450)
    Cartype = Entry(canvas,width="30",font=('castellar' ,10,'bold'), textvariable=cartype,bd=3 ,insertwidth=7,bg="BURLYWOOD" ,justify='left')
    Cartype.place(x=940,y=485)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^BOTTOM buttons^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Reset=Button(canvas,padx=16,pady=8,fg="black",font=('castellar' ,11,'bold'),width=10, text="Reset", bd=3,bg="BISQUE",command=S.reset)
    Reset.place(x=552,y=570)

    Exit=Button(canvas,padx=16,pady=8,fg="black",font=('castellar' ,11,'bold'),width=10, text="Exit",bd=3, bg="BISQUE",command=S.qexit)
    Exit.place(x=1072,y=570)

    Rates=Button(canvas,padx=16,pady=8,fg="black",font=('castellar' ,11,'bold'),width=10, text="Rate List",bd=3, bg="BISQUE",command=S.RATE)
    Rates.place(x=899,y=570)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^SUBMIT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    sub=Button(canvas,padx=16.5,pady=8,fg="black",font=('castellar' ,11,'bold'),width=10, text="receipt",bd=3, bg="BISQUE",command=S.Receipt)
    sub.place(x=725,y=570)
    
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    canvas.place(x=-1.5, y=-2)
    root.mainloop()


##============================================================================================================================================================================================================================================================
##============================================================( TITLE )==================================================================================================================================================================================

def popup():
        pop = Tk()
        pop.geometry("1366x768+0+0")
        pop.title("Car Repairing And Management System")
        canvas = Canvas(pop, width = 1366, height = 768)
        bg_img = PhotoImage(file='D:\\2nd Sem\\Final CRMS\\i.gif')
        canvas.create_image(0, 0, anchor=NW, image= bg_img)
        def despop():
            pop.destroy()
            main()
        def exe():
            pop.destroy()
        proceed= Button(canvas,padx=16.5,pady=8,fg="WHITE",font=('castellar',11,'bold'),width=20,text='Proceed',bd=3,bg="black",command=despop)
        proceed.place(x=530,y=570)
        exi= Button(canvas,padx=16.5,pady=8,fg="WHITE",font=('castellar',11,'bold'),width=20,text='Exit',bd=3,bg="black",command=exe)
        exi.place(x=530,y=620)
        canvas.place(x=-1.5, y=-2)
        pop.mainloop()    
popup()

##===========================================================================================================================================================================================================================================================
##===========================================================================================================================================================================================================================================================
