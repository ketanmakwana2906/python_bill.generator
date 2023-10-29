from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")


        # variables
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        

        #category list
        self.Category=["select option","Prescription Medications","Health and Wellness","Medical Devices"]
        self.SubPreMedication =["Antibiotics","Blood Pressure","Diabetes"]
        self.Antibiotics = ["Amoxicillin","Azithromycin","Ciprofloxacin","Penicillin"]
        self.price_Amoxicillin=200
        self.price_Azithromycin=100
        self.price_Ciprofloxacin=50
        self.price_Penicillin=30

        self.Blood_Pressure = ["Lisinopril","Amlodipine","Metoprolol","Hydrochloro"]
        self.price_Lisinopril=100
        self.price_Amlodipine=50
        self.price_Metoprolol=40
        self.price_Hydrochlorothiazide=30

        self.Diabetes = ["Metformin","Insulin","Glipizide","Januvia"]
        self.price_Metformin=200
        self.price_Insulin=150
        self.price_Glipizide=100
        self.price_Januvia=50

        # health and welness

        self.SubHealthWell =["Vitamins and Supplements","First Aid","Personal Care"]
        self.SubVitamin =["Multivitamins","Vitamin D2","Omega-3","Probiotics"]
        self.price_Multivitamins=200
        self.price_VitaminD2=100
        self.price_OmegaFishOil=250
        self.price_Probiotics=300

        self.FirAid = ["Band-Aids","Antiseptic","Gauze Pads","Adhesive Tape"]
        self.price_BandAids=100
        self.price_AntisepticWipes=150
        self.price_GauzePads=40
        self.price_AdhesiveTape=80

        self.PerCare = ["Hand Sanitizer","Shampoo","Toothpaste","Sunscreen"]
        self.price_HandSanitizer=100
        self.price_Shampoo=150
        self.price_Toothpaste=100
        self.price_Sunscreen=50

        # medical device

        self.SubMedicalDevice =["Thermometers","Blood Glucose Monitors","Nebulizers"]
        self.SubThermometers =["Digital Oral","Infrared","Ear-Thermo.","Disposable"]
        self.price_DigitalOral=2000
        self.price_InfraredForhead=1000
        self.price_Ear=2500
        self.price_Disposable=500

        self.BloodMonitor = ["Accu-Chek","OneTouch Verio","Freestyle","Contour Next"]
        self.price_Accu=100
        self.price_OneTouch=200
        self.price_Free=300
        self.price_Contour=400

        self.Nebulizer = ["Philips","DeVilbiss","Medline","Omron MicroAir"]
        self.price_Philip=500
        self.price_Devilbee=400
        self.price_Medline=300
        self.price_Omron=200




        # image 1
        img1 = Image.open("image/1.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=500, height=130)

        # image 2
        img2 = Image.open("image/2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=500, y=0, width=500, height=130)

        # image 3
        img3 = Image.open("image/3.jpg")
        img3 = img3.resize((525, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=1000, y=0, width=525, height=130)

        lbl_title = Label(self.root, text="MEDICAL STORE - BILLING SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1530, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font=('times new roman',16,'bold'),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=175, width=1530, height=620)
           #customer label frame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=(
            "times new roman", 12, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, font=(
            "times new roman", 10, "bold"), width=24,textvariable=self.c_phone)
        self.entry_mob.grid(row=0, column=1)

        self.lbl_custName = Label(Cust_Frame, text="Customer Name", bd=4, font=(
            "arial", 12, "bold"), bg="white")
        self.lbl_custName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(
            Cust_Frame, font=("arial", 10, "bold"), width=24,textvariable=self.c_name)
        self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(Cust_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Email", bd=4)
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(
            Cust_Frame, font=("arial", 10, "bold"), width=24,textvariable=self.c_email)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # product frame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=5, width=620, height=140)
          
          #category
        self.lblCategory = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, font=(
            "arial", 10, "bold"), width=24, state="readonly",value=self.Category)
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #sub category

        self.lblSubCategory = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="SubCategory", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Combo_SubCategory = ttk.Combobox(Product_Frame, font=(
            "arial", 10, "bold"), width=24, state="readonly",value=[""])
        self.Combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # product name
        self.lblProduct = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Product Name", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Product = ttk.Combobox(Product_Frame, font=(
            "arial", 10, "bold"), width=24, state="readonly",textvariable=self.product)
        self.Combo_Product.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Product.bind("<<ComboboxSelected>>",self.price)

        # price
        self.lblPrice = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.Combo_Price = ttk.Combobox(Product_Frame, font=(
            "arial", 10, "bold"), width=24, state="readonly",textvariable=self.prices)
        self.Combo_Price.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # qty

        self.lblCategory = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Qty", bd=4)
        self.lblCategory.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.Combo_Qty = ttk.Entry(
            Product_Frame, font=("arial", 10, "bold"), width=26,textvariable=self.qty)
        self.Combo_Qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # middle frame

        Middle_Frame = Frame(Main_Frame, bd=10)
        Middle_Frame.place(x=10, y=150, width=980, height=340)

        # image 4
        img4 = Image.open("image/4.jpg")
        img4 = img4.resize((490, 340), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img4 = Label(Middle_Frame, image=self.photoimg4)
        lbl_img4.place(x=0, y=0, width=490, height=340)

        # image 5
        img5 = Image.open("image/5.jpg")
        img5 = img5.resize((490, 340), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbl_img5 = Label(Middle_Frame, image=self.photoimg5)
        lbl_img5.place(x=490, y=0, width=490, height=340)

        # search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1020, y=15, width=500, height=40)

        self.lblBill = Label(Search_Frame, font=(
            "arial", 12, "bold"), bg="red", fg="white", text="Bill Number")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.Entry_Search = ttk.Entry(
            Search_Frame, font=("arial", 10, "bold"), width=24,textvariable=self.search_bill)
        self.Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Button(Search_Frame, text="Search", font=(
            "arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.find_bill)
        self.BtnSearch.grid(row=0, column=2)

        # right bill area

        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Area", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=1000, y=45, width=480, height=440)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set,
                             bg="white", fg="blue", font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # bill counter frame
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        Bottom_Frame.place(x=0, y=485, width=1520, height=125)

        # sub total
        self.lblSubTotal = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(
            Bottom_Frame, font=("arial", 10, "bold"), width=26,textvariable=self.sub_total)
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        # govt tax
        self.lblTax = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Govt tax", bd=4)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Txt_Tax = ttk.Entry(
            Bottom_Frame, font=("arial", 10, "bold"), width=26,textvariable=self.tax_input)
        self.Txt_Tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        # total amount
        self.lblTotalAmount = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Total", bd=4)
        self.lblTotalAmount.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_amount = ttk.Entry(
            Bottom_Frame, font=("arial", 10, "bold"), width=26,textvariable=self.total)
        self.txt_amount.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # button frame

        Btn_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart = Button(Btn_Frame, height=2, text="Add To Cart", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.AddItem)
        self.BtnAddToCart.grid(row=0, column=0)

        self.BtnGenerateBill = Button(Btn_Frame, height=2, text="Generate Bill", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.gen_bill)
        self.BtnGenerateBill.grid(row=0, column=1)

        self.BtnSaveBill = Button(Btn_Frame, height=2, text="Save Bill", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.save_bill)
        self.BtnSaveBill.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame, height=2, text="Print", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.iprint)
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame, height=2, text="Clear", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.clear)
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame, height=2, text="Exit", font=(
            "arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2",command=self.root.destroy)
        self.BtnExit.grid(row=0, column=5)

        self.root.bind("<Control-+>", lambda event: self.AddItem())
        self.root.bind("<Control-Return>", lambda event: self.gen_bill())
        self.root.bind("<Control-s>", lambda event: self.save_bill())
        self.root.bind("<Control-p>", lambda event: self.iprint())
        self.root.bind("<Control-Delete>", lambda event: self.clear())
        self.root.bind("<Control-w>", lambda event: self.root.destroy())
        

        self.welcome()
        self.l = []
      # add item
    def AddItem(self):
        Tax =1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        sub_total = sum(self.l)
        tax = 0.03 * sub_total
        total = sub_total + tax
        if self.product.get()=="":
            messagebox.showerror("Error","please select the product name")
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t\t{self.qty.get()}\t{self.m}")
            self.sub_total.set(f'Rs.{sub_total:.2f}')
            self.tax_input.set(f'Rs.{tax:.2f}')
            self.total.set(f'Rs.{total:.2f}')   





    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Hindustan medical store Bhavnagar \n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone No. : {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email : {self.c_email.get()}")

        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\tPrice")
        self.textarea.insert(END,"\n==================================================")

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","please add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,"\n" +text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")

    def save_bill(self):
            op = messagebox.askyesno("Save Bill","Do you want to save the bill")
            if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
                f1.write(self.bill_data)
                op = messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} saved successfully")
                f1.close()

    def iprint(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.search_bill.get():
                f1 = open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close
                found="yes"
        if found=="no":
                messagebox.showerror("Error","invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


            




    def Categories(self,event=""):
        if self.Combo_Category.get()=="Prescription Medications":
            self.Combo_SubCategory.config(value=self.SubPreMedication)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Health and Wellness":
            self.Combo_SubCategory.config(value=self.SubHealthWell)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Medical Devices":
            self.Combo_SubCategory.config(value=self.SubMedicalDevice)
            self.Combo_SubCategory.current(0)

    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Antibiotics":
            self.Combo_Product.config(value=self.Antibiotics)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Blood Pressure":
            self.Combo_Product.config(value=self.Blood_Pressure)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Diabetes":
            self.Combo_Product.config(value=self.Diabetes)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Vitamins and Supplements":
            self.Combo_Product.config(value=self.SubVitamin)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="First Aid":
            self.Combo_Product.config(value=self.FirAid)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Personal Care":
            self.Combo_Product.config(value=self.PerCare)
            self.Combo_Product.current(0)
        
        if self.Combo_SubCategory.get()=="Thermometers":
            self.Combo_Product.config(value=self.SubThermometers)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Blood Glucose Monitors":
            self.Combo_Product.config(value=self.BloodMonitor)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Nebulizers":
            self.Combo_Product.config(value=self.Nebulizer)
            self.Combo_Product.current(0)
    def price(self,event=""):
        if self.Combo_Product.get()=="Amoxicillin":
            self.Combo_Price.config(value=self.price_Amoxicillin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Azithromycin":
            self.Combo_Price.config(value=self.price_Azithromycin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Ciprofloxacin":
            self.Combo_Price.config(value=self.price_Ciprofloxacin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Penicillin":
            self.Combo_Price.config(value=self.price_Penicillin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Lisinopril":
            self.Combo_Price.config(value=self.price_Lisinopril)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Amlodipine":
            self.Combo_Price.config(value=self.price_Amlodipine)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Metoprolol":
            self.Combo_Price.config(value=self.price_Metoprolol)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Hydrochloro":
            self.Combo_Price.config(value=self.price_Hydrochlorothiazide)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Metformin":
            self.Combo_Price.config(value=self.price_Metformin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Insulin":
            self.Combo_Price.config(value=self.price_Insulin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Glipizide":
            self.Combo_Price.config(value=self.price_Glipizide)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Januvia":
            self.Combo_Price.config(value=self.price_Januvia)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Multivitamins":
            self.Combo_Price.config(value=self.price_Multivitamins)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Vitamin D2":
            self.Combo_Price.config(value=self.price_VitaminD2)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Omega-3":
            self.Combo_Price.config(value=self.price_OmegaFishOil)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Probiotics":
            self.Combo_Price.config(value=self.price_Probiotics)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Band-Aids":
            self.Combo_Price.config(value=self.price_BandAids)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Antiseptic":
            self.Combo_Price.config(value=self.price_AntisepticWipes)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Gauze Pads":
            self.Combo_Price.config(value=self.price_GauzePads)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Adhesive Tape":
            self.Combo_Price.config(value=self.price_AdhesiveTape)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="Hand Sanitizer":
            self.Combo_Price.config(value=self.price_HandSanitizer)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Shampoo":
            self.Combo_Price.config(value=self.price_Shampoo)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="Toothpaste":
            self.Combo_Price.config(value=self.price_Toothpaste)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Sunscreen":
            self.Combo_Price.config(value=self.price_Sunscreen)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Digital Oral":
            self.Combo_Price.config(value=self.price_DigitalOral)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Infrared":
            self.Combo_Price.config(value=self.price_InfraredForhead)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Ear-Thermo.":
            self.Combo_Price.config(value=self.price_Ear)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Disposable":
            self.Combo_Price.config(value=self.price_Disposable)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Accu-Chek":
            self.Combo_Price.config(value=self.price_Accu)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="OneTouch Verio":
            self.Combo_Price.config(value=self.price_OneTouch)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Freestyle":
            self.Combo_Price.config(value=self.price_Free)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Contour Next":
            self.Combo_Price.config(value=self.price_Contour)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Philips":
            self.Combo_Price.config(value=self.price_Philip)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="DeVilbiss":
            self.Combo_Price.config(value=self.price_Devilbee)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Medline":
            self.Combo_Price.config(value=self.price_Medline)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Omron MicroAir":
            self.Combo_Price.config(value=self.price_Omron)
            self.Combo_Price.current(0)
            self.qty.set(1)

      


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
