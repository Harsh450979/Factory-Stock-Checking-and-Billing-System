from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class Productclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Factory Stock Checking & Billing System")
        self.root.config(bg="#F9F5B0")
        self.root.focus_force()
        #=================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
       
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        #=====title=====
        
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="yellow",fg="#010c48").pack(side=TOP,fill=X)
    
      #======column1
        lbl_Category=Label(product_Frame,text="Category",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_Supplier=Label(product_Frame,text="Supplier",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_Price=Label(product_Frame,text="Price",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_Status=Label(product_Frame,text="Status",font=("goudy old style",15),bg="white").place(x=30,y=310)
        
         #======column2
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)
        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
        
       
        #===buttons===
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
     #====searchfram====
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
      #====options===
        cmb_search=ttk.Combobox (SearchFrame,textvariable=self.var_searchby,values=("select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_Search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_Search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
     #=========product detels
        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.productTable=ttk.Treeview(p_frame,columns=("pid","supp","cat","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="Product ID")
        self.productTable.heading("cat",text="Category")
        self.productTable.heading("supp",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=90)
        self.productTable.column("cat",width=100)
        self.productTable.column("supp",width=100)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)
       
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
    #============================================================================================================
    
    def fetch_cat_sup(self):
      self.cat_list.append("Empty")
      self.sup_list.append("Empty")
      con=sqlite3.connect(database=r'fsc.db')
      cur=con.cursor()
      try: 
        cur.execute("Select name from Category")
        cat=cur.fetchall()
       
        if len(cat)>0:
           del self.cat_list[:]
           self.cat_list.append("Select")
           for i in cat:
               self.cat_list.append(i[0])
        
        cur.execute("Select name from Supplier")
        sup=cur.fetchall()
        if len(sup)>0:

           del self.sup_list[:]
           self.sup_list.append("Select")
           for i in sup:
               self.sup_list.append(i[0])
        
       
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    
    
    def add(self): 
      con=sqlite3.connect(database=r'fsc.db')
      cur=con.cursor()    
      try:
          if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select"or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are be required",parent=self.root)
          else:
            cur.execute("Select * from product where name=?",(self.var_name.get(),))
            row=cur.fetchone()
            if row!=None:
              messagebox.showerror("Error","Product already present,try different",parent=self.root)
            else:
                cur.execute("Insert into product (cat,supp,name,price,qty,status) values(?,?,?,?,?,?)",(
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    
                                    ))
                con.commit()
                messagebox.showinfo("Success","Product Addedd Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
        
    def show(self):
      con=sqlite3.connect(database=r'fsc.db')
      cur=con.cursor()
      try:
        cur.execute("select * from product")
        rows=cur.fetchall()
        self.productTable.delete(*self.productTable.get_children())
        for row in rows:
          self.productTable.insert('',END,values=row)
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values'] 
        self.var_pid.set(row[0]),
        self.var_sup.set(row[1]),
        self.var_cat.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
        
    def update(self): 
      con=sqlite3.connect(database=r'fsc.db')
      cur=con.cursor()
      try:
          if self.var_pid.get()=="":
            messagebox.showerror("Error","Please select product from list",parent=self.root)
          else:
            cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide Product",parent=self.root)
            else:
                cur.execute("Update product set cat=?,supp=?,name=?,price=?,qty=?,status=? where pid=?",(
                                    
                                    self.var_cat.get(),
                                    self.var_sup.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    self.var_pid.get()
                ))
                con.commit()
                messagebox.showinfo("Success","product updated Successfully",parent=self.root)
                self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
         
    
    def delete(self):
      con=sqlite3.connect(database=r'fsc.db')
      cur=con.cursor()
      try:
          if self.var_pid.get()=="":
            messagebox.showerror("Error","Select Product from the list",parent=self.root)
          else:
            cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
            row=cur.fetchone()
            if row==None:
              messagebox.showerror("Error","Invalide product",parent=self.root)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                if op==True:
                   cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                   con.commit()
                   messagebox.showinfo("Delete","Product Delete successfully",parent=self.root)
                   self.clear()
        
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),
        self.var_searchtxt.set(""),
        self.var_searchby.set("Select"),
        self.show()
        
        
                                     
    
    def search(self):
        con=sqlite3.connect(database=r'fsc.db')
        cur=con.cursor()
        try:
          if self.var_searchby.get()=="Select":
            messagebox.showerror("Error","Select Search By option",parent=self.root)
          elif self.var_searchtxt.get()=="":  
           messagebox.showerror("Error","Search input should be required",parent=self.root)
          else:
              cur.execute("select * from product Where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                 self.productTable.delete(*self.productTable.get_children())
                 for row in rows:
                    self.productTable.insert('',END,values=row)
              else:
                messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          
    
         
if __name__ =="__main__":
    root=Tk()
    obj=Productclass(root)
    root.mainloop()
