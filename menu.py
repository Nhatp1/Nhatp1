import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
def get_ip_from_url(url):
    # response = requests.get(url)
    # ip_address = socket.gethostbyname(response.text.strip())
    # return ip_address
    return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url
import os
import requests
from time import strftime
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_key_to_file(key, filename='NhatTool-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='NhatTool-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None


def fetch_shortened_url(url, token):
    try:
        encoded_url = urllib.parse.quote(url)
        api_url = f'https://yeumoney.com/QL_api.php?token={token}&url={encoded_url}&format=json'
        try:
            response = requests.get(api_url)
        except:
            print('Vui Lòng Kết Nối Mạng !')
            exit("")
        response.raise_for_status()
        result = response.json()
        if result["status"] == "success":
            return result["shortenedUrl"]
        else:
            return result["status"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching shortened URL: {e}"


def main():
    clear_screen()

    ngay = int(strftime('%d'))
    key = "NhatTool" + str(ngay * 2593885817 + 4610273)
    key = "nhatkeyvip"

    saved_key = load_key_from_file()

    if saved_key == key:
        print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')
    else:

        url = f'https://taoweb1s.net/key-tool?key={key}'
        token_link1s = "432c9b236e4e2a7ca16f55b2029fe3461c78be79bb267c98e4f80f49303dbab3"
        link_key = fetch_shortened_url(url, token_link1s)

        if link_key is None:
            print("Unable to generate shortened URL. Please try again later.")
            return

        nhap_key = input(f'''
   \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
        \x1b[38;5;226mĐÂY LÀ TOOL FREE NÊN KEY SẼ THAY ĐỔI MỖI NGÀY !!
        \x1b[38;5;207mHôm Nay Ngày : \x1b[38;5;46m{thu}/{ngay_hom_nay}/{thang_nay}/{nam_}
        \x1b[38;5;207mGiờ Hiện Tại : \x1b[38;5;46m{gio_hien_tai}
        \x1b[38;5;207mIP Của Bạn Là : \x1b[38;5;46m
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝
   \x1b[38;5;46mLink Lấy Key Là : \x1b[38;5;226m{link_key}
   \033[1;32m Nhập Key để Vào Tool : ''')

        if nhap_key == key:
            print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')

            save_key_to_file(nhap_key)
        else:
            print('\033[1;31m Key Sai Vui Lòng Vượt Link Để lấy')
            quit()


if __name__ == "__main__":
    main()
banner = '''   \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
        \x1b[38;5;226m CHÚC MỌI NGƯỜI MỘT NGÀY VUI VẼ!!
        \x1b[38;5;207mBOX ZALO : \x1b[38;5;46mhttps://zalo.me/g/ozebne540
        \x1b[38;5;207m ADMIN : \x1b[38;5;46m NHẬT TOOL
        \x1b[38;5;207m MUA KEY VIP LIÊN HỆ ZALO (500đ/1day) \x1b[38;5;46m
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝

'''
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║  TOOL Trao Đổi Sub  ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [1] TDS TIKTOK MAX SPEED [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [2] TDS BẰNG PAGE PRO5 [TẠM] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [3] TDS FACEBOOK FULL JOD [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [4] TDS INSTAGRAM MAX SPEED  [MỚI] \n',Colors.white,interval=0.0001)

Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL FACEBOOK ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [0.1] TOOL BUFF VIEW FB BẰNG PRO5 [ỔN ĐỊNH]\n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [0.2] TOOL SHARE ẢO FB [NGON]\n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [0.3] TOOL ADD BẠN BÈ [NGON]\n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [0.4] TOOL NUÔI FACEBOOK [NGON] \n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [0.5] TOOL COMMENTS FACEBOOK [NGON]\n',Colors.white,interval=0.0001)
Write.Print('[⟨⟩]➩ Nhập Số [0.6] TOOL REG PRO5 + UP AVATAR [NGON] \n',Colors.white,interval=0.0001)

Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL GOLIkE  ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [5] TOOL GOLKIE TIKTOK [VIP] \n',Colors.white,interval=0.0001)

Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL TIKTOK ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [6] TOOL VIEW TIKTOK [HAY LỖI] \n',Colors.white,interval=0.0001)
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL ENCODE + DECODE║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [7] TOOL ENCODE [NGON]\n',Colors.white,interval=0.0001)
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL GỘP KHÁC ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [8] TOOL GỘP HDT-TOOL \n',Colors.white,interval=0.0001)
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL VIP        ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [9] TOOL TẤN CÔNG WEB [NGON] \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [10] TOOL CÀY HAMTER [VIP]  \n',Colors.yellow,interval=0.0001,end='\r')
import requests

chon = str(input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tdstiktok.py').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tdspro5.py').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tdsfb.py').text)
elif chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tdsig.py').text)
elif chon == '5':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/golike.py').text)
elif chon == '0.1':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/viewfb.py').text)
elif chon == '0.2':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/shareao.py').text)
elif chon == '0.3':
	exec(requests.get(' https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/addbb.py').text)
elif chon == '0.4':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/nuoifb.py').text)
elif chon == '6':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tim.py').text)
elif chon == '7':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/enc.py').text)
elif chon == '0.5':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/cmt.py').text)
elif chon == '8':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/dec_hdttool.py').text)
elif chon == '9':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/ddos.py').text)
elif chon == '0.6':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/regpro5.py').text)
elif chon == '10':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/hamter.py').text)

else:
    print("Sai Lựa Chọn")
    exit()
    
