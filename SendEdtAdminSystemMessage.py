from glob import glob as exists
from datetime import datetime
import smtplib
import os
def send(fileName_):
    fileName = fileName_
    if not fileName:
        exit()
    if not exists(fileName):
        exit()

    mbotpath=r"d:\edtadmin\programs\netmail.bot"
    aplgpath=r"d:\edtadmin\prod\log"

    nmailbot=mbotpath +r"\netmailbot.exe"
    sysnmlog=aplgpath + r"\NetMailBotSystem.log"
    seasmsg=aplgpath + r"\SendEdtAdminSystemMessageDetail.log"

    with open(seasmsg,"a") as debugLog:
        debugLog.write("\n")
        debugLog.write("====================================\n")
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        debugLog.write("-------------------------------------\n")
        debugLog.write(currentDateTime+"\n")
        with open(fileName) as logFile:
            for row in logFile.readlines():
                debugLog.write(row+"\n")
    computerName = os.environ['COMPUTERNAME']
    errorLevel = os.system(f'{nmailbot} -server smtp.bdp.com -to mrs@bdp.com -from EDTADMMAIL@bdp.com -subject "EDT Admin System Notification From {computerName}" -bodyfile {fileName} -logfile {sysnmlog} -appendlog')
    with open(sysnmlog,"a") as sysLog:
        sysLog(errorLevel+"\n")
    pass


 
    
