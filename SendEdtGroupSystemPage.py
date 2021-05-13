from glob import glob as exists
from datetime import datetime
import os
def send(fileName_):
    fileName = fileName_
    if not fileName:
        return
    if not exists(fileName):
        return
    mbotpath=r"d:\edtadmin\programs\netmail.bot"
    aplgpath=r"d:\edtadmin\prod\log"
    plstpath=r"d:\edtadmin\prod\list"
    edtpagrp = plstpath+r"\EdtPagingGroup.txt"

    nmailbot=mbotpath +r"\netmailbot.exe"
    sysnmlog=aplgpath + r"\NetMailBotSystem.log"
    seasmsg=aplgpath + r"\SendEdtAdminSystemMessageDetail.log"
    #some logging
    with open(seasmsg,"a") as debugLog:
        debugLog.write("\n")
        debugLog.write("====================================\n")
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        debugLog.write("-------------------------------------\n")
        debugLog.write(currentDateTime+"\n")
        with open(fileName) as logFile:
            for row in logFile.readlines():
                debugLog.write(row+"\n")
    #actual computername
    
    computerName = os.environ['COMPUTERNAME']
    #logging the exitcode of netmailbot
    errorLevel = os.system(f'{nmailbot} -server smtp.bdp.com -tolist {edtpagrp}  -from EDTPRODSUPMAIL@bdp.com -subject "EDT GROUP System Notification From {computerName}" -bodyfile {fileName} -logfile {sysnmlog} -appendlog')
    with open(sysnmlog,"a") as sysLog:
        sysLog(errorLevel+"\n")
    pass