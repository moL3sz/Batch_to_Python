# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run 
def find(argv):
    if argv[3] == "":
        return
    counts = 0
    with open(argv[2]) as f:
        if argv[1] in argv[2]:
            counts+=1
    if counts >= 1:
        with open(argv[3],"a") as f:
            f.write(argv[1],argv[3])
    
        