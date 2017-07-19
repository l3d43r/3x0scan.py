import socket
import os
import sys
from colorama import Fore, Back, Style
import time

os.system("clear")
print("\n")
print("## Detected Hosts with open ports 22 ")
print("<------------------------------------>")
print("")



print ("Processing wait for it...\\"),
syms = ['\\', '|', '/', '-']
bs = '\b'

for _ in range(10):
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(.20)
        sys.stdout.flush()


def info2(ip,port):
    try:
        socket.setdefaulttimeout(1)
        s= socket.socket()
        s.connect((ip,port))
        info=s.recv(45)
        return info
    except:
        return

def main():
    port=22
    for x in range(74,137):
        ip="162.246.52."+str(x)

        info=info2(ip,port)
        if(info):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print(Fore.LIGHTGREEN_EX+ Back.BLACK +"[+]" + ip + "   --->    " + info+Style.RESET_ALL)
            #os.system(" say Scanning , Found , open port ")
        #else:
           # print( "[+] Nothing open here -- > " + ip)



if __name__ == '__main__':
     main()
