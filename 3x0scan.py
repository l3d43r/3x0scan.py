import socket
import os


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
    for x in range(1,255):
        ip="127.0.0."+str(x)

        info=info2(ip,port)
        if(info):
            print("[+]" + ip + "   --->    " + info)
            os.system(" say Scanning , Found , open port ")
        #else:
           # print( "[+] Nothing open here -- > " + ip)



if __name__ == '__main__':
     main()
