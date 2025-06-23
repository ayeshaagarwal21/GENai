import os
import webbrowser

desktop=r"C:\Users\exper\desktop"

print("1. Create folder")
print("2. Create file")
print("3. Send Whatsapp Message")
print("4. Shutdown PC")
choice=input("Enter your choice from (1-4)")
if(choice=="1"): 
  folder_name=input("enter folder Name:")
  folder_path=os.path.join(desktop,folder_name)
  try:
    os.makedirs(folder_path)
    print(f"folder'{folder_name}'created on desktop")
  except FileExistsError: 
    print("folder already exsists")
  except Exception as e:  
    print("error:",e)

elif(choice=="2"):  
  file_name=input("enter file name(with extension like test.txt)")
  file_path=os.path.join(desktop,file_name)
  try:  
    with open(file_path,'w') as f:  
      f.write("")
    print(f"file'{file_name}'created on desktop")
  except Exception as e:
    print("error:",e)

elif(choice=="3"):  
  phone=int(input("enter the phone number (with country code(+91 etc.)):"))
  message=input("enter message:")
  url=f"https://web.whatsapp.com/send?phone={phone}&text={message}"
  webbrowser.open(url)
  print("whatsapp web opened in your browser please send message manually")

elif(choice=="4"):  
  confirm=input("are you sure u want to shutdown your pc(yes/no):")
  if(confirm.lower()=="yes"): 
    print("shutting down your pc..")
    os.system("shutdown /s /t 1")
  else: 
    print("shutdown canceled")

else: 
  print("invalid choice, enter from(1-4)")