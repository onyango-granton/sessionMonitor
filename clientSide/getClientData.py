from getmac import get_mac_address as gma
import os
import json

def getUnameAndLogs():
    #execute last command save input to file
    os.system("last > dataManipulation/userLogFile/users.txt")

    # had to create output dir
    os.system("mkdir output")

    #run go cleanup sript
    os.system("go run ./dataManipulation/main.go")

'''opens the csv file and returns its data in json format'''
def parseData():
    f = open("output/data.csv")
    fileContents = f.read()
    #gma() gets the mac address of the client machine
    return json.dumps({gma():fileContents})