from getmac import get_mac_address as gma
import os
import json

def getUnameAndLogs():

    ## check if datacleaning/userLogFile folder exsists
    ## create it if not
    if os.path.exists("dataCleaning/userLogFile/") == False:
        os.system("cd dataCleaning; mkdir userLogFile")

    #execute last command save input to file
    os.system("last > dataCleaning/userLogFile/users.txt")

    # had to create output dir
    os.system("mkdir clientOutput")

    #run go cleanup sript
    os.system("./dataCleaning/main")

'''opens the csv file and returns its data in json format'''
def parseData():
    f = open("clientOutput/data.csv")
    fileContents = f.read()
    #gma() gets the mac address of the client machine
    return json.dumps({gma():fileContents})