from glob import glob as exists
from datetime import datetime
import os
import ntpath
#extract the filename from the actual path
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
#logging the data
def log(text,path):
    with open(path,"a") as f:
        f.write(text+"\n")
def send(fileName_):
    fileName = fileName_
    if not fileName:
        return
    if not exists(fileName):
        return
    mbotpath=r"d:\edtadmin\programs\netmailbot"
    aplgpath=r"d:\edtadmin\prod\log"
    aplspath=r"d:\edtadmin\prod\log\stats"
    stmppath=r"d:\edtadmin\prod\systemp"
    netmblog=aplgpath+r"\NetMailBot.log"

    nmailbot=mbotpath+r"\netmailbot.exe"
    sysnmlog=aplgpath+r"\NetMailBotSystem.log"
    sjmemlog=aplgpath+r"\SendJmagicEmailMessageDetail.log"
    jmailtrk=aplspath+r"\EdtJmagicEmailSentTrack.log"
    jmbodywt=stmppath+r"\jmbodywt.tmp"
    jmbodyf1 = fileName_
    #just some logging
    log("",sjmemlog)
    log("====================================",sjmemlog)
    currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
    log(currentDateTime,sjmemlog)
    if not exists(jmbodyf1):
        log("The file"+jmbodyf1+" does not exist.",sjmemlog)
        return
    with open(jmbodyf1) as jm:
        for row in jm.readlines():
            log(row,sjmemlog)
    #getting the actual filename (email)
    jbodname = path_leaf(jmbodyf1)
    log("{} {}".format(currentDateTime,jbodname),jmailtrk)
    
    log("Short Description: EDT Production Support Ticket.",jmbodywt)
    log("Detailed Description:",jmbodywt)
    with open(jmbodyf1) as jm:
        for row in jm.readlines():
            #log the file content
            log(row,jmbodywt)
    log("********",jmbodywt)
    log("Ignore any HTML text after this line.",jmbodywt)
    log("******",jmbodywt)
    errorLevel = os.system(nmailbot+"-server smtp.bdp.com -to edsmmagic@bdp.com -from no-reply@bdp.com -subject 'FSY-PSS-COM-EDT' -bodyfile {}  -logfile {} -appendlog".format(jmbodywt,netmblog))
    log(str(errorLevel),netmblog)
    os.remove(jmbodywt)
    
            
