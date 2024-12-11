from getmac import get_mac_address as gma
import getpass
import os
import asyncio


macAddress = gma()



# no need data in users.txt
#userName = getpass.getuser()

# implement cmd
# last > users.txt

# trigger func
# get users.txt filter data 
# data manipulation done in golang
# output sent by python


def getUnameAndLogs():
    #execute last command save input to file
    os.system("last > dataManipulation/userLogFile/users.txt")

    # had to create output dir
    os.system("mkdir output")

    #run go cleanup sript
    os.system("go run ./dataManipulation/main.go")

getUnameAndLogs()
print("hello")