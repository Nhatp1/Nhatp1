import os
import sys
import time
import struct
import socket
import requests
from pystyle import *
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

banner = """
  \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
  \033[1;36m ███╗   ██╗██╗  ██╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m ████╗  ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;36m ██╔██╗ ██║███████║███████║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║╚██╗██║██╔══██║██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║ ╚████║██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;36m ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
        \x1b[38;5;226m CHÚC MỌI NGƯỜI MỘT NGÀY VUI VẼ!!
        \x1b[38;5;207mBOX ZALO : \x1b[38;5;46mhttps://zalo.me/g/ozebne540
        \x1b[38;5;207m ADMIN : \x1b[38;5;46m NHẬT TOOL
        \x1b[38;5;207m MUA KEY VIP LIÊN HỆ ZALO: 0386358592 (500đ/1day) \x1b[38;5;46m
        \x1b[38;5;207m BOT SPAM SMS: https://t.me/sharebotvip \x1b[38;5;207m
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝
            `'''''''''
            
[!] danploit priv proxy checker

"""

def country_http(proxy):
    ip, port = proxy.split(':')
    url = f'http://ip-api.com/json/{ip}'
    country = 'N/A'
    ip_response = requests.get(url)
    if ip_response.status_code == 200:
        ip_data = ip_response.json()
        country = ip_data.get('country', 'N/A')
    print('-| {:<35} --> {}[ HTTP ] [ {} ]'.format(proxy, fg, country))
    if country != 'N/A':
        with open('http.txt', 'a') as file:
            file.write(f"{proxy}\n")
    else:
        print(' -| {:<35} --> {}[ Unknown Country ]'.format(proxy, fr, e))

def country_https(proxy):
    ip, port = proxy.split(':')
    url = f'http://ip-api.com/json/{ip}'
    country = 'N/A'
    ip_response = requests.get(url)
    if ip_response.status_code == 200:
        ip_data = ip_response.json()
        country = ip_data.get('country', 'N/A')
    print('-| {:<35} --> {}[ HTTPs ] [ {} ]'.format(proxy, fg, country))
    if country != 'N/A':
        with open('https.txt', 'a') as file:
            file.write(f"{proxy}\n")
    else:
        print(' -| {:<35} --> {}[ Unknown Country ]'.format(proxy, fr, e))
        
def country_socks5(proxy):
    ip, port = proxy.split(':')
    url = f'http://ip-api.com/json/{ip}'
    country = 'N/A'
    ip_response = requests.get(url)
    if ip_response.status_code == 200:
        ip_data = ip_response.json()
        country = ip_data.get('country', 'N/A')
    print('-| {:<35} --> {}[ SOCKS5 ] [ {} ]'.format(proxy, fg, country))
    if country != 'N/A':
        with open('socks5.txt', 'a') as file:
            file.write(f"{proxy}\n")
    else:
        print(' -| {:<35} --> {}[ Unknown Country ]'.format(proxy, fr, e))
        
def country_socks4(proxy):
    ip, port = proxy.split(':')
    url = f'http://ip-api.com/json/{ip}'
    country = 'N/A'
    ip_response = requests.get(url)
    if ip_response.status_code == 200:
        ip_data = ip_response.json()
        country = ip_data.get('country', 'N/A')
    print('-| {:<35} --> {}[ SOCKS4 ] [ {} ]'.format(proxy, fg, country))
    if country != 'N/A':
        with open('socks4.txt', 'a') as file:
            file.write(f"{proxy}\n")
    else:
        print(' -| {:<35} --> {}[ Unknown Country ]'.format(proxy, fr, e))
        
def socks5_proxy(proxy):
    try:
        ip, port = proxy.split(':')
        port = int(port)
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.settimeout(5)
        proxy_socket.connect((ip, port))
        proxy_socket.sendall(b'\x05\x01\x00')
        response = proxy_socket.recv(2)
        proxy = f"{ip}:{port}"
        if response == b'\x05\x00':
            country_socks5(proxy)
        else:
            print(' -| {:<35} --> {}[ Dead Proxy ]'.format(proxy, fr))
        proxy_socket.close()
    except socket.error as e:
        print(' -| {:<35} --> {}[ {} ]'.format(proxy, fr, e))

def socks4_proxy(proxy):
    try:
        ip, port = proxy.split(':')
        port = int(port)
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.settimeout(5)
        proxy_socket.connect((ip, port))
        request_data = struct.pack('!BBH4s', 4, 1, port, socket.inet_aton('0.0.0.1'))
        proxy_socket.sendall(request_data)
        response_data = proxy_socket.recv(8)
        version, status, _ = struct.unpack('!BBH', response_data[:4])
        if version == 0 and status == 0x5A:
            country_socks4(proxy)
        else:
            print(' -| {:<35} --> {}[ Dead Proxy ]'.format(proxy, fr))
        proxy_socket.close()
    except socket.error as e:
        print(' -| {:<35} --> {}[ {} ]'.format(proxy, fr, e))
        
def http_proxy(proxys):
    ip, port = proxys.split(':')
    port = int(port)
    proxy = f"{ip}:{port}"
    url = 'http://google.com/'
    try:
        response = requests.get(url, proxies={'http': proxy}, timeout=5)
        if response.status_code == 200:
            country_http(proxy)
        else:
            print(' -| {:<35} --> {}[ Dead Proxy ]'.format(proxy, fr))
    except requests.RequestException:
        print(' -| {:<35} --> {}[ Connection Timeout ]'.format(proxy, fr))

def https_proxy(proxys):
    ip, port = proxys.split(':')
    port = int(port)
    proxy = f"{ip}:{port}"
    url = 'https://google.com/'
    try:
        response = requests.get(url, proxies={'https': proxy}, timeout=5)
        if response.status_code == 200:
            country_https(proxy)
        else:
            print(' -| {:<35} --> {}[ Dead Proxy ]'.format(proxy, fr))
    except requests.RequestException:
        print(' -| {:<35} --> {}[ Connection Timeout ]'.format(proxy, fr))
        

def check(proxys):
    try:
        ip, port = proxys.split(':')
        port = int(port)
        proxy = f"{ip}:{port}"
        socks4_proxy(proxy)
        socks5_proxy(proxy)
        http_proxy(proxy)
        https_proxy(proxy)
    except socket.error as e:
        print(' -| {:<35} --> {}[ {} ]'.format(proxy, fr, e))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\n\n\n\nGunakan: python3 script.py <proxyname>\nContoh: python3 script.py proxy.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print(f'File "{file_name}" tidak di temukan !')
        sys.exit(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner)))
    time.sleep(2)
    
    with open(file_name, 'r') as proxy_file:
        proxies = proxy_file.read().splitlines()

    with ThreadPoolExecutor(max_workers=90) as executor:
        executor.map(check, proxies)
