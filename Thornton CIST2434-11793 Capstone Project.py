def path_verify(): #Create a function that will change the current working directory to "C:\\Temp" to write text files to the capstone folder.
   """This will create a directory to write all required text files for the entire script"""
   import os #impoting the module to work with the client file system. 
   if not os.path.exists("C:\\Temp\\Thornton Capstone FALL18"):
      os.chdir("C:\\Temp\\")
      os.mkdir("Thornton Capstone FALL18")
      os.chdir("Thornton Capstone FALL18")
      os.getcwd()
      print("You are now currently working in the following path: ", os.getcwd())
   else:
      os.chdir("C:\\Temp\\Thornton Capstone FALL18")
      print("You are now currently working in the following path: ", os.getcwd())
def automated_task1(): # Part II-Create a function that will display information from a client workstation.
   """This will import the socket module and gather system information."""
   flex1 = open("C:\\Temp\\Thornton Capstone FALL18\\pc_info_log.txt", "w")
   import socket #provides socket operations. On systems other than UNIX, it only supports IP.
   pc_host_name = socket.gethostname() #gather the system hostname.
   pc_ipv4_add = socket.gethostbyname(pc_host_name) #gather the IPv4 address using the above variable as an argument.
   pc_fqdn = socket.getfqdn() # gathers the FQDN.
   #Display and write files to text page.
   print("Your device IPv4 address is: ", pc_ipv4_add)
   flex1.write("Your device IPv4 address is: " + str(pc_ipv4_add) + "\n\n")
   print("Your device hostname is: ", pc_host_name)
   flex1.write("Your device hostname is: " + str(pc_host_name) + "\n\n")
   print("Your device FQDN is: ", pc_fqdn)
   flex1.write("Your device FQDN is: " + str(pc_fqdn) + "\n\n")
   flex1.close() #closes respective text file.
def automated_task2(): #Part III-Create a function that will scan the "C:\\Temp" folder to list files with an ".exe" extension.
   """This will scan the Temp folder for executable files."""
   flex2 = open("C:\\Temp\\Thornton Capstone FALL18\\tempdir_exefiles.txt", "w")
   print("These are the scan results. If there are no .exe files, it will print nothing under the this header!\n")
   flex2.write("These are the scan results. If there are no .exe files, it will print nothing under this header!\n\n")
   print("Here's your list of executables:\n\n")
   flex2.write("Here's your list of executables:\n\n")
   import os 
   os.chdir("C:\\Temp")
   path_name= os.getcwd()
   file_lyst = os.listdir(path_name)
   count = 0
   for eachfile in file_lyst:
      count +=1
      if ".exe" in eachfile: 
         print("File", count, ":", eachfile)
         flex2.write("File" + str(count) + ":" + eachfile + "\n\n")
   flex2.close() 
def automated_task4(): #Part III-Create a function that will gather a system's IPv4 address and check validity, class, private/public, or APIPA.
   """This will import the socket and ipaddress modules, gather the IPv4 address and check its validity, address class, private/public, and if it is or is not an APIPA address"""
   flex4 = open("C:\\Temp\\Thornton Capstone FALL18\\validIP_add.txt", "w")
   import socket
   from ipaddress import IPv4Address, IPv4Network #this is a lightweight IPv4/IPv6 manipulation library
   comp_ip =  socket.gethostbyname(socket.gethostname()) #variable which gathers the system's host ip address.
   #Listing the range of the IPv4 address classes for the control statements 
   classA = IPv4Network(("10.0.0.0", "255.0.0.0")) 
   classB = IPv4Network(("172.16.0.0",  "255.240.0.0"))
   classC = IPv4Network(("192.168.0.0", "255.255.0.0"))
   APIPA = IPv4Network(("169.254.0.0", "255.255.0.0"))
   #Validation to see if the IPv4 address is an actual address. Will return an error if invalid.
   try:
      socket.inet_aton(comp_ip) #Convert an IP address in string format to the 32-bit packed  binary format used in low-level network function
      print("This IP is valid")
      flex4.write("This IP is valid\n\n")
   except socket.error: 
      print("Invalid IP")
      flex4.write("Invalid IP\n\n")
   #check the IPv4's address to ascertain if it is private or public, its address class range
   if IPv4Address(comp_ip).is_private:
      print("This is a private IPv4 address!")
      flex4.write("This is a private IPv4 address!\n\n")
   if IPv4Address(comp_ip).is_global:
      print("This is a public IPv4 address!")
      flex4.write("This is a public IPv4 address!\n\n")
   if IPv4Address(comp_ip) == classA:
      print("This is a Class A private IPv4 address!")
      flex4.write("This is a Class A private IPv4 address!\n\n")
   if IPv4Address(comp_ip) == classB:
      print("This is a Class B private IPv4 address!")
      flex4.write("This is a Class B private IPv4 address!\n\n")
   if IPv4Address(comp_ip) == classC:
      print("This is a Class C private IPv4 address!")
      flex4.write("This is a Class C private IPv4 address!\n\n")
   if IPv4Address(comp_ip) == APIPA:
      print("This is an APIPA IPv4 address!")
      flex4.write("This is an APIPA IPv4 address!\n\n")
   elif IPv4Address(comp_ip) != APIPA:
      print("This is not an APIPA IPv4 address!")
      flex4.write("This is not an APIPA IPv4 address!\n\n")       
   flex4.close()
def automated_task3(): #Part III-Create a function to test whether or not the user password is valid.
   """This will check the validity of the user-generated password and perform a shift-cipher encryption with a value of 2."""   
   flex3 = open("C:\\Temp\\Thornton Capstone FALL18\\user_pwd.txt", "w")
   global password, faulty_lyst
   while True: #If the user password does not meet any of the criteria above, allow the user to reenter their password and retest the re-entered password accordingly.
      password = input("Enter a password: ")
      faulty_lyst = ["Password", "passwords", "password123", "PASSWORD", "PASSWORD!!", "password", "admin", "administrator"]
      if len(password) < 8:
         print("Make sure your password is at least 8-14 characters.")
         flex3.write("Make sure your password is at least 8-14 characters.")
      if password[0].isdigit():
         print("Make sure your password dosen't start with a number")
         flex3.write("Make sure your password dosen't start with a number")
      if password in faulty_lyst: 
         print("This password is invalid for use!")
         flex3.write("This password is invalid for use!")
      else:
         print("Your password seems fine") 
         flex3.write("Your password seems fine\n\n") 
         distance = 2
         code = " "
         for ch in password:
            ordValue = ord(ch)
            cipherValue = ordValue + distance
            code += chr(cipherValue)
         print("Your encrypted password is: ", code)
         flex3.write("Your encrypted password is:" +" "+ str(code)+"\n\n")
         break
   flex3.close()
def main(): # Create a main function which expects no arguments and serves as the entry point for your scripting program.
   """This is the entry point for this script"""
   """
   Author: Derahn S. Thornton
   Course: CIST 2434-11793
   Project: Fall 2018 Course Capstone
   Purpose: Create a scripting program that will help you automate the most common networking tasks.
   Credits: Eddie Hearst (supplied the loading bar code for aesthetics!) 
   """
   print("\t\t\tATC Cyber Research Institute\n\n")
   path_verify()
   print("This program encapsulate tools most common to Netwotring or Cyber professionals like yourself!\n\n")
   print("\t\tWelcome to the automated task selection list. Please choose an option:\n\n")
   global taskChoice
   taskChoice = int(input("\t\t1 – Gather system info (IP Address, Hostname, FQDN)\n\t\t2 – Scan Temp Folder for .exe files\n\t\t3 – Verify integrity of stored passwords\n\t\t4 – Verify validity of IP address\n\t\tYour selection is: "))
   if taskChoice == 1:
      print("You have chosen to gather system information.\n")
      automated_task1()
   elif taskChoice == 2:
      print("You have chosen to scan the Temp folder for executable programs.\n")
      automated_task2()
   elif taskChoice == 3:
      print("You have chosen to validate user-generated passwords.\n")
      automated_task3()
   elif taskChoice == 4:
      print("You have chosen to verify the validity of the system IP.\n")
      automated_task4()
   else:
      print("Thats not a selection!")
   do_over = input("Would you like to try another selection? Press 'y' for yes or 'n' for no: ")
   #create the multi-way statement to reloop the program untiil the user wants to quit 
   while do_over != "":
      while do_over == 'y':
         taskChoice = int(input("\t\t1 – Gather system info (IP Address, Hostname, FQDN)\n\t\t2 – Scan Temp Folder for .exe files\n\t\t3 – Verify integrity of stored passwords\n\t\t4 – Verify validity of IP address\n\t\tSelect 0 or any other number if you're finished!\n\t\tYour selection is: "))
         if taskChoice == 1:
            print("You have chosen to gather system information.\n")
            automated_task1()
            do_over = input("Would you like to try another selection? Press 'y' for yes or 'n' for no: ")
         elif taskChoice == 2:
            print("You have chosen to scan the Temp folder for executable programs.\n")
            automated_task2()
            do_over = input("Would you like to try another selection? Press 'y' for yes or 'n' for no: ")
         elif taskChoice == 3:
            print("You have chosen to validate user-generated passwords.\n")
            automated_task3()
            do_over = input("Would you like to try another selection? Press 'y' for yes or 'n' for no: ")
         elif taskChoice == 4:
            print("You have chosen to verify the validity of the system IP.\n")
            automated_task4()
            do_over = input("Would you like to try another selection? Press 'y' for yes or 'n' for no: ")
         else:
            print("Thats not a selection!")
            break
      break
main() 
input("Please press Enter to exit this program")     