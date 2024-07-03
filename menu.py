import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup

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

ngay = int(strftime('%d'))
key1 = str(ngay * 5868756 + 74356421)
keyvip = 'nhatlo'
key = 'nhattool' + key1
if not os.path.exists('key_nhattool.txt'):
    url = 'https://luvanlong.000webhostapp.com/key.html?key=' + key
    token_web1s = 'b39bf9e1-9fb7-4d49-897e-fbac842b5bd0'
    web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()

    # Check if there's an error with retrieving the key
    if web1s['status'] == "error":
        print(web1s['message'])
        quit()
    else:
        link_key = web1s['shortenedUrl']
        print("\033[1;33mTool Free Nên Sẽ Đổi Key Mỗi Ngày\033[1;33m")
        print("\033[1;35m ============================================  ")
        print('\033[1;36mVượt Link Để Lấy Key Free: \033[1;37m' + link_key)

        # Prompt the user to enter the purchased or obtained key
        keynhap = input('\033[1;34mKey Đã Mua Hoặc Vượt Là: \033[1;33m')
        if keynhap == key:
                    print('Key Chính Xác')
 #                   with open('key_nhattool.txt', 'w') as f:
     #                   f.write(keynhap)
        else:
            print('Key Sai Rồi Kìa')
            quit()
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
#THU 
def banner():
  banner = '''

  '''
  for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
banner()
print('')
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
Write.Print('║TOOL VIP ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[⟨⟩]➩ Nhập Số [9] TOOL TẤN CÔNG WEB [NGON] \n',Colors.yellow,interval=0.0001,end='\r')
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


else:
    print("Sai Lựa Chọn")
    exit()
