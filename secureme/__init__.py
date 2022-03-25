import sys, subprocess, datetime

class top():
    _alphabet = r"abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+-=,./;'[]<>?:\"{}|₹"

def HWID():
    string = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    for i in string:
        if i.isdigit() == True:
            HW += int(i)
    return 0

def encrypt(Text, Method="Length", Password="22"):
    args = ["HWID", "Length", "Password", "Date", "Month", "Year", "Hour"]
    if Method == "HWID":
        key = HWID()
    if Method == "Length":
        key = len(Text)
    if Method == "Password":
        key = Password
    if Method == "Date":
        key = datetime.datetime.now().day
    if Method == "Month":
        key = datetime.datetime.now().month
    if Method == "Year":
        key = datetime.datetime.now().year
    if Method == "Hour":
        key = datetime.datetime.now().hour
    if Method not in args:
        print(f"You have to pass one from {args} to encrypt or leave it blank.")
        sys.exit()
    return ''.join(
        top._alphabet[int((top._alphabet.find(i) + key) % len(top._alphabet))]
        for i in Text
    )
    
def decrypt(Text, Method="Length", Password="22"):
    args = ["HWID", "Length", "Password", "Date", "Month", "Year", "Hour"]
    if Method == "HWID":
        key = HWID()
    if Method == "Length":
        key = len(Text)
    if Method == "Password":
        key = Password
    if Method == "Date":
        key = datetime.datetime.now().day
    if Method == "Month":
        key = datetime.datetime.now().month
    if Method == "Year":
        key = datetime.datetime.now().year
    if Method == "Hour":
        key = datetime.datetime.now().hour
    if Method not in args:
        print(f"You have to pass one from {args} to encrypt or leave it blank.")
        sys.exit()
    return ''.join(
        top._alphabet[int((top._alphabet.find(i) + key) % len(top._alphabet))]
        for i in Text
    )
