from glob import glob as exists
import os
import shutil
def send():
    sysutilp=r"d:\edtadmin\prod\sysbatch\utililib"
    plstpath=r"d:\edtadmin\prod\list"
    ilstpath=r"d:\edtadmin\prod\list\infolist"
    usmlpath=r"d:\edtadmin\prod\email\usermail"
    stmppath=r"d:\edtadmin\prod\systemp"

    sndeumsg=sysutilp+r"\SendEdtUserEmailMessage.bat"
    genidown=plstpath+r"\GenericIdFileOwners.txt"
    lstumlst=ilstpath+r"\LastUserEmailList.txt"
    umailist=stmppath+r"\umailist.tmp"
    zrousrml=stmppath+r"\zrousml.tmp"
    user_emails = []
    #getting all the user emails from the usmldirectory
    for f in exists(usmlpath+r"\UserEmail@a*.txt"):
        user_emails.append(f)
    #getting the user emails from the genidown file
    with open(genidown) as ge:
        for row in ge.readlines():
            j = "".join(row[:2])
            for f in exists(usmlpath+r"\UserEmail@{}*.txt".format(j)):
                user_emails.append(f)
    import SendEdtUserEmailMessage
    #check if we found any email
    if len(user_emails) > 0:
        #copy the content of the umailst to lstumlst
        shutil.copyfile(umailist,lstumlst)
        for email in user_emails:
            #split the user email: i=UserEmail, j=a391756,k=ohwm61276.txt (just an example)
            i,j,k = email.split("@")[:3]
            ## call the SendEdtUserEmailMessage with the specific paramteres
            SendEdtUserEmailMessage.send("{}@bdp.com".format(i),"{}\\{}{}".format(usmlpath,i,j,k))
        with open(lstumlst,"w") as ls:
            for r in user_emails:
                ls.write(r+"\n")
    if exists(zrousrml):
        os.remove(zrousrml)
