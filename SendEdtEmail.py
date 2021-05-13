from glob import glob as exists
#SET PATH VARIABLES
sysutilp = r"d:\edtadmin\prod\sysbatch\utillib"
gpmlpath = r"d:\edtadmin\prod\email\\edtemail"
stmppath = r"d:\edtadmin\prod\systemp"
edtgplog = r"d:\edtgroup\grpread\log"

import os
#SET FILE VARIABLES
"""
adsmsg = sysutilp + r"\SendEdtAdminSystemMessage.bat"
adsyspag = sysutilp + r"\SendEdtAdminSystemPage.bat"
sndcfmsg = sysutilp + r"\SendEdtGroupSystemConfigListMessage.bat"
sndegmsg = sysutilp + r"\SendEdtGroupEmailMessage.bat"
gpsysmsg = sysutilp + r"\SendEdtGroupSystemMessage.bat"
jmsysmsg = sysutilp + r"\SendEdtGroupSystemPage.bat"
gpsyspag = sysutilp + r"\SendEdtGroupSystemPagebat"
"""
erordetl="{}\\DetailErrors.log".format(edtgplog)
gmailist="{}\\gmailist.tmp".format(stmppath)

import SendEdtAdminSystemMessage
import SendEdtAdminSystemPage
import SendEdtGroupConfigListMessage
#import SendEdtGroupSystemConfigListMessage unused
import SendEdtGroupEmailMessage
import SendEdtGroupSystemMessage
import SendEdtGroupSystemPage
import SendEdtJmagicSystemMessage
import datetime
def errordtlLog(t):
    with open(erordetl,"a") as e:
        e.write(t+"\n")

#use the proper email sending function for each type of emails
functions = {"AdminEmail":SendEdtAdminSystemMessage.send,
             "AdminPage":SendEdtAdminSystemPage.send,
             "ConfigEmail":SendEdtGroupConfigListMessage.send,
             "SupportEmail":SendEdtGroupSystemMessage.send,
             "SupportTicket":[SendEdtGroupSystemMessage.send,SendEdtJmagicSystemMessage.send],
             "SupportPage":[SendEdtAdminSystemPage.send,SendEdtGroupEmailMessage.send,SendEdtJmagicSystemMessage.send],
             
             
             }
def checkForEmails(fname):
    #adminEmails is a array of the required file if its empty just return
    adminEmails = exists(r"{}\{}_*.log".format(gpmlpath,fname))
    if not adminEmails:
        return
    #dir %gpmlpath%\(fname)_*.log /b > %gmaillist%    below the python equivalent
    with open(gmailist,"w") as g:
        for f in adminEmails:
            g.write("{}\n".format(f))
    #FOR /F %%I in (%gmailist%) DO rename %gpmlpath%\%%i RTS_%%i <-> python equivalent
    for f in adminEmails:
        os.rename(r"{}\{}".format(gpmlpath,f),"RTS_{}".format(f))
    #newAdminEmails is just a renamed log files
    newAdminEmails = exists(r"{}\RTS_{}_*.log".format(gpmlpath,fname))
    #dir %gpmlpath%\RTS_(fname)_*.log /b >%gmailist% <-> python equivalent
    with open(gmailist,"w") as g:
        for f in newAdminEmails:
            g.write("{}\n".format(f))
    #FOR /F %%I in (%gmailist%) DO call %(EmailSendFile)% %gpmlpath%\%%i <-> pyhton equivalent
    for f in newAdminEmails:
        path = gpmlpath+r"\{}".format(f)
        if fname == "SupportTicket":
            errordtlLog("***************")
            currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
            errordtlLog(currentDateTime)
            for ff in newAdminEmails:
                errordtlLog(ff)
            #call the funciton properly with the path parameter.
            functions[fname][0](path)
            functions[fname][1](path)
            continue
        if fname == "SupportPage":
            errordtlLog("***************")
            currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
            errordtlLog(currentDateTime)
            for ff in newAdminEmails:
                errordtlLog(ff)
            functions[fname][0](path)
            functions[fname][1]("grouppage",path)
            functions[fname][2](path)
            continue
        functions[fname](path)
    #FOR /F %%I in (%gmailist%) DO del %gpmlpath%\%%i
    for f in newAdminEmails:
        os.remove(r"{}\{}".format(gpmlpath,f))
    #del %gmailist%
    os.remove(gmailist)
def handleAllTypesOfEmail():
    logNames = ["AdminEmail","AdminPage","ConfigEmail","SupportEmail","SupportTicket","SupportPage"]
    for typ in logNames:
        checkForEmails(typ)
