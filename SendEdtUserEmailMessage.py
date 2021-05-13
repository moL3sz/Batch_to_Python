from glob import glob as exists
from datetime import datetime
import ntpath
import os
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def log(text,where):
    with open(where,"a") as f:
        f.write(text+"\n")
def send(argv):
    if argv[2] == "":
        return

    mbotpath=r"d:\edtadmin\programs\netmailbot"
    sysutilp=r"d:\edtadmin\prod\sysbatch\utillib"
    plstpath=r"d:\edtadmin\prod\list"
    aplgpath=r"d:\edtadmin\prod\log"
    stmppath=r"d:\edtadmin\prod\systemp"
    slogpath=r"d:\edtgroup\grpread\log\stats"

    nmailbot=mbotpath+r"\netmailbot.exe"
    fndtxlst=sysutilp+r"\FindTextInList.bat"
    ausrmesg=plstpath+r"\UserMessage.txt"
    edtbidnm=plstpath+r"\EdtGroupBadgeIdsAndNames.txt"
    sysnmlog=aplgpath+r"\NetMailBotSystem.log"
    seuemlog=aplgpath+r"\SenEdtUserEmailMessageDetail.log"
    edtidfnd=stmppath+r"\edtidfnd.tmp"
    ckatsign=stmppath+r"\ckatsign.tmp"
    isatsign=stmppath+r"\isatsign.tmp"
    isperiod=stmppath+r"\isperiod.tmp"
    umailtrk=slogpath+r"\EdtUserEmailSentTrack.log"
    umsendto=argv[1]
    umbodyf1=argv[2]
    if not exists(umbodyf1):
        log("", seuemlog)
        log("======================" , seuemlog)
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        log(f"{currentDateTime}" , seuemlog)
        log(f" Send E-mail To: {umsendto}" , seuemlog)
        log(" -------------------------"  , seuemlog)
        log(f" The recipent address {umsendto} is invalid.", seuemlog)
        return
    fmrbadge = umsendto.split("@")[0]
    fndatsgn = 1 if "@" in umsendto else 0
    fndperod = 1 if "." in umsendto else 0
    if fmrbadge == "AP106137":
        return
    if fndatsgn == 0 or fndperod == 0:
        log("", seuemlog)
        log("======================" , seuemlog)
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        log(f"{currentDateTime}" , seuemlog)
        log(f" Send E-mail To: {umsendto}" , seuemlog)
        log(" -------------------------"  , seuemlog)
        log(f" The recipent address {umsendto} is invalid.", seuemlog)
        os.remove(umbodyf1)


    log("",seuemlog)
    log( "=========================",seuemlog)
    currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
    log(currentDateTime, seuemlog)
    log( f"Send E-mail To: {umsendto}", seuemlog)
    log(  f"------------------------",seuemlog)
    with open(umbodyf1) as f:
        for r in f.readlines():
            log(r,seuemlog)
    umbodname = path_leaf(umbodyf1)
    currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
    log(f"{currentDateTime} {umsendto} {umbodname}",umailtrk)

    """
    64.line

    """
    import FindTextInList
    FindTextInList.find([fmrbadge,edtbidnm,edtidfnd])
    if exists(edtidfnd):
        os.remove(edtidfnd)
        errorLevel = os.system(nmailbot+" -server smtp.bdp.com - to {} -from EDTFTPPROD@bdp.COM -fromfriendly EDT BATCH AUTOMATED E-mail Service -subject EDT FILE TRANSFER STATUS -bodyfile {} -logfile {} -appendlog".format(umsendto,umbodyf1,sysnmlog))
        log(str(errorLevel),sysnmlog)
    os.remove(umbodyf1)

    


