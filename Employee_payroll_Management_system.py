from tkinter import *
from tkinter import messagebox
import pymysql
import time
import os

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1420x750+2+2")
        title=Label(self.root,text="Employee Payroll Management System ",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        #================ Frame1 ===========================#
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_experience = StringVar()
        self.var_proof_id = StringVar()#==Adhaar Card ==#
        self.var_contact = StringVar()


        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=760,height=630)

        title2=Label(Frame1,text="Employee Details",font=("times new roman",30,"bold"),bg="green",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_employee_code=Entry(Frame1,font=("times new roman",17),textvariable=self.var_emp_code,bg="lightyellow",fg="black").place(x=200,y=75,width=200)

        # search_button = Button(Frame1, text="Search",font=("times new roman",15),command=self.search,bg="white",fg="black").place(x=480,y=70)


        #=========Row1
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",15),bg="white",fg="black").place(x=20,y=130)
        txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=160,y=130,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",15),bg="white",fg="black").place(x=390,y=130)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=500,y=130)


        #=========Row2
        lbl_name=Label(Frame1,text="Name",font=("times new roman",15),bg="white",fg="black").place(x=20,y=180)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=160,y=180,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",15),bg="white",fg="black").place(x=390,y=180)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=500,y=180)

        #=========Row3
        lbl_age=Label(Frame1,text="Age",font=("times new roman",15),bg="white",fg="black").place(x=20,y=230)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=160,y=230,width=200)
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",15),bg="white",fg="black").place(x=390,y=230)
        txt_exp=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=500,y=230)

        #=========Row4
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",15),bg="white",fg="black").place(x=20,y=280)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=160,y=280,width=200)
        lbl_proof=Label(Frame1,text="Proof ID:",font=("times new roman",15),bg="white",fg="black").place(x=390,y=280)
        txt_proof=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=500,y=280)

        #=========Row5
        lbl_email=Label(Frame1,text="Email:",font=("times new roman",15),bg="white",fg="black").place(x=20,y=330)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=160,y=330,width=200)
        lbl_contact=Label(Frame1,text="Contact no:",font=("times new roman",15),bg="white",fg="black").place(x=390,y=330)
        txt_contact=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=500,y=330)

        #=========Row6
        lbl_Address=Label(Frame1,text="Address:",font=("times new roman",15),bg="white",fg="black").place(x=20,y=400)
        self.txt_address=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=160,y=400,width=500,height=200)

        # ================ Frame2 ===========================#

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_basic_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()


        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=639,height=350)

        title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",30,"bold"),bg="green",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        #=========Row1
        lbl_month=Label(Frame2,text="Month",font=("times new roman",15),bg="white",fg="black").place(x=20,y=70)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=90,y=70,width=100)
        lbl_year=Label(Frame2,text="Year:",font=("times new roman",15),bg="white",fg="black").place(x=200,y=70)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=270,y=70,width=100)
        lbl_bs=Label(Frame2,text="Basic Salary",font=("times new roman",15),bg="white",fg="black").place(x=390,y=70)
        txt_bs=Entry(Frame2,font=("times new roman",15),textvariable=self.var_basic_salary,bg="lightyellow",fg="black").place(x=520,y=70,width=100)

        #=========Row2
        lbl_total_days=Label(Frame2,text="Total_days:",font=("times new roman",15),bg="white",fg="black").place(x=20,y=120)
        txt_t_days=Entry(Frame2,font=("times new roman",15),textvariable=self.var_t_days,bg="lightyellow",fg="black").place(x=160,y=120,width=100)
        lbl_Absents=Label(Frame2,text="Absents:",font=("times new roman",15),bg="white",fg="black").place(x=300,y=120)
        txt_absents=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=450,y=120,width=100)

        #=========Row3
        lbl_medical=Label(Frame2,text="Medical",font=("times new roman",15),bg="white",fg="black").place(x=20,y=170)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=160,y=170,width=100)
        lbl_Provident_fund=Label(Frame2,text="Provident Fund:",font=("times new roman",15),bg="white",fg="black").place(x=300,y=170)
        txt_pf=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=450,y=170,width=100)

        #=========Row4
        lbl_Convence=Label(Frame2,text="Convence:",font=("times new roman",15),bg="white",fg="black").place(x=20,y=220)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=160,y=220,width=100)
        lbl_net_salary=Label(Frame2,text="Net Salary:",font=("times new roman",15),bg="white",fg="black").place(x=300,y=220)
        txt_net_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_net_salary,bg="lightyellow",fg="black").place(x=450,y=220,width=100)

        calculate_button = Button(Frame2, text="Calculate",command = self.calculate,font=("times new roman",15),bg="orange",fg="black").place(x=180,y=255)
        save_button = Button(Frame2, text="Save",command=self.add,font=("times new roman",15),bg="blue",fg="black").place(x=300,y=255)
        clear_button = Button(Frame2, text="Clear",command=self.clear,font=("times new roman",15),bg="gray",fg="black").place(x=380,y=255)

        save_button = Button(Frame2, text="Update",command = self.update,font=("times new roman",15),bg="green",fg="black").place(x=180,y=300,width=100)
        save_button = Button(Frame2, text="Delete",command=self.delete,font=("times new roman",15),bg="Red",fg="black").place(x=300,y=300,width=100)

        # ================ Frame3 ===========================#
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=420,width=640,height=280)

        Cal_Frame=Frame(Frame3,bd=3,relief=RIDGE,bg="white")
        Cal_Frame.place(x=2, y=2, width=285, height=280)

        #=================Calculate here
        self.var_txt=StringVar()
        self.var_receipt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def clear_cal():
            self.var_txt.set('')
            self.var_operator= ''

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        txt_result=Entry(Cal_Frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",15,"bold"),justify=RIGHT)
        txt_result.place(x=0, y=0,relwidth=1, height=30)

        btn_7=Button(Cal_Frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=29,w=70,h=60)
        btn_8=Button(Cal_Frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=70,y=29,w=70,h=60)
        btn_9=Button(Cal_Frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=140,y=29,w=70,h=60)
        btn_div=Button(Cal_Frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=210,y=29,w=70,h=60)

        btn_4=Button(Cal_Frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=90,w=70,h=60)
        btn_5=Button(Cal_Frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=70,y=90,w=70,h=60)
        btn_6=Button(Cal_Frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=140,y=90,w=70,h=60)
        btn_multi=Button(Cal_Frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=210,y=90,w=70,h=60)

        btn_1=Button(Cal_Frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=151,w=70,h=60)
        btn_2=Button(Cal_Frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=70,y=151,w=70,h=60)
        btn_3=Button(Cal_Frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=140,y=151,w=70,h=60)
        btn_minus=Button(Cal_Frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=210,y=151,w=70,h=60)
        #
        btn_0=Button(Cal_Frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=212,w=70,h=60)
        btn_dot=Button(Cal_Frame,text="C",command=clear_cal,font=("times new roman",15,"bold")).place(x=70,y=212,w=70,h=60)
        btn_add=Button(Cal_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=140,y=212,w=70,h=60)
        btn_equal=Button(Cal_Frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=210,y=212,w=70,h=60)

        #=================Sal Frame
        sal_Frame=Frame(Frame3,bd=3,relief=RIDGE,bg="white")
        sal_Frame.place(x=288, y=2, width=346, height=273)
        title_sal=Label(sal_Frame,text="Salary Reciept",font=("times new roman",20),bg="green",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=200)
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_Frame2,font=("times new roman",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)

        calculate_button = Button(sal_Frame, text="Print", font=("times new roman", 15), bg="orange", fg="black").place(x=210, y=230,width=120)
        self.txt_salary_reciept.delete('1.0',END)

        try:
            total_present = int(self.var_t_days.get()) - int(self.var_absent.get())
        except ValueError:
            total_present = 0

#         new_sample = f'''\tCompany Name, XYZ\n\tAddress: XYZ, Floor4
# ----------------------------------------------------
# Employee ID\t\t:  {self.var_emp_code.get()}
# Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
# Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
# ----------------------------------------------------
# Total Days\t\t:  {self.var_t_days.get()}
# Total Present\t\t:  {total_present}
# Total_Absent\t\t:  {self.var_absent.get()}
# Canvence\t\t:  Rs.{self.var_convence.get()}
# Medical\t\t:  Rs.{self.var_medical.get()}
# PF\t\t:  Rs.{self.var_pf.get()}
# Gross Payment\t\t:  Rs.{self.var_basic_salary.get()}
# Net_salary\t\t:  Rs.{self.var_net_salary.get()}
# ----------------------------------------------------
# This is computer generated slip, not
# required any signature
# '''
#
#         self.txt_salary_reciept.delete('1.0',END)
#         self.txt_salary_reciept.insert(END,new_sample)

        self.check_connection()


#========================All Functions start============================================#

    def clear(self):
        self.var_month.set('')
        self.var_year.set('')
        self.var_basic_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.var_txt.set('')
        self.var_operator = ''
        self.txt_salary_reciept.delete('1.0', END)

    def update(self):
        if (
                self.var_month.get() == ''
                or self.var_year.get() == ''
                or self.var_t_days.get() == ''
                or self.var_absent.get() == ''
                or self.var_pf.get() == ''
                or self.var_medical.get() == ''
                or self.var_designation.get() == ''
                or self.var_doj.get() == ''
                or self.var_dob.get() == ''
                or self.var_age.get() == ''
                or self.var_email.get() == ''
                or self.var_gender.get() == ''
                or self.var_contact.get() == ''
                or self.var_proof_id.get() == ''
        ):
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='employee management system')
                cur = con.cursor()

                # Execute the update query
                cur.execute("UPDATE emp_salary SET designation=%s, name=%s, age=%s, gender=%s, email=%s, "
                            "doj=%s, dob=%s, experience=%s, proof_id=%s, address=%s, contact=%s, "
                            "month=%s, year=%s, basic_salary=%s, receipt=%s, t_days=%s, absent=%s, "
                            "medical=%s, pf=%s, convence=%s, net_salary=%s WHERE e_id=%s",
                            (
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.txt_address.get(),
                                self.var_contact.get(),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_basic_salary.get(),
                                self.var_receipt.get(),
                                self.var_t_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get(),
                            )
                            )

                con.commit()
                con.close()

                # Save the updated salary receipt
                file_path = "Salary_reciept/" + str(self.var_emp_code.get()) + ".txt"
                with open(file_path, 'w') as file_:
                    file_.write(self.txt_salary_reciept.get('1.0', END))

                messagebox.showinfo("Success", "Record Updated Successfully")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def delete(self):
        if self.var_emp_code.get() == '':
            messagebox.showerror('Error', 'Please enter the Employee Code to delete the record')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='employee management system')
                cur = con.cursor()

                # Execute the delete query
                cur.execute("DELETE FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get(),))

                con.commit()
                con.close()

                # Delete the salary receipt file
                file_path = "Salary_reciept/" + str(self.var_emp_code.get()) + ".txt"
                if os.path.exists(file_path):
                    os.remove(file_path)

                messagebox.showinfo("Success", "Record Deleted Successfully")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    # def search(self):
    #     try:
    #         con = pymysql.connect(host='localhost', user='root', password='', db='employee management system')
    #         cur = con.cursor()
    #         cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
    #         row = cur.fetchone()
    #         if row == None:
    #             messagebox.showerror("Error", "Invalid Employee ID, please try another ID",
    #                                  parent=self.root)
    #         else:
    #             print(row)
    #             self.var_emp_code.set(row[0])
    #             self.var_designation.set(row[1])
    #             self.var_name.set(row[2])
    #             self.var_age.set(row[3])
    #             self.var_gender.set(row[4])
    #             self.var_email.set(row[5])
    #             self.var_doj.set(row[6])
    #             self.var_dob.set(row[7])
    #             self.var_experience.set(row[8])
    #             self.var_proof_id.set(row[9])
    #             self.var_contact.set(row[10])
    #             # self.txt_address.delete('1.0',END)
    #             self.txt_address.insert(END,row[11])
    #             self.var_month.set(row[12])
    #             self.var_year.set(row[13])
    #             self.var_basic_salary.set(row[14])
    #             self.var_receipt.set(row[15])
    #             self.var_t_days.set(row[16])
    #             self.var_absent.set(row[17])
    #             self.var_medical.set(row[18])
    #             self.var_pf.set(row[19])
    #             self.var_convence.set(row[20])
    #             self.var_net_salary.set(row[21])
    #             # file_=open("Salary_reciept/"+str(row[22]),'r')
    #             # self.txt_salary_reciept.delete('1.0',END)
    #             # for i in file_:
    #             # file_.close()
    #         file_path = "Salary_reciept/" + str(row[22])
    #         print("File path:", file_path)
    #
    #         self.txt_salary_reciept.delete('1.0',END)
    #         if os.path.exists(file_path):
    #             print("File exists.")
    #             with open(file_path, 'r') as file_:
    #                 self.txt_salary_reciept.delete('1.0', END)
    #                 for line in file_:
    #                     self.txt_salary_reciept.insert(END, line)
    #         else:
    #             self.txt_salary_reciept.delete('1.0', END)
    #             self.txt_salary_reciept.insert(END, "Salary receipt not found for this employee.")
    #
    #     except Exception as ex:
    #         messagebox.showerror("Error", f'error due to: {str(ex)}')

    def add(self):
        if (
                self.var_month.get()==''
                or self.var_year.get()==''
                or self.var_t_days.get()==''
                or self.var_absent.get()==''
                or self.var_pf.get()==''
                or self.var_medical.get()==''
                or self.var_designation.get()==''
                or self.var_doj.get()==''
                or self.var_dob.get()==''
                or self.var_age.get()==''
                or self.var_email.get()==''
                or self.var_gender.get()==''
                or self.var_contact.get()==''
                or self.var_proof_id.get()==''

        ):
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='employee management system')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID has already available in our record, try another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary (e_id, designation, name, age, gender, email, doj, dob, experience, "
                            "proof_id, address, contact, month, year, basic_salary, t_days, absent, medical, pf, "
                            "convence, net_salary, receipt) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.txt_address.get(),


                        self.var_contact.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_basic_salary.get(),
                        self.var_receipt.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),

                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_reciept.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully")

            except Exception as ex:
                messagebox.showerror("Error",f'error due to: {str(ex)}')

    def calculate(self):


        if (
                self.var_month.get()==''
                or self.var_year.get()==''
                or self.var_t_days.get()==''
                or self.var_absent.get()==''
                or self.var_pf.get()==''
                or self.var_medical.get()==''
                or self.var_designation.get()==''
                or self.var_doj.get()==''
                or self.var_dob.get()==''
                or self.var_age.get()==''
                or self.var_email.get()==''
                or self.var_gender.get()==''
                or self.var_contact.get()==''
                or self.var_proof_id.get()==''

        ):
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                per_day=int(self.var_basic_salary.get())/int(self.var_t_days.get())
                work_day=int(self.var_t_days.get())-int(self.var_absent.get())
                sal_=per_day*work_day
                net_sal=sal_-int(self.var_medical.get())+int(self.var_convence.get())
                self.var_net_salary.set(str(round(net_sal,2)))
                # Update the salary receipt text widget
                total_present = int(self.var_t_days.get()) - int(self.var_absent.get())

                new_sample = f'''\tCompany Name, XYZ\n\tAddress: XYZ, Floor4
----------------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary Of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
----------------------------------------------------
Total Days\t\t:  {self.var_t_days.get()}
Total Present\t\t:  {total_present}
Total_Absent\t\t:  {self.var_absent.get()}
Canvence\t\t:  Rs.{self.var_convence.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_basic_salary.get()}
Net_salary\t\t:  Rs.{self.var_net_salary.get()}
----------------------------------------------------
This is a computer-generated slip,
not required any signature
'''

                self.txt_salary_reciept.delete('1.0', END)
                self.txt_salary_reciept.insert(END, new_sample)

            except Exception as ex:
                messagebox.showerror("Error", f'error due to: {str(ex)}')

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='employee management system')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

root=Tk()
obj=EmployeeSystem(root)
root.mainloop()