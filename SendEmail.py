sysbatf1=r"d:\edtadmin\prod\sysbatch\batfiles"
syjqpath=r"d:\edtadmin\prod\sysqueue"

sedtmail=sysbatf1+r"\SendEdtEmail.bat"
susrmail=sysbatf1+r"\SendUserEmail.bat"
openseml=syjqpath+r"\OPEN_SendEmail.tmp"
from datetime import datetime
if __name__ =="__main__":
    with open(openseml,"a") as f:
        currentTime = datetime.now().time().strftime("%H:%M:%S")
        f.write("Running at "+currentTime+"\n")
    import SendEdtEmail
    SendEdtEmail.handleAllTypesOfEmail()
    import SendUserEmail
    SendUserEmail.send()