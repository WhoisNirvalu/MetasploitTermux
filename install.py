#/usr/lib/python3

#Import
import os 

#Banner
banner = ('''Welcome user of termux to Metasploit installer''')
metasploit = ('''
    __  ___     __                   __      _ __ 
   /  |/  /__  / /_____ __________  / /___  (_) /_
  / /|_/ / _ \/ __/ __ `/ ___/ __ \/ / __ \/ / __/
 / /  / /  __/ /_/ /_/ (__  ) /_/ / / /_/ / / /_  
/_/  /_/\___/\__/\__,_/____/ .___/_/\____/_/\__/  
                          /_/                     
Made by Nirvalu Version 1.0
''')



#Banner 2
print(banner)
print(metasploit)

#Modules
modules = ("perl python python2 python3 ruby -y"

os.system("termux-setup-storage")
print("Accept the permission for which termux can access your files")
os.system("apt update && apt upgrade -y")
os.system("apt install"), modules
os.system("pkg install unstable-repo")
os.system("clear")
print("Now wait to install metasploit")
os.system("apt install metasploit -y")

print("Ready!!! now run msfconsole to open the metasploit console")
print('''
                                                                     
 ,----.                    ,--.,--.                       ,-.,----.  
'  .-./    ,---.  ,---.  ,-|  ||  |-.,--. ,--.,---.      /  /'.-.  | 
|  | .---.| .-. || .-. |' .-. || .-. '\  '  /| .-. :    /  /   .' <  
'  '--'  |' '-' '' '-' '\ `-' || `-' | \   ' \   --.    \  \ /'-'  | 
 `------'  `---'  `---'  `---'  `---'.-'  /   `----'     \  \`----'  
                                     `---'                `-'        
''')

