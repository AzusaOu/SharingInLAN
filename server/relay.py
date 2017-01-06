#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import os
import time
import datetime
import thread
import shs_mt

def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def serv_listen(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('0.0.0.0', port))  
    sock.listen(5)
    print('Relay service running...')
    while True:
        try:
            connection, address = sock.accept()
            try:  
                buf = connection.recv(1024)
                print('[%s] Get request from %s'%(getTime(), buf))
                with open('template.txt', 'r') as o:
                    template = o.read()
                with open('index.htm', 'w') as w:
                    w.write(template.replace('###', 'http://%s'%buf))
                    # This template can be changed.
                connection.send(buf)
            except socket.timeout:
                print 'time out'
            time.sleep(3)
        except:
            time.sleep(5)
            pass
    connection.close()

def httpserver(port):
    print('HTTP server running...')
    shs_mt.start_server(port)


if __name__ == '__main__':
    # try:
    thread.start_new_thread(httpserver, (8009,))
    thread.start_new_thread(serv_listen, (1221,))
    while 1:
        time.sleep(20)
    # except:
    #     print "Error: unable to start thread"