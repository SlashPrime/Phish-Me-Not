#!/usr/bin/python3
import subprocess
import time
import smtplib
import os
from email.message import EmailMessage
from tkinter import *

subprocess.call("XXXX")

with open ("ngrokURL","r") as f:	# reading victim_url to include in the mail
	victim_url = f.read()

EMAIL_ADDRESS = os.environ.get('EMAILID')
EMAIL_PASS = os.environ.get('PASS')

print ("\n")
choice = input("[?] Do you want to create an employee-table?(y/n): ")
if choice == 'y':
	root = Tk()
	root.title('Phish-Me-Not')
	root.geometry("430x200+630+350")
	bg= PhotoImage(file="background.png")   #define bg image    

	#create a canvas
	my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	my_canvas.pack(fill="both", expand=True)

	#set image in canvas
	my_canvas.create_image(0,0, image=bg, anchor="nw")
	my_canvas.create_text(220,80, text="Welcome to", font=("Helvetica", 24,'bold'), fill="white")
	my_canvas.create_text(220,120, text="Phish-Me-Not", font=("Helvetica", 24,'bold'), fill="white")

	def destroy():
		root.destroy()
	root.after(2000, destroy)
	root.mainloop()

	root = Tk()
	root.title('Phish-Me-Not')
	root.geometry("430x200+630+350")
	bg= PhotoImage(file="background.png")   #define bg image    

	#create a canvas
	my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	my_canvas.pack(fill="both", expand=True)

	#set image in canvas
	my_canvas.create_image(0,0, image=bg, anchor="nw")
	my_canvas.create_text(220,40, text="Enter number of employees:", font=("Helvetica", 13,'bold'), fill="white")



	entry1 = Entry(root, font=("Helvitica",12),width=13, fg="black", bd=0)

	entry1_window = my_canvas.create_window(160,70,anchor='nw', window=entry1)

	def myClick():
	    global noe
	    noe=entry1.get()
	    root.destroy()
	button1=Button(root, text="Done",font=("times",12),width=5,padx=15, pady=7, fg='white', bg='black', bd=0, command=myClick)
	button1_window = my_canvas.create_window(190,120,anchor='nw', window=button1)

	#root.bind('<Configure>',resizer)
	root.mainloop()
	file = open("employee-table.txt", "w")
	file.write("Name Email IP_Address Recent_Project\n")
	for i in range(0,int(noe)):
	    root = Tk()
	    root.title('Phish-Me-Not')
	    root.geometry("430x200+630+350")
	    bg= PhotoImage(file="background.png")   #define bg image    

	    #create a canvas
	    my_canvas = Canvas(root, width=200, height=100, bd=0, highlightthickness=0)
	    my_canvas.pack(fill="both", expand=True)

	    #set image in canvas
	    my_canvas.create_image(0,0, image=bg, anchor="nw")
	    my_canvas.create_text(100,25, text="Employee:"+str(i+1), font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,50, text="Name:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,75, text="Email:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,100, text="IP address:", font=("Helvetica", 13,'bold'), fill="white")
	    my_canvas.create_text(100,125, text="Recent Project:", font=("Helvetica", 13,'bold'), fill="white")
	    
	    entry1 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry2 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry3 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)
	    entry4 = Entry(root, font=("Helvitica",14),width=20, fg="black", bd=0)

	    entry1_window = my_canvas.create_window(165,35,anchor='nw', window=entry1)
	    entry2_window = my_canvas.create_window(165,60,anchor='nw', window=entry2)
	    entry3_window = my_canvas.create_window(165,85,anchor='nw', window=entry3)
	    entry4_window = my_canvas.create_window(165,110,anchor='nw', window=entry4)
	    
	    def myClick():
	        name=entry1.get()
	        email=entry2.get()
	        ip=entry3.get()
	        project=entry4.get()
	        
	        file.write(name.replace(" ","_"))
	        file.write(" "+email)
	        file.write(" "+ip)
	        file.write(" "+project.replace(" ","_")+"\n")
	        root.destroy()
	    if(int(i)==int(noe)-1):
	        button1=Button(root, text="Finish",font=("times",10),width=5, fg='white', bg='black', bd=0, command=myClick)
	        button1_window = my_canvas.create_window(250,150,anchor='nw', window=button1)
	    else:
	        button1=Button(root, text="Next",font=("times",10),width=5, fg='white', bg='black', bd=0, command=myClick)
	        button1_window = my_canvas.create_window(250,150,anchor='nw', window=button1)
	    
	    #root.bind('<Configure>',resizer)
	    root.mainloop() 
	file.close()
print ("\n")
with open ("employee-table.txt","r") as employee_table:
	email=[]
	name=[]
	ip=[]
	recent_project=[]
	
	for i in employee_table:
		employee_intel = employee_table.readlines()[:]
		for employee in employee_intel:
			name.append(employee.strip().split()[0])
			email.append(employee.strip().split()[1])
			ip.append(employee.strip().split()[2])
			recent_project.append(employee.strip().split()[3])
print ("[+] Sending phishing email to employees...")
for emp in range(len(email)):
	print (f'[+] Sending mail to: {name[emp].replace("_"," ")}')
	msg = EmailMessage()
	msg['Subject'] = "EMPLOYEE BONUS REWARD" #subject
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = email[emp]
	msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {name},<br><br>On behalf of company's management, I would like to extend our appreciation towards your amazing work on the project <b>{project}</b>. We appreciate your contribution and it is always a pleasure to work with brilliant and dedicated people like you.<br><br>As a sign of our appreciation, we would like to reward you for your dedication towards your work. As part of our new fiscal period, kindly accept the enclosed cheque as a token of appreciation for your praisworthy contributions to the company.<br><br>We are proud to have you onboard. Keep up the good work!<br><br>Regards,<br><br>Dhruv Kandpal<br>Manager<br>Human Resource.<br><br>P.S.-  To view the complete payment details, you may <a href={victim_url}>click here</a>. You are most welcome to contact the HR department to seek any clarification.</p>
		</body>
	</html>
		""".format(victim_url=victim_url,name=name[emp].replace("_"," "),project=recent_project[emp]),subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
		smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
		smtp.send_message(msg)

subprocess.call("YYYY")

with open ("results.txt","r") as results_table:
	IP = []
	Port = []
	Country = []
	State = []
	City = []
	Latitude = []
	Longitude = []
	Zip_Code = []
	Time_Zone = []
	ISP = []
	Domain = []
	Is_Proxy = []
	Proxy_Type = []
	
	for j in results_table:
		result_data=results_table.readlines()[:]
		for phished_employee in result_data:
			IP.append(phished_employee.strip().split()[0])
			Port.append(phished_employee.strip().split()[1])
			Country.append(phished_employee.strip().split()[2])
			State.append(phished_employee.strip().split()[3])
			City.append(phished_employee.strip().split()[4])
			Latitude.append(phished_employee.strip().split()[5])
			Longitude.append(phished_employee.strip().split()[6])
			Zip_Code.append(phished_employee.strip().split()[7])
			Time_Zone.append(phished_employee.strip().split()[8])
			ISP.append(phished_employee.strip().split()[9])
			Domain.append(phished_employee.strip().split()[10])
			Is_Proxy.append(phished_employee.strip().split()[11])
			Proxy_Type.append(phished_employee.strip().split()[12])

victims = []
for flag_emp in IP:
	if flag_emp in ip:
 		victims.append(name[ip.index(flag_emp)].replace("_"," "))
print ("\n[+] The following employees were phished!")
print ("\n".join(victims))

with open ("phished-employees","w") as f:
	f.write("\n".join(victims))

#sending awareness email to phished employees
print ("\n")
with open ("phished-employees","r") as f:
	data=f.readlines()
	for i in data:
		i=i.replace(" ","_").strip()
		print (f'[+] Sending awareness mail to {i.replace("_"," ")}')

		msg = EmailMessage()
		msg['Subject'] = "URGENT: YOU HAVE BEEN PHISHED!" #subject
		msg['From'] = EMAIL_ADDRESS
		msg['To'] = email[name.index(i)]
		msg.add_alternative("""\
		<!DOCTYPE html>
		<html>
			<body>
			<p>Dear {name},<br><br>In an effort to further enhance our company’s cyber defenses, a phishing mail was sent to you. The bad news is that you fell prey to it. The good news is that we are here to help you.<br><br><b><i>Although we maintain controls to help protect our networks and computers from cyber threats, we rely on you to be our first line of defense.</i></b><br><br><i>To avoid such phishing schemes in future, please observe the following email best practices:</i><ul><li><b>Do not click on links</b> or <b>attachments</b> from senders that you do not recognize. Be especially wary of .zip or other compressed or executable file types.</li><li><b>Do not provide sensitive personal information</b> (like usernames and passwords) over email.</li><li><b>Watch for email senders</b> that use <b>suspicious or misleading domain names.</b></li><li><b>Inspect URLs carefully</b> to make sure they’re legitimate and not imposter sites.</li><li><b>Do not try to open any shared document</b> that you’re <b>not expecting to receive</b>.</li></ul><br>If you receive an e-mail that <b>you suspect to be a phishing attempt</b>, or if you are <b>unsure of an e-mail’s legitimacy, please do not respond.</b> Remember that <b>our company will never request personal information</b>, usernames, passwords, or money <b>from you via email.</b><br><br>Do not feel demoralized, instead feel happy that now you are much more aware about malicious phishing schemes. Thanks for helping to keep our networks and our people safe from these threats.<br><br>P.S-Call It a <b>reinforcement or awareness drill</b>, no simulated phishing program is complete without supporting content.<br><br>Kindly find the guide attached with this email on <b>how to spot and report suspected phishing attempts</b> to protect yourself and the company from cybercriminals, hackers, and other bad actors.<br><br>Please let us know if you have any questions.<br><br>Regards,<br>th3hack3rw!z<br>HR Head</p>
			</body>
		</html>
			""".format(name=i.replace("_"," ")),subtype='html')

		files = ['phishing_awareness_guide.pdf']
		for i in files:
			with open (i,'rb') as f:
				file_data = f.read()
				file_name = f.name
			#	print(file_type)
			msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

		with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:	
			smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
			smtp.send_message(msg)
print ("\n[~] Thank you for using Phish-Me-Not!")
