#Encrypter_v2.1
import os
from datetime import datetime
import time
import subprocess

def Encrypt(absolutepath, key):
    global tstart 
    tstart = time.perf_counter()
    file = open(absolutepath, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    return write(absolutepath, data, "ept")


def Decrypt(filename, key):
    absolutepath = filename.strip()
    file = open(absolutepath, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    return write(absolutepath, data, "dpt")

def write(absolutepath, data, type):
    
    pathtofile = os.path.dirname(absolutepath)
    filename = os.path.basename(absolutepath)
    

    timest = datetime.now().strftime("%Y%m%d-%H%M%S")
    if type == "ept":
        newname = "Enc"+filename+".dp"
    elif type == "dpt":
        newname = filename[3:-3]

    writingpath = os.path.join(pathtofile, newname)
    file_stat = os.path.exists(writingpath)
    
    if file_stat == True:
        if type == "ept":
            inter = (os.path.splitext(newname)[0])
            newname = os.path.splitext(inter)[0]+"-"+ timest + os.path.splitext(inter)[1] + os.path.splitext(newname)[1]
        elif type == "dpt":
            newname = os.path.splitext(newname)[0]+"-"+ timest +os.path.splitext(newname)[1]
        writingpath = os.path.join(pathtofile, newname)

    file = open(writingpath, "wb")
    file.write(data)
    file.close()
    global tfinish 
    tfinish = time.perf_counter()
    return writingpath, newname


def restart():
    valid = True
    while valid:
        print(f'Process time is {(tfinish - tstart):.5f} seconds')
        ans = input("\nDo you want to continue the program ? 'y' or 'n' : ")
        if ans in ['n', 'no','N','NO','No']:
            valid = False
            return True
        elif ans in ['y','yes','Y','YES','Yes']:
            valid = False
            return False
        else:
            valid = True
            print("Invalid Answer!!")

def welcome_screen():
    if os.name == "posix":
        subprocess.run('clear', shell=True)
    else:
        subprocess.run('cls', shell=True)
    logotime = 0.5
    titletime = 0.75
    finishline = 0.25
    finishlinelength = 65
    space = "    "
    rwsymbol = "_"
    currentsymbol = rwsymbol
    for ftime in range(0,finishlinelength):
        if ftime >= finishlinelength-1 :
            print(currentsymbol)
            print("")
        else:
            print(currentsymbol,end="\r")
        currentsymbol = currentsymbol + rwsymbol
        time.sleep(0.05)
    time.sleep(logotime)
    print(space+"                             //                      ")
    time.sleep(logotime)
    print(space+"                            //                       ")
    time.sleep(logotime)
    print(space+"                           //                        ")
    time.sleep(logotime)
    print(space+"          + + + + + + + + // // + + + + + + + +      ")
    time.sleep(logotime)
    print(space+"         //              // //               //      ")
    time.sleep(logotime)
    print(space+"        //              // //               //       ")
    time.sleep(logotime)
    print(space+"       //              // //               //        ")
    time.sleep(logotime)
    print(space+"      //              // //               //         ")
    time.sleep(logotime)
    print(space+"     //              // //               //          ")
    time.sleep(logotime)
    print(space+"    + + + + + + + + // // + + + + + + + +            ")
    time.sleep(logotime)
    print(space+"                      //                             ")
    time.sleep(logotime)
    print(space+"                     //                              ")
    time.sleep(logotime)
    print(space+"                    //                               ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A                            ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N                         ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N  D                      ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N  D  O                   ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N  D  O  R                ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N  D  O  R  A             ",end="\r")
    time.sleep(titletime)
    print(space+"                    //  A  N  D  O  R  A  S          ")
    print("")
    time.sleep(finishline)
    currentsymbol = rwsymbol
    for ftime in range(0,finishlinelength):
        print(currentsymbol,end="\r")
        currentsymbol = currentsymbol + rwsymbol
        time.sleep(0.05)
    time.sleep(2)
    if os.name == "posix":
        subprocess.run('clear', shell=True)
    else:
        subprocess.run('cls', shell=True)

if __name__ == "__main__":
    try:
        # welcome_screen()
        print(r"===========================\\Encrypter_v2.2//==========================")
        print("---------------Press 'Ctrl + C' to Exit Program Any Time---------------")
        time.sleep(2)
        while True:
            try:
                try:
                    key = int(input("\nEnter Key for encryption (Between 1 - 255) : "))
                    filepath = input("Drag and Drop File here : ")
                    absolutepath = filepath.strip().strip("\'").strip('\"').replace("\\''","")
                    
                    filename = os.path.basename(absolutepath)

                    if key in range(1,256):
                        if filename.endswith('.dp'):
                            decfilepath, decfilename = Decrypt(absolutepath, key)
                            print(f"\nFile decrypted successfully! Decrypted file name : {decfilename}")
                            print("File saved in " + decfilepath)
                            if restart():
                                break
                        else:
                            encfilepath, encfilename = Encrypt(absolutepath, key)
                            print(f"\nFile encrypted successfully! Encrypted file name : {encfilename}")
                            print("File saved in " + encfilepath)
                            if restart():
                                break
                    else:
                        print("\n~ Please Enter Valid Key Value Number Between 1-255...!!!")
                except ValueError:
                    print("\n~ Please check key values again..!! It should be Numerical Value")
                except FileNotFoundError:
                    print("\n~ The File that you want to encrypt/decrypt is not exist  OR \n~ The File path is not exist, \nPlease Check again...!")
                except OSError:
                    print("\n~ Please Check the File name again ...!")
            except KeyboardInterrupt:
                break
        print("Exiting Program.......")
        time.sleep(1.5)
        if os.name == "posix":
            subprocess.run('clear', shell=True)
        else:
            subprocess.run('cls', shell=True)
        print("\nPress Enter to EXIT the program..!")
        input()
        if os.name == "posix":
            subprocess.run('clear', shell=True)
        else:
            subprocess.run('cls', shell=True)
    except KeyboardInterrupt:
        print("Force Stopping....!!!")
        time.sleep(0.5)
        if os.name == "posix":
            subprocess.run('clear', shell=True)
        else:
            subprocess.run('cls', shell=True)