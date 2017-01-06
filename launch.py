#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import socket
import time
import os
import datetime
import httpud

ipnow = '0.0.0.0'

def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H-%M-%S")

def getIP():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    # ipList = socket.gethostbyname_ex(socket.gethostname())
    # myaddr = ipList[2][2]
    return myaddr

def send2serv(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect((ip, port))  
    import time
    myaddr = getIP()
    sock.send(myaddr)
    sockGet = sock.recv(1024)
    global ipnow
    if sockGet != ipnow:
        print('[%s] The ip now is %s.'%(getTime(), sockGet))
        ipnow = sockGet
    sock.close()
    time.sleep(10)

def alwaysend(ip, port, delay):
    while 1:
        try:
            send2serv(ip, port)
            time.sleep(delay)
        except:
            pass

def httpserverX(serveraddr, SimpleHTTPRequestHandler):
    srvr = httpud.ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
    srvr.serve_forever()

def httpserver():
    print('HTTP server running...')
    os.system('ltpd.bat')

# def ftpserver(port=2121):
#     mtpyftp.main(port)

if __name__ == '__main__': 
    try:
        thread.start_new_thread(alwaysend, ('123.207.136.236', 1221, 30,))
        thread.start_new_thread(httpserver, ())
        thread.start_new_thread(httpserverX, (httpud.serveraddr, httpud.SimpleHTTPRequestHandler,))
        while 1:
            time.sleep(20)
    except:
        print "Error: unable to start thread"
    