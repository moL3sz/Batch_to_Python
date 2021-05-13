from sys import argv
from datetime import datetime
from glob import glob as exists
import os
import ntpath
#extracting the filname from the path.
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def send(argv):
    #check if the file is specifyed (argv[2]) if not just returns
    if not argv[2]:
        return
    mbotpath=r"d:\edtadmin\programs\netmailbot"
    plstpath=r"d:\edtadmin\prod\list"
    aplgpath=r"d:\edtadmin\prod\log"
    aplspath=r"d:\edtadmin\prod\log\stats"
    stmppath=r"d:\edtadmin\prod\systemp"
    jobqpath=r"d:\edtgroup\support\jobqueue"

    nmailbot=mbotpath+r"\netmailbot.exe"
    edtpagrp=plstpath+r"\EdtPagingGroup.txt"
    netmblog=aplgpath+r"\NetMailBot.log"
    segemlog=aplgpath+r"\SendEdtGroupEmailMessageDetail.log"
    gamiltrk=aplgpath+r"\EdtGroupEmailSentTrack.log"
    vtxtgmsg=stmppath+r"\vtxtgmsg.tmp"

    gmsendto = argv[1]
    gmbodyf1 = argv[2]

    egrpfrm="EDTGRPMAIL"
    egrpsubj= "EDT GROUP NOTIFICATION"

    if gmsendto == "grouppage":
        egrpfrm="EDTGRPAGE"
        egrpsubj= "EDT Group Pager Notification"
    #logging
    with open(segemlog,"a") as slog:
        slog.write("\n")
        slog.write("====================================\n")
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        slog.write(currentDateTime+"\n")
        slog.write("-------------------------------------\n")
    #check if the filen is exists
    if not exists(gmbodyf1):
        with open(segemlog,"a"):
            slog.write(f"The file {gmbodyf1} does not exist.")
            return
    with open(segemlog,"a") as slog:
        with open(gmbodyf1) as gm:
            for g in gm.readlines():
                slog.write(g+"\n")
    gbodname = path_leaf(gmbodyf1)
    with open(gamiltrk) as g:
        currentDateTime = datetime.now().strftime("%Y. %m. %d %H:%M:%S")
        g.write(currentDateTime+" "+gbodname+"\n")
    
    #runs the nmailbot and logging the exit code
    errorLevel = os.system(nmailbot +'-server smtp.bdp.com -to edtproductionsupport@bdp.com -from EDTPRODSUPMAIL@bdp.com -subject "{}" -bodyfile {} -logfile {} -appendlog'.format(egrpsubj,gmbodyf1,netmblog))
    with open(netmblog) as nb:
        nb.write(errorLevel+"\n")
    errorLevel = os.system(nmailbot+' -server smtp.bdp.com -to tprschange@bdp.com -from EDTPRODSUPMAIL@bdp.com -subject "{}" -bodyfile {} -logfile {} -appendlog'.format(egrpsubj,gmbodyf1,netmblog))
    with open(netmblog) as nb:
        nb.write(errorLevel+"\n")
    if gmsendto != "grouppage":
        return
    computername = os.environ["COMPUTERNAME"]
    with open(vtxtgmsg) as vt:
        vt.write("EDT batch process issue on "+computername+"\n")
        vt.write("CHECK e-mail and logs for errors.\n")
        for f in exists(jobqpath+r"\PROCESSING_*.tmo"):
            vt.write(f+"\n")
    errorLevel = os.system(nmailbot+' -server smtp.bdp.com -tolist {} -from {}@bdp.com -subject "{}" -bodyfile {}  -logfile {} -appendlog'.format(edtpagrp,egrpfrm,egrpsubj,vtxtgmsg,netmblog))
    with open(netmblog) as nt:
        nt.write(errorLevel+"\n")
    os.remove(vtxtgmsg)
    exit()

    
