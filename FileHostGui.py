#!/bin/python3

from tkinter import *
import os


File_directory="/etc/"
File_name     ="hosts"

class test():
    def __init__(self,scrol):
        global File_directory
        global File_name
        ############## Screen print for Actuel configuration ############
        ecr=Text(frame2_1,yscrollcommand=scrol.set, height=35)
        
        self.ecr=ecr
        self.ecr.pack()
        
        scrol.config(command=self.ecr.yview)
        
    ################  read file ##################    
    def reads(self):
        os.chdir(File_directory)
        self.ecr.delete(END)
        i=0
        fichier=open(File_name, 'r')
        ligne=fichier.readlines()
        
        
        for lettre in ligne:
            self.ecr.insert(END,str(i)+"-- "+ ligne[i])
            i=i+1
            
        fichier.close()
        self.ecr.config(state="disabled")
    ################ write file #################    
    def writes(self,ipv, nameh):
        self.ecr.config(state="normal")
        print("valider")
    
        fichier=open(File_name, 'a')
        fichier.writelines(str(ipv)+"         "+str(nameh)+"\n")
    
        fichier.close()
        self.ecr.delete(1.0, "end")
        self.ecr.delete(END)
        i=0
        fichier=open(File_name, 'r')
        ligne=fichier.readlines()
        
        for lettre in ligne:
            self.ecr.insert(END,str(i)+"-- "+ligne[i])
            i=i+1
            
        fichier.close()
        self.ecr.config(state="disabled")
    ############# modify file ###############
      
    def modify(self, line_num):
        fichier=open(File_name,'r')
        line=fichier.readlines()
        ints=int(line_num)
        del(line[ints]) 
        fichier.close()
        # #### update of /etc/hosts file
        fichier=open(File_name,'w')
        fichier.writelines(line)
        
        fichier.close()
        self.ecr.config(state="normal")
        
        self.ecr.delete(1.0, "end")
        self.ecr.delete(END)
        ##########################################
        i=0
        fichier=open(File_name, 'r')
        ligne=fichier.readlines()
        
        
        for lettre in ligne:
            self.ecr.insert(END,str(i)+"-- "+ligne[i])
            i=i+1
            
        fichier.close()
        self.ecr.config(state="disabled")
        
        
       
        
        
        
        
    


app=Tk()
app.geometry("1200x700")
app.config(background="gray")
app.title("FileHostGui")



frame1=Frame(app, background="gray", width=800, height=800)
Label(frame1, text="this programme able to help you to configure /etc/hosts file in GUI",font=("Arial", 16), background="gray", fg="white").pack()


############### IPV 4 configuration ###################
frame1_1=Frame(frame1, width=800, height=200, background="gray")

ip4Configure=Label(frame1_1, text="IPv 4 configuration and host", background="gray", font=("Arial", 12), fg="white")
ip4Configure.place(x=300, y=12)

ipv4=Label(frame1_1, text="IPV 4 address :", font=("Arial",12), background="gray", fg="white")
ipv4.place(x=10, y=50)
ip4value=Entry(frame1_1, font=("Arial", 14))
ip4value.place(x=150,y=50)

dns_name_4=Label(frame1_1, text="dns_name :", font=("Arial",12), background="gray", fg="white")
dns_name_4.place(x=450, y=50)
dns_4_value=Entry(frame1_1, font=("Arial", 14))
dns_4_value.place(x=550,y=50)


frame1_1.pack()

########## IPV 6 configuration ####################

frame1_2=Frame(frame1, width=800, height=500, background="gray")

ip4Configure=Label(frame1_2, text="IPv 6 configuration and host", background="gray", font=("Arial", 12), fg="white")
ip4Configure.place(x=300, y=12)

ipv6=Label(frame1_2, text="IPV 6 address :", font=("Arial",12), background="gray", fg="white")
ipv6.place(x=10, y=50)
ip6value=Entry(frame1_2, font=("Arial", 14))
ip6value.place(x=150,y=50)

dns_name_6=Label(frame1_2, text="dns_name :", font=("Arial",12), background="gray", fg="white")
dns_name_6.place(x=450, y=50)
dns_6_value=Entry(frame1_2, font=("Arial", 14))
dns_6_value.place(x=550,y=50)

frame1_2.pack()
frame1.pack(side=LEFT)


frame2=Frame()


frame2_1=Frame(background="gray")

################# scroll #######################
scrol=Scrollbar(frame2_1)
scrol.pack(side=RIGHT, fill=Y)
    
############################################


p=Label(frame2_1, text="Actual configuration", font=("Arial",14),fg="white", background="gray")
p.pack(side=TOP)

tackeClass=test(scrol)
tackeClass.reads()

#### button's frame 1 and frame 2
button_1=Button(frame1_1, text="Submit", width=10, font=("Arial",14), command=lambda:tackeClass.writes(ip4value.get(),dns_4_value.get()))
button_1.place(x=400,y=100)

button_2=Button(frame1_2, text="Submit", width=10, font=("Arial",14), command=lambda:tackeClass.writes(ip6value.get(),dns_6_value.get())            )
button_2.place(x=400,y=100)

########
frame2_1_2=Frame(frame2_1, height=50,width=600, background="gray")
line_modify=Label(frame2_1_2, text="delte line: ",background="gray", font=("Arial",12), fg="white")
line_modify.place(x=10, y=10)
line_num=Entry(frame2_1_2,font=("Arial", 12))
line_num.place(x=100,y=10)
modify=Button(frame2_1_2, text="Delete", width=10, font=("Arial", 12), command=lambda:tackeClass.modify(line_num.get()))
modify.place(x=400,y=10)

frame2_1_2.pack()
frame2_1.pack()
# scrol.config(command=actualConfig.yview)
frame2.pack(side=RIGHT)



app.mainloop()
