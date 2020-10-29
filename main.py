from tkinter import *
import csv

root = Tk()

#Labels
admiL = Label(root,text="Admission Number")
nameL = Label(root,text="Name")
fatherL = Label(root,text="Father Name")
mobileL = Label(root,text="Mobile Number")
emailL = Label(root,text="Email ID")
desgAddL = Label(root,text="Designation-Address of Organisation")
perAddL = Label(root,text="Permanent Address")
preAddL = Label(root,text="Present Address")

#Input fields
admi = Entry(root)
name = Entry(root)
father = Entry(root)
mobile = Entry(root)
email = Entry(root)
desgAdd = Entry(root)
perAdd = Entry(root)
preAdd = Entry(root)


#grid layout arrangment
admiL.grid(row=0,sticky=W)
nameL.grid(row=1,sticky=W)
fatherL.grid(row=2,sticky=W)
mobileL.grid(row=3,sticky=W)
emailL.grid(row=4,sticky=W)
desgAddL.grid(row=5,sticky=W)
perAddL.grid(row=6,sticky=W)
preAddL.grid(row=7,sticky=W)


admi.grid(row=0,column=1,pady=10)
name.grid(row=1,column=1,pady=10)
father.grid(row=2,column=1,pady=10)
mobile.grid(row=3,column=1,pady=10)
email.grid(row=4,column=1,pady=10)
desgAdd.grid(row=5,column=1,pady=10)
perAdd.grid(row=6,column=1,pady=10)
preAdd.grid(row=7,column=1,pady=10)

digital.grid(row=8,column=2,pady=10)
rounded.grid(row=9,column=2,pady=10)
leveler.grid(row=10,column=2,pady=10)
metter.grid(row=8,column=2,pady=10)
brick.grid(row=9,column=2,pady=10)
honda.grid(row=10,column=2,pady=10)

def showdata():
    with open('personnel.csv','w') as csvfile:
        filewriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Addmission Number',admi.get()])
        filewriter.writerow(['Name',name.get()])
        filewriter.writerow(['Father Name',father.get()])
        filewriter.writerow(['Mobile Number',mobile.get()])
        filewriter.writerow(['Email ID',email.get()])
        filewriter.writerow(['Designation-Address of Organisation',desgAdd.get()])
        filewriter.writerow(['Permanent Address',perAdd.get()])
        filewriter.writerow(['Present Address',preAdd.get()])
    

saveBtn = Button(text="Save Data",command=showdata)
saveBtn.grid(row=8,columnspan=2,ipady=5,ipadx=8,pady=10)

root.mainloop()


