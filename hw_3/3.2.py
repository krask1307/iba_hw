import os

def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname + "> /dev/null")
    
    if response == 0:
        pingstatus = "SUCCESS"
    else:
        pingstatus = "DOESN'T WORK"
    
    return pingstatus

pingstatus = check_ping()

print(pingstatus)
