from tkinter import*
from PIL import Image,ImageTk #pip install pillow
import time
import sqlite3
import os
from tkinter import messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product  import Productclass
from sales import salesClass
from billing import BillClass
class FSC:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Factory Stock Checking & Billing System")
        self.root.config(bg="#F9F5B0")
        #===title===
        self.icon_title=PhotoImage(file="")
        title=Label(self.root,text="Factory Stock Checking & Billing System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="yellow",fg="#010c48",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #===clock===
        self.lbl_clock=Label(self.root,text="Factory Stock Checking & Billing System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left Menu===
        

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        

        btn_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_bill=Button(LeftMenu,text="Generate Bill",command=self.billing,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


     #===Content===

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=90,width=1000)

        self.lbl_supplier=Label(self.root,text="Total Customer\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=300,y=220,height=90,width=1000)

        self.lbl_category=Label(self.root,text="Total Connection\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=300,y=320,height=90,width=1000)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=420,height=90,width=1000)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=300,y=520,height=90,width=1000)
        
        #===footer===
        lbl_footer=Label(self.root,text="FSC-Factory Stock Checking & Billing System",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
     
        self.update_content()
    #==========================================================================================================
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
        
    def supplier(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=supplierClass(self.new_win)    
        
    def category(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=categoryClass(self.new_win) 
       
    def product(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=Productclass(self.new_win)       
        
    def sales(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=salesClass(self.new_win) 

    def billing(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=BillClass(self.new_win)   

    def update_content(self):
        con=sqlite3.connect(database=r'fsc.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]")

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Categories\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employees\n[ {str(len(employee))} ]")

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill)} ]")

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Factory Stock Checking & Billing System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def exit(self):
        self.root.destroy()  

    def logout(self):
        self.root.destroy()
        os.system("python login.py")     

                
if __name__ =="__main__":
    root=Tk()
    obj=FSC(root)
    root.mainloop()