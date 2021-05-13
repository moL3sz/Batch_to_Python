from glob import glob as exists
from datetime import datetime
import os
from sys import argv
def send(fileName_):
    #check if the filname is exits and not null
    fileName = fileName_
    if not fileName:
        return
    if not exists(fileName):
        return

    mbotpath=r"d:\edtadmin\programs\netmail.bot"
    aplgpath=r"d:\edtadmin\prod\log"

    nmailbot=mbotpath +r"\netmailbot.exe"
    sysnmlog=aplgpath + r"\NetMailBotSystem.log"
    seasmsg=aplgpath + r"\SendEdtAdminSystemMessageDetail.log"
    #some loggin
    with open(seasmsg,"a") as debugLog:
        debugLog.write("\n")
        debugLog.write("====================================\n")
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        debugLog.write("-------------------------------------\n")
        debugLog.write(currentDateTime+"\n")
        with open(fileName) as logFile:
            for row in logFile.readlines():
                debugLog.write(row+"\n")
    #loggin the exitcode of the nmailbot program
    computerName = os.environ['COMPUTERNAME']
    errorLevel = os.system(f'{nmailbot} -server appmailrelay.bdp.com -to mrs@bdp.com -from EDTADMPAGE@bdp.com-subject "EDT Admin System Notification From {computerName}" -bodyfile {fileName} -logfile {sysnmlog} -appendlog')
    with open(sysnmlog,"a") as sysLog:
        sysLog(errorLevel+"\n")
    with open(seasmsg,"a") as sysLog:
        sysLog(errorLevel+"\n")
        pass


 
    
