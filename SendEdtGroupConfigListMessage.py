from glob import glob as exists
from datetime import datetime
import os
def send(fileName_):
    fileName = fileName_
    #check if the filename is exists and it is not null
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
        ##just write some log
        debugLog.write("\n")
        debugLog.write("====================================\n")
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        debugLog.write("-------------------------------------\n")
        debugLog.write(currentDateTime+"\n")
        with open(fileName) as logFile:
            for row in logFile.readlines():
                debugLog.write(row+"\n")
        #getting the actual comp
        computerName = os.environ['COMPUTERNAME']
        errorLevel = os.system(f'{nmailbot} -server smtp.bdp.com -to EDTConfigurationListChanges@bdp.com -from EDTCONFIGLISTEMAIL@bdp.com -subject "EDT Config List Change Group System Notification From {computerName}" -bodyfile {fileName} -logfile {sysnmlog} -appendlog')
    
    
    #logging the exitcode of the nmailbot 
    with open(sysnmlog,"a") as sysLog:
        sysLog(errorLevel+"\n")
    with open(seasmsg,"a") as sysLog:
        sysLog(errorLevel+"\n")


 
    
