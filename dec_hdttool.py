# Decomple enc UyenCoder --> By MinhNguyen2412

from builtins import exec, input, len, print, int, range, str, open, exit
exec('')
xnhac = '\x1b[1;36m'
do = '\x1b[1;31m'
luc = '\x1b[1;32m'
vang = '\x1b[1;33m'
xduong = '\x1b[1;34m'
hong = '\x1b[1;35m'
trang = '\x1b[1;39m'
whiteb = '\x1b[1;39m'
red = '\x1b[0;31m'
redb = '\x1b[1;31m'
end = '\x1b[0m'
dev = '\x1b[1;39m[\x1b[1;31m×\x1b[1;39m]\x1b[1;39m'
thanh_xau = red + '[' + vang + '⟨⟩' + red + '] ' + trang + '➩ ' + luc
thanh_dep = trang + '~' + red + '[' + luc + '✓' + red + '] ' + trang + '➩ ' + luc
import requests
import json
import os
import sys
from sys import platform
from datetime import datetime
from time import sleep, strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
os.system('pip install pystyle')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
bug_duoc_cai_lon = {
    'pass': 'bongocvidaii' }

def is_connected():
    import socket
    socket.create_connection(('1.1.1.1', 53))
    return True
    if OSError:
        pass
    return False

os.system('clear')

def banner():
    banner = '\n\x1b[38;5;226m╔═════════════════════════════════════════════════════════════════╗\n\x1b[38;5;226m║\x1b[38;5;207m██╗░░██╗██████╗░████████╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░ \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;226m██║░░██║██╔══██╗╚══██╔══╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░ \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;99m███████║██║░░██║░░░██║░░░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░ \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;46m██╔══██║██║░░██║░░░██║░░░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░ \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;51m██║░░██║██████╔╝░░░██║░░░░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗ \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;208m╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝ \x1b[38;5;226m║\n\x1b[38;5;226m╠═════════════════════════════════════════════════════════════════╣\n\x1b[38;5;226m║\x1b[38;5;46m▶ Nhóm Zalo  : \x1b[38;5;207mhttps://zalo.me/g/bprmyn080                       \x1b[38;5;226m║\n\x1b[38;5;226m║\x1b[38;5;46m▶ Website Share Tool  : \x1b[38;5;207mhttps://beacons.ai/hdttool              \x1b[38;5;226m ║\n\x1b[38;5;226m║\x1b[38;5;46m▶ Bot Spam CALL SMS Telegram : \x1b[38;5;207mhttps://t.me/botspamcallsms \x1b[38;5;226m      ║\n\x1b[38;5;226m╚═════════════════════════════════════════════════════════════════╝\n\x1b[38;5;46m-----------------------------------------------------------------\n'
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0)
        return None

now = datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')

def get_ip_from_url(url):
    return '127.0.0.1'

url = 'http://kiemtraip.com/raw.php'
ip = get_ip_from_url(url)
os.system('clear')
banner()
#a = now.strftime('%d')
#h = int(now.strftime('%d'))
#ngay_trc = h - 2
#ngay_mai = h + 1
#time = datetime.now().strftime('%Hh:%Mp:%Ss')
#b = now.strftime('%m')
#day = now.strftime('%d-%m-%Y')
#today = now.strftime('%d-%m-%Y')
#hientai = now.strftime('%m-%Y')
#ngay = int(strftime('%d'))
#key1 = str(ngay * 1246881999 + 0xAC2626E5L)
#key = 'HDT-' + key1
#keyvip = '881995'
#ip = requests.post('https://api.proxyscrape.com/ip.php').text
#long_url = f'''http://offvn.io.vn/hdt.html?key={key}'''
#ip = requests.post('https://api.proxyscrape.com/ip.php').text
#url_dilink = requests.get(f'''https://dilink.net/api_rv.php?token=r0vl9pwku8l8pwoq04psn1bh9nycvjstjcinbec4l6jara3y7leybxd8e60lhp88d9s6dvt0sxhusl5ozrm7pzq5m2k83k86vlrl&url={long_url}''').text
#ip = requests.post('https://api.proxyscrape.com/ip.php').text
#if '<link rel="canonical" href="' in url_dilink:
#    link_key_dilink = url_dilink.split('<link rel="canonical" href="')[1].split('">')[0]
#link_key_dilink = 'Không Thể Tạo Url!!!'
#file_key = f'''key_ngay{ngay_hom_nay}.txt'''
#file_key_cu = f'''key_ngay{ngay_trc}.txt'''
#check_file_key = os.path.exists(file_key)
#if check_file_key == False:
#print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
#print(f'''{thanh_xau}\x1b[38;5;226mĐÂY LÀ TOOL FREE NÊN KEY SẼ THAY ĐỔI MỖI NGÀY !!''')
#print(f'''{thanh_xau}\x1b[38;5;207mHôm Nay Ngày : \x1b[38;5;46m{ngay_hom_nay}/{thang_nay}/{nam_}''')
#print(f'''{thanh_xau}\x1b[38;5;207mGiờ Hiện Tại : \x1b[38;5;46m{time}''')
#print(f'''{thanh_xau}\x1b[38;5;207mIP Của Bạn Là : \x1b[38;5;46m{ip}''')
#print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
#print(f'''{thanh_xau}\x1b[38;5;46mLink Lấy Key Là : \x1b[38;5;226m{link_key_dilink}''')
#    os.system(f'''termux-open-url {link_key_dilink} ''')
   # ma = input(f'''{thanh_xau}\x1b[38;5;46mNhập API Key Ngày \x1b[38;5;207m{ngay_hom_nay}/{thang_nay}/{nam_}: \x1b[38;5;226m''')
   # if ma == key or ma == keyvip:
   #     print(f'''{thanh_xau}\x1b[38;5;46mAPI Key Chính Xác''')
     #   luu = open(file_key, 'a+')
   #     luu.write(ma)
      #  luu.close()
 #   if ma != key or ma != keyvip:
    #print(f'''{thanh_xau}\x1b[38;5;46mAPI Key Sai''')
#if check_file_key == True:
 #   print(f'''{thanh_xau}\x1b[38;5;46mĐang Lấy Key...''', end = '\r')
 #   sleep(1)
   # k = open(file_key, 'r')
   # ma = k.read()
 #   k.close()
  #  if ma == key or ma != keyvip:
    #    print(f'''{thanh_xau}\x1b[38;5;46mLấy Key Thành Công       ''', end = '\r')
    #    sleep(0.5)
 #   if ma != key or ma != keyvip:
    #    if os.path.exists(file_key) == True:
      #      os.system(f'''rm {file_key}''')
      #  os.system(f'''rm {file_key}''')
      #  print(f'''{thanh_xau}\x1b[38;5;46mAPI Key Sai         ''')
   #     ma = input(f'''{thanh_xau}\x1b[38;5;46mNhập API Key Ngày \x1b[38;5;207m{ngay_hom_nay}/{thang_nay}/{nam_}: \x1b[38;5;226m''')
     #   if ma == key or ma != keyvip:
     #       print(f'''{thanh_xau}\x1b[38;5;46mAPI Key Chính Xác''')
     #       luu = open(file_key, 'a+')
      #      luu.write(ma)
      #      luu.close()
       # if ma != key or ma != keyvip:
         #   print(f'''{thanh_xau}\x1b[38;5;46mAPI Key Sai           ''')
if os.name == 'nt':
    pass
#'cls'('clear')
banner()
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print(f'''{thanh_xau}\x1b[38;5;226mCHÀO MỪNG BẠN ĐÃ VÀO TOOL !!''')
print(f'''{thanh_xau}\x1b[38;5;207mHôm Nay Ngày : \x1b[38;5;46m{ngay_hom_nay}/{thang_nay}/{nam_}''')
print(f'''{thanh_xau}\x1b[38;5;207mGiờ Hiện Tại : \x1b[38;5;46m{Anime}''')
print(f'''{thanh_xau}\x1b[38;5;207mIP Của Bạn Là : \x1b[38;5;46m{ip}''')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;46m-----------------------------------------------------------------')
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTOOL TRAO ĐỔI SUB    \x1b[38;5;208m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;226m[1] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS TIKTOK + TIKTOK NOW')
print('\x1b[38;5;226m[2] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS BẰNG PAGE PRO5')
print('\x1b[38;5;226m[3] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS FACEBOOK FULL JOD')
print('\x1b[38;5;226m[4] \x1b[38;5;46mTOOL \x1b[38;5;51mTDS INSTAGRAM')
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTOOL TƯƠNG TÁC CHÉO  \x1b[38;5;208m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;226m[5] \x1b[38;5;46mTOOL \x1b[38;5;51mTTC PAGE PRO5\x1b[38;5;226m [ Mới ]')
print('\x1b[38;5;226m[6] \x1b[38;5;46mTOOL \x1b[38;5;51mTTC INSTAGRAM VIPIG')
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTOOL TIỆN ÍCH PRO5   \x1b[38;5;208m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;226m[7] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF CẢM XÚC STORY BẰNG PRO5')
print('\x1b[38;5;226m[8] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF VIEW STORY BẰNG PRO5')
print('\x1b[38;5;226m[9] \x1b[38;5;46mTOOL \x1b[38;5;51mKÍCH HOẠT PAGE PRO5')
print('\x1b[38;5;226m[10] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF FOLOW BẰNG PAGE PRO5')
print('\x1b[38;5;226m[11] \x1b[38;5;46mTOOL \x1b[38;5;51mCHUYỂN QUYỀN QTV PRO5')
print('\x1b[38;5;226m[12] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF TV NHÓM BẰNG PAGE PRO5')
print('\x1b[38;5;226m[13] \x1b[38;5;46mTOOL \x1b[38;5;51mREG PAGE PRO5 + ÚP ĐẠI DIỆN')
print('\x1b[38;5;226m[14] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF SHARE BẰNG PAGE PRO5\x1b[38;5;226m [ Mới ]')
print('\x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗')
print('\x1b[38;5;208m║ \x1b[38;5;207mTOOL TIỆN ÍCH KHÁC   \x1b[38;5;208m ║')
print('\x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝')
print('\x1b[38;5;226m[15] \x1b[38;5;46mTOOL \x1b[38;5;51mKẾT BẠN FACEBOOK GỢI Ý')
print('\x1b[38;5;226m[16] \x1b[38;5;46mTOOL \x1b[38;5;51mNUÔI NICK FACEBOOK')
print('\x1b[38;5;226m[17] \x1b[38;5;46mTOOL \x1b[38;5;51mGET TOKEN FACEBOOK')
print('\x1b[38;5;226m[18] \x1b[38;5;46mTOOL \x1b[38;5;51mLỌC PROXY')
print('\x1b[38;5;226m[19] \x1b[38;5;46mTOOL \x1b[38;5;51mTẤN CÔNG WEBSITE')
print('\x1b[38;5;226m[20] \x1b[38;5;46mTOOL \x1b[38;5;51mGET TOKEN PAGE PRO5')
print('\x1b[38;5;226m[21] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF VIEW TIKTOK \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[22] \x1b[38;5;46mTOOL \x1b[38;5;51mSPAM CALL SMS\x1b[38;5;207m [ MỚI ]')
print('\x1b[38;5;226m[23] \x1b[38;5;46mTOOL \x1b[38;5;51mREG ACC GARENA')
print('\x1b[38;5;226m[24] \x1b[38;5;46mTOOL \x1b[38;5;51mREG PAGE VỊ TRÍ')
print('\x1b[38;5;226m[25] \x1b[38;5;46mTOOL \x1b[38;5;51mSPAM MESSENGER')
print('\x1b[38;5;226m[26] \x1b[38;5;46mTOOL \x1b[38;5;51mGET COOKIE PAGE THƯỜNG + PRO5')
print('\x1b[38;5;226m[27] \x1b[38;5;46mTOOL \x1b[38;5;51mTAG TÊN NGƯỜI KHÁC VÀO TIỂU SỬ FACEBOOK')
print('\x1b[38;5;226m[28] \x1b[38;5;46mTOOL \x1b[38;5;51mTĂNG LIKE BÀI VIẾT FACEBOOK')
print('\x1b[38;5;226m[29] \x1b[38;5;46mTOOL \x1b[38;5;51mBUFF LIKE TIKTOK')
print('\x1b[38;5;226m[30] \x1b[38;5;46mTOOL \x1b[38;5;51mSPAM + CALL \x1b[38;5;226m[ Mới ] ')
print('\x1b[38;5;226m[31] \x1b[38;5;46mTOOL \x1b[38;5;51mDECODE FILE Kramer\x1b[38;5;207m [ VIP ]')
print('\x1b[38;5;226m[32] \x1b[38;5;46mTOOL \x1b[38;5;51mDECODE FILE Hyperion\x1b[38;5;207m [ VIP ]')
print('\x1b[38;5;226m[33] \x1b[38;5;46mTOOL \x1b[38;5;51mDECODE FILE Marshal/PYC\x1b[38;5;207m [ VIP ]')
print('\x1b[38;5;226m[34] \x1b[38;5;46mTOOL \x1b[38;5;51mXEM COMMENT VIDEO TIKTOK')
print('\x1b[38;5;226m[35] \x1b[38;5;46mTOOL \x1b[38;5;51mKÉO MEM TELEGRAM')
print('\x1b[38;5;226m[36] \x1b[38;5;46mTOOL \x1b[38;5;51mGOLIKE TIKTOK \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[37] \x1b[38;5;46mTOOL \x1b[38;5;51mGmail 12 CHẾ ĐỘ \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[38] \x1b[38;5;46mTOOL \x1b[38;5;51mKết Xuất Bạn Bè Không Giới Hạn \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[39] \x1b[38;5;46mTOOL \x1b[38;5;51mGet ID User Facebook + Instagram \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[40] \x1b[38;5;46mTOOL \x1b[38;5;51mGet Token 16 Loại Facebook Thường + Page Pro5 \x1b[38;5;226m[ Mới ]')
print('\x1b[38;5;226m[41] \x1b[38;5;46mTOOL \x1b[38;5;51mBuff Comment Bằng Page Pro5 \x1b[38;5;207m[ Mới ]')
print('\x1b[38;5;46m-----------------------------------------------------------------')
chon = int(input('\x1b[38;5;46m▶ Nhập Số \x1b[1;32m: \x1b[38;5;226m'))
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 1:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/tiktok.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 2:
    exec(requests.get('http://off-vn.x10.mx/tdspro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 3:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/tdsfulljod.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 4:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/Instagram.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 5:
    exec(requests.get('http://off-vn.x10.mx/ttcpro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 6:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/ttcvipig.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 7:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/strpro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 8:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/viewstr.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 9:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/kichhoat.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 10:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/flpro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 11:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/qtvpro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 12:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/tvnhompro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 13:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/regpro5.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 14:
    exec(requests.get('http://off-vn.x10.mx/share.py').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 15:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/ketban.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 16:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/nuoifb.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 17:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/gettokenfb.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 18:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/getproxy.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 19:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/dossweb.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 20:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/gettoken.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 21:
    exec(requests.get('http://off-vn.x10.mx/tik.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 22:
    exec(requests.get('http://off-vn.x10.mx/spamvip.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 23:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/reggarena.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 24:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/regvt.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 25:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/mes.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 26:
    exec(requests.get('https://run.mocky.io/v3/c75abbd1-354a-4b37-ab16-673bbcbe3082').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 27:
    exec(requests.get('https://run.mocky.io/v3/c1bca812-eae6-472c-b86c-1827bb779712').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 28:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/tanglike.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 29:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/tym.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 30:
    exec(requests.get('http://off-vn.x10.mx/sms.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 31:
    exec(requests.get('http://off-vn.x10.mx/kramer.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 32:
    exec(requests.get('http://off-vn.x10.mx/hyperion.html').text)
ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 33:
    exec(requests.get('http://off-vn.x10.mx/marshal_pyc.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 34:
    exec(requests.get('https://run.mocky.io/v3/823ebd35-7b3f-407c-830a-fa272e26d6d0').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 35:
    exec(requests.get('http://off-vn.x10.mx/telegram.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 36:
    exec(requests.get('https://raw.githubusercontent.com/hdttool/HDT-TOOL/main/golike.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 37:
    exec(requests.get('http://off-vn.x10.mx/gmailvip.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 38:
    exec(requests.get('http://off-vn.x10.mx/xembb.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 39:
    exec(requests.get('http://off-vn.x10.mx/getid.html').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 40:
    exec(requests.get('http://off-vn.x10.mx/gettoken.py').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
if chon == 41:
    exec(requests.get('http://off-vn.x10.mx/comments.py').text)
    ip = requests.post('https://api.proxyscrape.com/ip.php').text
#    return None
print(' Sai Lựa Chọn ')
exit()
